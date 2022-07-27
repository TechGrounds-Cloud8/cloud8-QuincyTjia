# Daily log (extended)

During this project I have to make some choices which are not described in the project document. I will describe the decissions I made in this document and why I made them. This document is also where I will describe all the work I did for the project per subject.

# VPC's

06-07-2022: The first step I had to do is to add a IAM user (myself) which have Administrator access. This is a best practice to do. After that I had to login with the right credentials to the CLI. When I had done that the first step was to create a new cdk project. When I finished that I was good to go to actually start with the project.  

The first step in making the architecture from the project is to make a VPC in which we can deploy resources. So I had to find out how to do this. I choose to deploy my first VPC in the eu-central-1 region because that region is close to my own living place (latency). The architecture uses 2 public subnets. When I deployed mine VPC I thought I had created 2 subnets but it turned out they where 4 created. I had to search why this happened.

07-07-2022: I managed to make the code right and to deploy a VPC with two subnets in two AZ's. It turned out I had a extra line of code where I said to deploy two subnets per AZ instead of 1. 

The next step is to make a second VPC with another IP range but with the same design: 2 public subnets in two different AZ's. I deployed the VPC in the same region (eu-central-1). 

The next thing to do is to make sure the two VPC's have VPC peering enabled. 

08-07-2022: I started working on the VPC peering, I had to figure out how to enable this. So I began with researching. After a while I found a working code for enabling the peering connection. There was only one problem, when destroying your stack and deploying it again it gave an error because everytime you deploy a new stack, the VPC's will get a different ID. So now I had to find a solution on how to fix this problem. After a long time of searching I got help from Ben. It turned out I had to use object programming to make it work. 

# EC2

The next step to take is to deploy an EC2 webserver in VPC 1, so I had to figure out how to do it. I managed after some research how to deploy an EC2 instance with an AMI. The next step is to tweak it a little bit better with the right AMI (type etc. for this project). For now I will deploy the webserver and management server in the same AZ. 

12-07-2022: The next step to do is to add a user data script, so that on deployment the webserver will be automatically installed. I had to figure out how to add that. It took me quite a long time to make the right code for it. It turned out I still didn't quite know how OOP worked.

# Security Groups

The next step to do is to make the security groups for the webserver VPC. That went quite well and was done quickly. The next step to do is to make a second security group for the management server.

13-07-2022: I have to make a SG for the management server. This SG has to have a rule which add a inbound rule to allow a SSH conncection from a trusted IP address. This went very quickly because I already had the code and only needed to change some settings. 

The next step to do is to make a NACL for the Subnets in the Webserver VPC. It should have the Ingress and Egress HTTP and HTTPS traffic allowed. I also have to add a ACL for the managementserver. It should have at least for now have a Ingress and Egress SSH traffic allowed. I finished the code and the ACL's where added, however I couldn't access my webserver. So I had to find a solution to get access to it again (Ephemeral port). After a while I managed to fix the problem and now I can access my webserver again.   

# S3

14-07-2022: The next step to do is to make a storage solution where I can store bootstrap/post-deployment scripts. I choose to make a S3 bucket where I can store the scripts (user data). So I had to find out how to create a S3 bucket first. It was pretty easy to create a basic bucket, now I need to place my userdata in the bucket instead of hardcoded in my code. When the webserver will start it will need to read the userdata, but this userdata will be stored in the S3 bucjet. I will need to find out how to make this work. I had to make a new directory which I called assets. In that dir can I place the userdata script. After a while of researching I managed to write the code to put a object (userdata) in the S3 Bucket. The next step to do is to make sure that the webserver can access the userdata which is stored in the S3 Bucket. I managed to make a code which used the .sh file from my bucket to use as userdata. When I want to access the webserver it say access denied, so I have to figure out why (Permissions?). 

When I deleted my stack the S3 bucket wasn't deleted, so I had to add a few extra lines of code to make sure the S3 bucket is automatically deleted when the stack is destroyed. 

15-07-2022: I had to fix the issue why I cannot access my webserver, so I began by fixing that. I think it has to do with permissions, so I will search in that direction. I tried to make the bucket public and after that I could access the website. So it defenitely has to do with permissions. I had to make a IAM role that grants access to the S3 bucket.

18-07-2022: A new sprint! Before I get started with this sprint I had to make a clear overview of the tasks I had to do for this print. So I began the day by making a planning and by making tasks in jiira. After I had done that I went further with the project. I still had to make a IAM role that grants access to the S3 bucket, so I continued working on that. After a lot of searching and trying things out, it turned out I had to change the permissions of the s3 bucket. I allowed the webserver to read  the s3 bucket and it worked after that. 

# SSH and Managementserver

The next step I was going to take is to make sure the SSH connection will work when you try to login on the managementserver. I already made the SG which allows SSH connections and the NACL for the managementserver. The first step is to make sure a key-pair exist or is generated, otherwise you cant login with SSH. I created a key-pair via the management console for now. After that I tried to connect to the Admin server via SSH. I couldn't connect to it because it said a port 22 connection time out. I had to look a bit better at my SG's. It turned out I had to change the outbound SSH rule for the NACL of the managementserver. I had to change the port range to the same range as the ephemeral traffic instead of only using port 22. I can now access my managementserver via SSH connection. A requirement is that the management server can only be reached from a trusted IP adress (my home), so I have to make sure that it is only reachable via my IP adress. I had to modify some SG's.

19-07-2022: I continued working on making sure the that the admin server is only reachable (via SSH) from my own IP address. After some tries I figured out it had to do with my IP address in the code. After some adjustments, the admin server is only rechable from my home IP.

# Routingtable

20-07-2022: The next step to take is make sure I can reach my webserver via the admin server. I already make sure there is a peering connection between the VPC's, but now I have to change the routing tables in order to make a right connection. So I have to figure out how to make this work. When I had a bit of code and tried do deploy it, I got the error: Already a Construct with name ..... in stack. After a lot of googling and some help from a teammate I found out I have to use a f string for the routetable ID. Because now it will take the same ID for all the subnets within a VPC, so thats where the error comes from. So I have to learn what f strings are and how to use them. After I googled a bit I  came across tokens on the aws documentation. After I made some changes to my code, I could deploy it. Now I have to test if it actually works. To be able to test it, I need to SSH to my managementserver and within the server SSH to the webserver. But to do that, I need to find a solution on how to get the key-pair from my managementserver to the webserver. I found something called SSH agent forwarding. This is a secure way to keep a decrypted key in memory. When trying to connect it works, so the routing tables work! I find out that I can also make a SSH connection directly to the webserver, this isn't allowed as a requirement, so I have to change some SG or NACL's later on.   

# AWS Backup

21-07-2022: The next step to take, is to make sure that the webserver will have a daily backup which will be kept for 7 days. I will use the AWS backup service for this, so I have to figure out how this works and how to write the right code for it. After some time I managed to write the code for it. I only have to wait right now to check if a actually backup will be created at 2 pm everyday. After that I need to make sure that the right permissions are in effect to be able to get by the backups. 

# Encryption

Another requirement is that the VM disks must be encrypted and that alle data in rest or in transit should be encrypted. So the next thing to do is to search for a solution for that. When I think about data at rest, all the data in the S3 bucket should be encrypted and all the data on the VM disks and all the data in the BackupVault. I already encrypted the data in the S3 bucket and now I will encrypt the VM disks (volumes). 

I managed to encrypt the webserver volume. Now I need to encrypt the backupvault. After encrypting the backupVault, I will first make a windows adminserver before encrypting the disk for the admin server.   

22-07-2022: After some extra research I actually found out that the backups from VM's are always encrypted in the Vault. So I don't have to do that anymore. 

 # Index HTML

The Product owners said that the default apache website should be replaced, so I had to figure out how to do that. The first step was to make simple html file. After that I had to make sure the script is uploaded in the S3 bucket when the stack is deployed. After some more research I managed to make sure a new html file is add during the deployment. Within this file, users of the program can add html code to configure the website. 

# Windows server and RDP

25-07-2022: The next step to take, is to make a Windows management server instead of a Linux server. This is a new requirement from the product owners, so it has to be included in version 1.0. I have to find out which is the correct AMI for this server (cost etc.) After I changed the Linux server to a windows server, I had to make sure RDP connections are allowed to the windows server. So I had to look up how RDP works. After that I had to make sure that the SG's are updated so that RDP is allowed from my home IP. After that I tried to connect to the windows machine via RDP and it worked. So the next step to take, is to make sure that within the Managementserver, you can SSH to the Webserver. I have to look in the direction of Authentication forwarding. I need to make sure I can use the same key(pair) within my windows machine to ssh to the linux machine. With some help from a teammate I found out I needed to install a ssh windows server on the adminserver. After that I can ssh to my webserver. When I tried installing the openssh server, I got an error. When I googled the error I found out it was because there was no internet connection. So I have to add some SG's permissions and add some NACL's rules. After that I was able to connect to the internet. After that I made sure the open ssh was installed correctly. When that was done, I needed to find a way on how to login with the keypair. After a tip I searched in the direction of proxyjump. It turned out that it worked and I am able to connect to the admin server and to the webserver via my own PC. 

# Last bits

26-07-2022: The application is working and running but there are a few things I still have to do to meet all the requirements. All the VM's disks should be encrypted, so I started with encrypting the admin server. After I had done that I started on making sure you can only SSH to the admin server directly, but not directly to the webserver. After that I added some user data to the managementserver so it is easier to login each time.  


