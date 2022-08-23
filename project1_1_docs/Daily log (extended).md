# Daily log (extended)

01-08-2022: Today I started with version 1.1 of the project. Before I actually started with coding, I had to make sure that I completely understood the new requirements etc. So I started the day by putting everything in Jiira and making user stories. After that I made a document with all the new requirements. Then I was ready to start coding.

## VPC's

The first step I wanted to do, is to make sure that the webserver is deployed in a Private Subnet instead of in a Public subnet. So I had to adjust the current webserver VPC, so that there will be a Public subnet and a Private subnet. To make a private subnet in a VPC, you have to make sure its a subnet with no internet gateway attached. So after I had done that, I wanted to deploy the webserver in the private subnet. After I deployed it, there is no public IP address connected to the webserver instance. So I will deploy the whole stack, to see if I can still login via the adminserver. After deploying the whole stack, I cannot connect to the webserver again via the adminserver, so tommorrow I will have to look at the routingtables again. 

## Auto-scaling group

02-08-2022: I decided to go further with the autoscaling groups, because after adding a Load Balancer, you probably have to change the routingtables again otherwise. So the first step was to see how to actually program auto scaling groups. After some time I figured out how to do it. Before I made a autoscaling group, I made a launchtemplate. The next step to do, is to add an application load balancer.

## Application Load Balancer

03-08-2022: So today I will start working on the Application Load Balancer. So the first step is to find out how to program this part. After having found the rigth code, I had to find a way to add the right certificates. 

04-08: I started this day with a lot of troubleshooting, my code wasn't working good, so I had to make some changes. After is worked again I started to add the ssl certificate. I am going to use a self-signed certificate because I already know how to make one and how to use it. After making one, I saw that a certificate is being used for the Load Balancer, so this part is working.  

22-08: After the holiday I started working on the project again. I had so see where I ended the last time, this was with the working ssl certificate. But when I tried to connect to the ALB, there is a bad gateway error. So I have to fix this. The first step I took was to add a new routingtable for the private subnets. After that I had to figure out how to fix the bad gateway error. First I started with making sure the instances are deployed in the right subnets. So I added some lines of code to make sure they are deployed the right way. After that I updated the NACL's and SG's. I had to make a new SG for the private subnets. After I did all of that, I still had a bad gateway error, so the problem lies somewhere else. 

23-08: Today I continued with fixing the gateway problem. After some troubleshooting I found out that the problem lies wiht the user data for the ASG which doenst launch a webserver. So I spend the whole morning to try to fix it, but I needed some help from Casper. After his help he nodded me in the direction of using a AMI from the working webserver. So now I will try do use it in that way. Another thing I want to try, is to add the user data to the ASG (I didn't using code) and change the order. Those things I will try tommorow.   