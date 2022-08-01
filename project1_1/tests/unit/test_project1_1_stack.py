import aws_cdk as core
import aws_cdk.assertions as assertions

from project1_1.project1_1_stack import Project11Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in project1_1/project1_1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Project11Stack(app, "project1-1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
