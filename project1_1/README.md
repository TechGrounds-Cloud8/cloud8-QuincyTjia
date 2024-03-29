# Project version 1.1
This is project 1.1 for the Cloud Engineering cohort of Techgrounds. During the first part of the project I had to make a existing AWS architecture with only using CDK. If I saw some improvements for the architecture, I was allowed to implement them. During the second part of the project, we only got some new requirements and we had to design everything ourselfs. In the directory 'Documents', you can find all the deliverables for this project. There is also the Project itself and the requirements decribed. This README file will contain the necessary information on how to use the application and how to deploy it. 

## Requirements
Before you can start using the app, there are a few requirements which are needed.

- [Install Python and make sure Python is on your PATH](https://cdkworkshop.com/15-prerequisites/600-python.html)
- [AWS CLI](https://docs.aws.amazon.com/cli/v1/userguide/install-windows.html#install-msi-on-windows)
- [AWS Account and User](https://cdkworkshop.com/15-prerequisites/200-account.html)
- [Node.js installed](https://cdkworkshop.com/15-prerequisites/300-nodejs.html)
- [AWS CDK Toolkit installed](https://cdkworkshop.com/15-prerequisites/500-toolkit.html)
- [Setup CDK](https://cdkworkshop.com/30-python/20-create-project.html) 
- [Create or import a certificate and import it in Amazon Certificate Manager](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html)

## Before Use
After the requirements are met, there are a few thing which need to be adjusted before the app can be used.

- Go to your AWS account and generate a keypair and name it project_1_0. When you download you keypair, make sure that you store your keypair somewhere where you can remember it (you need to be in the same directory as the keypair when using the app). 
- In the project1_0_stack.py, go to line 21 and change the value of the IP address to your own Public IP address.  
- After adding the Certificate to the Manager, go to line 619 and replace the ARN of your uploaded certificate.
- After these things are changed, use this command to deploy the app (make sure you are in the same directory as the app) : 
```
cdk deploy
```

## Connecting to the Managementserver
If you only want to connect to the Managementserver, follow these steps:

- Go to the AWS managementconsole and go to ec2 (make sure you are in the right region). Within ec2, go to the instances and select the Managementserver.
- When you are at the right page for the Managementserver, click on connect.
- Choose RDP client and decrypt the password by adding the project_1_0.pem file. 
- Download the RDP launch file and use the decrypted password to login.

## Connecting to the Webserver
If you want to connect to the webserver, you need to do that via the Managementserver. Follow these steps:

- Go to the AWS managementconsole and go to ec2 (make sure you are in the right region). Within ec2, go to the instances and select the Managementserver.
- When you are at the right page for the Managementserver, click on connect.
- Choose RDP client and decrypt the password by adding the project_1_0.pem file. 
- Open a bash terminal and go to the directory where the project_1_0.pem file is located.
- Use the following command:

```
ssh-agent bash
```
- Add the keypair:

```
ssh-add project_1_0.pem
```
- You need to use proxyjump to connect to the webserver via the managementserver:
```
ssh -A -J Administrator@<public IP Managementserver> ec2-user@<private IP webserver>
```
You can find the IP addresses in the AWS managementconsole at the instances.

## Changing website
If you want to change the website, you can go to the assets folder and change the index.html file. Note: This should be changed before you deploy the stack. 

## Edit IP adress of administrator when deployed
If you want to add or edit an administrator IP adress when you are already deployed, you can do that in the console. This is how you can do that:

- When you are in the console, go to the EC2 service and go to the security groups page. There you can edit the inbound rules (chnage trusted IP).
- You also have to change it at the VPC service, the NACL's. You can also edit the inbound rules over there.

## Closing the App
If you want to destroy the app, you need to use the following command:
```
cdk destroy
```
Note: The AWS Backupvault will not be destroyed because it contains the RP's. If you want to destroy it, you have to destroy it manually via the AWS managementconsole. 
