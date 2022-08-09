import boto3
from create_cloudwatch_dashboards.dashboard_template import get_dashboard_body

cloudwatch = boto3.client("cloudwatch")


def create_device_dashboard(device_id):
    dashboard_body = get_dashboard_body(device_id)
    response = cloudwatch.put_dashboard(DashboardName=f"{device_id}-dashboard", DashboardBody=dashboard_body)
    print(response)


if __name__ == '__main__':
    create_device_dashboard("SB1001")
    create_device_dashboard("SB1002")
