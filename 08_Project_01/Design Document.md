# Design document

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



