from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
)
from constructs import Construct

class Project10Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #This is where the first VPC is made.
        vpc_1 = ec2.Vpc(
        self, "VPC_1",
        cidr="10.10.10.0/24",
        max_azs=2,
        nat_gateways=0,
        subnet_configuration=[
            ec2.SubnetConfiguration(name="public", cidr_mask=26, subnet_type=ec2.SubnetType.PUBLIC),
        ]
    )   

        #THis is where the second VPC is made.
        vpc_2 = ec2.Vpc(
        self, "VPC_2",
        cidr="10.20.20.0/24",
        max_azs=2,
        nat_gateways=0,
        subnet_configuration=[
            ec2.SubnetConfiguration(name="public", cidr_mask=26, subnet_type=ec2.SubnetType.PUBLIC),
        ]
    )

        #This is where the VPC peering is enabled.
        VPC_Peering_connection = ec2.CfnVPCPeeringConnection(self, "VPCPeeringConnection",
        peer_vpc_id=vpc_2.vpc_id,
        vpc_id=vpc_1.vpc_id,
    
    )

        #This is where the AMI for the webserver/management server is decribed.
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
    
     )

        #This is where the webserver is deployed. 
        instance = ec2.Instance(self, "Webserver",
        instance_type=ec2.InstanceType("t2.micro"),
        machine_image=amzn_linux,
        vpc = vpc_1,
        #role = role
            
    )

        #This is where the managament server is deployed. 
        instance = ec2.Instance(self, "Managementserver",
        instance_type=ec2.InstanceType("t2.micro"),
        machine_image=amzn_linux,
        vpc = vpc_2,
        #role = role
    
    )
