import aws_cdk as core
import aws_cdk.assertions as assertions

from project1_0.project1_0_stack import Project10Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in project1_0/project1_0_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Project10Stack(app, "project1-0")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
