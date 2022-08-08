import json

import boto3
import pathlib


iot = boto3.client('iot')


def get_all_things():
    things_dict = iot.list_things()['things']
    things = {thing['thingName'] for thing in things_dict}
    return things


def create_device(device_id):
    """
    Creates an IoT Thing, keys and certificates, attaches policies and writes its info in a file.
    """
    pathlib.Path(f"devices/{device_id}").mkdir(parents=True, exist_ok=True)
    thing_info_file = pathlib.Path(f"devices/{device_id}/thing_info.json")

    response = iot.create_thing(thingName=device_id)
    response.pop('ResponseMetadata')
    with thing_info_file.open(mode='w') as info_file:
        print(json.dumps(response, indent=4), file=info_file)

    # create keys
    certificate_arn = create_keys_and_certificate(device_id)

    # attach policy to certificate
    iot.attach_policy(
        policyName="sunbird-IoT-Policy",
        target=certificate_arn
    )

    # attach thing to certificate
    iot.attach_thing_principal(
        thingName=device_id,
        principal=certificate_arn
    )

    return response


def create_keys_and_certificate(device_id):
    """
    Creates keys and certificates and writes them to the devices folder.
    Returns the ARN for the certificate
    """
    response = iot.create_keys_and_certificate(setAsActive=True)
    response.pop('ResponseMetadata')
    certificate_file = pathlib.Path(f"devices/{device_id}/certificate.pem.crt")
    private_key_file = pathlib.Path(f"devices/{device_id}/private.pem.key")
    certificate_info_file = pathlib.Path(f"devices/{device_id}/cert_info.json")

    with certificate_file.open(mode='w') as cert_file:
        cert_file.writelines(response['certificatePem'])

    with private_key_file.open(mode='w') as private_file:
        private_file.writelines(response['keyPair']['PrivateKey'])

    with certificate_info_file.open(mode='w') as info_file:
        print(json.dumps(response, indent=4), file=info_file)

    return response['certificateArn']


def create_multiple_devices(device_ids):
    things = get_all_things()
    for device_id in device_ids:
        if device_id in things:
            print(f"{device_id} already exists, skipping")
        else:
            print(f"Creating {device_id}...")
            resp = create_device(device_id)
            print(f"Successfully created {device_id} with ARN: {resp['thingArn']}")
        print(f"===========================================")
        print(f"===========================================")


if __name__ == '__main__':
    # resp = create_device("SB1001")
    # print(json.dumps(resp, indent=4))
    create_multiple_devices(["SB1001", "SB1002", "SB1003"])
