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








