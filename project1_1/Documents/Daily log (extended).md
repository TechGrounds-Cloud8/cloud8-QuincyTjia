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

23-08: Today I continued with fixing the gateway problem. After some troubleshooting I found out that the problem probably lies wiht the user data for the ASG which doenst launch a webserver. So I spend the whole morning to try to fix it, but I needed some help from Casper. After his help he nodded me in the direction of using a AMI from the working webserver. So now I will try do use it in that way. Another thing I want to try, is to add the user data to the ASG (I didn't using code) and change the order. Those things I will try tommorow. 

24-08: Today I continued with fixing the code. After a collegue tested my code in the evening, she figured out that my user data is fine. She can deploy my code and it worked. So there must be a problem with my PC settings or certificate, because those are the only things I have to change on my own laptop, or the dir of the assets for the S3 bucket.  

25-08: I continued with troubleshooting today and everybody helped. No one seems to find the right solution but we found out that the code also doens't work on the laptop of aurel, so we now know there is a fault in my code. We now have to figure out where it goes wrong.    

26-08: I continue working with troubleshooting the code. Casper is also aware of the problem and is also looking at it right now. Today we are going to disect the code from working v1.0 and making seperate constructs. After that we will add everything from v1.1 to see where it goes wrong. At the end of the day, we split the entire code into smaller constructs, but it still isn't working. We even almost 1 on 1 copied the working code from Killian and it is still not working. Getting really frustrated now. After a loooooooong time of troubleshooting, it turned out the problem WAS the user data. 

29-08: After the weekend I continued with the code. Still couldn't figure out what the problem was. After a while we went to see the systemlogs of the ASG and we saw that there was a weird bug at the user data part. There was a line which said, can't find such file or directory and there stood ^M. We figured out that the user data was corrupt, so we deleted the file and made a new one and after that it worked. It turned out my code was working all the way!!! Very frustrated but also relieved. Now I only have to change some little things to the code, such as change instance types. The code is now completely working. Now I have to do the documentation and the architecture. 