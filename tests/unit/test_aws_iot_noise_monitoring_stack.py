import aws_cdk as core
import aws_cdk.assertions as assertions

from aws_iot_noise_monitoring.aws_iot_noise_monitoring_stack import AwsIotNoiseMonitoringStack

# example tests. To run these tests, uncomment this file along with the example
# resource in aws_iot_noise_monitoring/aws_iot_noise_monitoring_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = AwsIotNoiseMonitoringStack(app, "aws-iot-noise-monitoring")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
