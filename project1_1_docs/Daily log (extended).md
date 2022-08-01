#Daily log (extended)

01-08-2022: Today I started with version 1.1 of the project. Before I actually started with coding, I had to make sure that I completely understood the new requirements etc. So I started the day by putting everything in Jiira and making user stories. After that I made a document with all the new requirements. Then I was ready to start coding.

##VPC's

The first step I wanted to do, is to make sure that the webserver is deployed in a Private Subnet instead of in a Public subnet. So I had to adjust the current webserver VPC, so that there will be a Public subnet and a Private subnet. To make a private subnet in a VPC, you have to make sure its a subnet with no internet gateway attached. Also make sure you deploy a NAT gate in the public subnet. So after I had done that, I wanted to deploy the webserver in the private subnet. After I deployed it, there is no public IP address connected to the webserver instance. So I will deploy the whole stack, to see if I can still login via the adminserver. After deploying the whole stack, I cannot connect to the webserver again via the adminserver, so tommorrow I will have to look at the routingtables again. 