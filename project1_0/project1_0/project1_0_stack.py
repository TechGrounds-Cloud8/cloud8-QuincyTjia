#from unittest.main import _TestRunner
from aws_cdk import (
    aws_ec2 as ec2,
    Stack,
)
from constructs import Construct

class Project10Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #This is where the webserver VPC is made.
        vpc_webserver = ec2.Vpc(
            self, "VPC_1",
            cidr="10.10.10.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PUBLIC),
                ]
        )   

        #THis is where the managamentserver VPC is made.
        vpc_managementserver = ec2.Vpc(
            self, "VPC_2",
            cidr="10.20.20.0/24",
            max_azs=2,
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PUBLIC),
                ]
        )

        #This is where the VPC peering is enabled.
        VPC_Peering_connection = ec2.CfnVPCPeeringConnection(
            self, "VPCPeeringConnection",
            peer_vpc_id=vpc_managementserver.vpc_id,
            vpc_id=vpc_webserver.vpc_id,
        )

        #This is where the AMI for the webserver/management server is decribed.
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        #This is where the user data is described.
        userdata_webserver = ec2.UserData.for_linux()
        userdata_webserver.add_commands(
                    """
                    yum -y install httpd
                    systemctl enable httpd
                    systemctl start httpd
                    echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
                    """
        )

        #Create a security group for the VPC webserver.
        SG_webserver = ec2.SecurityGroup(
            self, "Webserver SG",
            vpc=vpc_webserver,
            allow_all_outbound=True

        )

        #Create a rule that allows HTTP traffic.
        SG_webserver.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80)

        )
        
        #Create a rule that allows HTTPS traffic. 
        SG_webserver.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            
        )
        #This is where the webserver is deployed. 
        instance_webserver = ec2.Instance(
            self, "Webserver",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=amzn_linux,
            vpc = vpc_webserver,
            user_data = userdata_webserver,
            security_group = SG_webserver,
            
        )
        
        #This is where the managament server is deployed. 
        instance_managementserver = ec2.Instance(
            self, "Managementserver",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=amzn_linux,
            vpc = vpc_managementserver,
            #role = role
        )
        

