from asyncio import events
from calendar import month
from aws_cdk import (
    Duration,
    RemovalPolicy,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy,
    aws_iam as iam,
    aws_backup as backup,
    aws_events as events,
    aws_kms as kms,

    Stack,
)

import aws_cdk
from constructs import Construct

trusted_ip = "84.106.100.87/32"

class Project11Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

             ########
        #### VPC's #####
            ########

        #This is where the webserver VPC is made.
        vpc_webserver = ec2.Vpc(
            self, "VPC_1",
            cidr="10.10.10.0/24",
            max_azs=1,
            nat_gateways=1,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="private", 
                    cidr_mask=26, 
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT
                ),
                ec2.SubnetConfiguration(
                    name ="public",
                    cidr_mask = 26,
                    subnet_type = ec2.SubnetType.PUBLIC
                )
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

        #This is where the routing table for the adminserver is configured.
        for subnet in vpc_managementserver.public_subnets:
            ec2.CfnRoute(
                self, 
                id = f"{subnet.node.id} Managementserver Route Table",
                route_table_id = subnet.route_table.route_table_id,
                destination_cidr_block = "10.10.10.0/24", 
                vpc_peering_connection_id = VPC_Peering_connection.ref,
        )
        
        #This is where the routing table for the webserver is configured.
        for subnet in vpc_webserver.public_subnets:
            ec2.CfnRoute(
                self,
                id = f"{subnet.node.id} Webserver Route Table",
                route_table_id = subnet.route_table.route_table_id,
                destination_cidr_block = "10.20.20.0/24", 
                vpc_peering_connection_id = VPC_Peering_connection.ref,
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
            ec2.Port.tcp(80),

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

        #Create a rule that allows SSH connection from a trusted IP.
        SG_managementserver.add_ingress_rule(
            ec2.Peer.ipv4(trusted_ip),
            ec2.Port.tcp(22),

        )

        #Create a rule that allows RDP connection from a trusted IP.
        SG_managementserver.add_ingress_rule(
            ec2.Peer.ipv4(trusted_ip),
            ec2.Port.tcp(3389),

        )

        #Create a rule that allows HTTP traffic.
        SG_managementserver.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),

        )

        #Create a rule that allows HTTPS traffic. 
        SG_managementserver.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            
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
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTP rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow outbound HTTP traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 100,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound HHTPS rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTPS rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow outbound HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 110,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound Ephemeral rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow inbound Ephemeral traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound Ephemeral rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow outbound Ephemeral traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 120,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,

        )

        #This is where I add the inbound SSH rule for the webserver NACL.
        NACL_webserver.add_entry(
            id = "Allow inbound SSH traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 125,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
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
            cidr = ec2.AclCidr.ipv4(trusted_ip), 
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound SSH rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound SSH traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 130,
            traffic = ec2.AclTraffic.tcp_port(22),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound Ephemeral for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow inbound Ephemeral",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 140,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound Ephemeral for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound Ephemeral",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 140,
            traffic = ec2.AclTraffic.tcp_port_range(1024, 65535),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound RDP for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow inbound RDP",
            cidr = ec2.AclCidr.ipv4(trusted_ip), 
            rule_number = 150,
            traffic = ec2.AclTraffic.tcp_port(3389),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound RDP for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound RDP",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 150,
            traffic = ec2.AclTraffic.tcp_port(3389),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound HTTP rule for the Managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow inbound HTTP traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 160,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTP rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound HTTP traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 160,
            traffic = ec2.AclTraffic.tcp_port(80),
            direction = ec2.TrafficDirection.EGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the inbound HHTPS rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 170,
            traffic = ec2.AclTraffic.tcp_port(443),
            direction = ec2.TrafficDirection.INGRESS,
            rule_action = ec2.Action.ALLOW,
        )

        #This is where I add the outbound HTTPS rule for the managementserver NACL.
        NACL_managementserver.add_entry(
            id = "Allow outbound HTTPS traffic",
            cidr = ec2.AclCidr.any_ipv4(), 
            rule_number = 170,
            traffic = ec2.AclTraffic.tcp_port(443),
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
            enforce_ssl = True,
            encryption = s3.BucketEncryption.S3_MANAGED,
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

        #This is where the AMI for the webserver server is decribed.
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=ec2.AmazonLinuxEdition.STANDARD,
            virtualization=ec2.AmazonLinuxVirt.HVM,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        #THis is where the AMI for the managementserver is described.
        Windows_AMI = ec2.WindowsImage(ec2.WindowsVersion.WINDOWS_SERVER_2022_ENGLISH_FULL_BASE)
        
        #This is where the user data for the webserver is downloaded.
        userdata_webserver = ec2.UserData.for_linux()
        file_script_path = userdata_webserver.add_s3_download_command(
            bucket = Bucket,
            bucket_key = "webserver.sh",            
        )

        userdata_webserver.add_execute_file_command(file_path = file_script_path) 

        #This is where the index page is downloaded.
        userdata_webserver.add_s3_download_command(
            bucket = Bucket,
            bucket_key = "index.html",
            #local_file = "/tmp/index.html",
            local_file = "/var/www/html/",
        )

        userdata_webserver.add_commands("chmod 755 -R /var/www/html/")

        userdata_webserver.add_execute_file_command(file_path = "/var/www/html/")
        
        #This is where the webserver is deployed. 
        instance_webserver = ec2.Instance(
            self, "Webserver",
            instance_type=ec2.InstanceType("t2.micro"),
            machine_image=amzn_linux,
            vpc = vpc_webserver,
            user_data = userdata_webserver,
            security_group = SG_webserver,
            key_name = "project_1_0",
            block_devices = [ec2.BlockDevice(
                device_name = "/dev/xvda",
                volume = ec2.BlockDeviceVolume.ebs(
                    volume_size = 8,
                    encrypted = True,
                    delete_on_termination = True,
                ))
            ]
        )
        
        #This is where the managament server is deployed. 
        instance_managementserver = ec2.Instance(
            self, "Managementserver",
            instance_type= ec2.InstanceType("t2.micro"),
            machine_image= Windows_AMI,
            vpc = vpc_managementserver,
            security_group = SG_managementserver,
            key_name = "project_1_0",
            block_devices = [ec2.BlockDevice(
                device_name = "/dev/sda1",
                volume = ec2.BlockDeviceVolume.ebs(
                    volume_size = 30,
                    encrypted = True,
                    delete_on_termination = True,
                )
            )]
        )

        #This is where the user data for the managementserver is described.
        instance_managementserver.user_data.for_windows()
        instance_managementserver.add_user_data(
            "Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0",
            "Start-Service sshd",
            "Set-Service -Name sshd -StartupType 'Automatic'",
            "New-NetFirewallRule -Name sshd -DisplayName 'Allow SSH' -Enabled True -Direction Inbound -Protocol TCP -Action Allow -LocalPort 22",
        )

        #This is where I set a permission to allow the webserver to read my s3 Bucket.
        Bucket.grant_read(instance_webserver)

        #Only direct SSH connections to the admin server is allowed.
        SG_webserver.connections.allow_from(
            other = instance_managementserver,
            port_range = ec2.Port.tcp(22),
        )

            ###########
        #### AWS Backup #####
            ###########
        
        #This is where I create a Vault.
        vault = backup.BackupVault(
            self, "Webserver_Backup_Vault",
            backup_vault_name = "Webserver_Backup_Vault",
            removal_policy = RemovalPolicy.DESTROY,
        )

        #THis is where I create a Backupplan.
        backup_plan = backup.BackupPlan(
            self, "Daily_Backup",
            backup_vault = vault,
        )

        #This is where I add my webserver to the backupplan.
        backup_plan.add_selection("selection",
            resources = [
                backup.BackupResource.from_ec2_instance(instance_webserver),
            ]
        )
        
        #This is where the the rules are added for the Backupplan. 
        backup_plan.add_rule(backup.BackupPlanRule(
            completion_window = Duration.hours(2),
            start_window = Duration.hours(1),
            schedule_expression = events.Schedule.cron(
                day = "*",
                month = "*",
                hour = "12",
                minute = "0"),
            delete_after = Duration.days(7),    
            )
        )
        



