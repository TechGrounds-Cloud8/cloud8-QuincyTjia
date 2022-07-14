#from unittest.main import _TestRunner
from aws_cdk import (
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    Stack,
)
import aws_cdk
from constructs import Construct

class Project10Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

            ########
        #### VPC's #####
            ########

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

            ########
        #### SG's #####
            ########

        #Create a security group for the webserver.
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

        #Create a security group for the management server.
        SG_managementserver = ec2.SecurityGroup(
            self, "Managementserver SG",
            vpc=vpc_managementserver,
            allow_all_outbound=True

        )

        #Create a rule that allows SSH connection from a trusted IP (have to be added later)
        SG_managementserver.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(22)

        )

            ########
        #### NACL's #####
            ########

        #Create a NACL for the webserver.
        NACL_webserver = ec2.NetworkAcl(
            self, "Webserver NACL",
            vpc = vpc_webserver,
            subnet_selection = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PUBLIC
            )

        )

        #This is where I add the inbound HTTP rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow inbound HTTP traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 100,
            traffic = ec2.AclTraffic.all_traffic().tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTP rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow outbound HTTP traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 100,
            traffic = ec2.AclTraffic.all_traffic().tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound HHTPS rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 110,
            traffic = ec2.AclTraffic.all_traffic().tcp_port(443),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTPS rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow outbound HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 110,
            traffic = ec2.AclTraffic.all_traffic().tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound Ephemeral rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow inbound Ephemeral traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 130,
            traffic = ec2.AclTraffic.all_traffic().tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound Ephemeral rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow outbound Ephemeral traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 130,
            traffic = ec2.AclTraffic.all_traffic().tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,

        )
         #Create a NACL for the managementserver.
        NACL_managementserver = ec2.NetworkAcl(
            self, "Managementserver NACL",
            vpc = vpc_managementserver,
            subnet_selection = ec2.SubnetSelection(
                subnet_type = ec2.SubnetType.PUBLIC
            )
        
        )

         #This is where I add the inbound SSH rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow inbound SSH traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 120,
            traffic = ec2.AclTraffic.all_traffic().tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound SSH rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound SSH traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 120,
            traffic = ec2.AclTraffic.all_traffic().tcp_port(22),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

             #####
        #### S3 #####
            #####

        #This is where the S3 bucket is created.
        Bucket = s3.Bucket(
            self, "Bucket with scripts",
            bucket_name = "postdeploymentscripts",
            removal_policy = aws_cdk.RemovalPolicy.DESTROY,
            auto_delete_objects = True,
        )

        #This is where the user data script is uploaded to the S3 bucket. 
        user_data_upload = s3deploy.BucketDeployment(
            self, "Deploy_assets_dir",
            destination_bucket = Bucket,
            sources = [s3deploy.Source.asset("/Users/quinc/OneDrive/Documenten/GitHub/cloud8-QuincyTjia/project1_0/project1_0/Assets")],
        )
            
            ###########
        #### Instances #####
            ###########

        #This is where the AMI for the webserver/management server is decribed.
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        #This is where the user data is described.
        userdata_webserver = ec2.UserData.for_linux()
        file_script_path = userdata_webserver.add_s3_download_command(
            bucket = Bucket,
            bucket_key = "webserver.sh",            
        )

        userdata_webserver.add_execute_file_command(file_path = file_script_path) 

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
            security_group = SG_managementserver,
            #role = role
        )
        