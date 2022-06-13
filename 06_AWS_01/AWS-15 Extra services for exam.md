# AWS-15 Extra services for exam 
This is a overview of the services which are in the exam but which we didn't learn during the course. 

## Key terminology

General terminology

- Cost Explorer: AWS Cost Explorer has an easy-to-use interface that lets you visualize, understand, and manage your AWS costs and usage over time.

- Infrastructure as Code (IaC): Infrastructure as code (IaC) means to manage your IT infrastructure using configuration files.

- AWS service quotas: Service Quotas is an AWS service that helps you manage your quotas for many AWS services, from one location. Along with looking up the quota values, you can also request a quota increase from the Service Quotas console.

- AWS CLoud Development Kit (AWS CDK): The AWS Cloud Development Kit (AWS CDK) is an open-source software development framework to define your cloud application resources using familiar programming languages. 

- AWS Software development kits (SDKs): SDKs take the complexity out of coding by providing language-specific APIs for AWS services.

- Consolidated billing feature: You can use the consolidated billing feature in AWS Organizations to consolidate billing and payment for multiple AWS accounts or multiple Amazon Internet Services Pvt. Ltd (AISPL) accounts. Every organization in AWS Organizations has a management account that pays the charges of all the member accounts. Consolidated billing has the following benefits:

    - One bill – You get one bill for multiple accounts.

    - Easy tracking – You can track the charges across multiple accounts and download the combined cost and usage data.

    - Combined usage – You can combine the usage across all accounts in the organization to share the volume pricing discounts, Reserved Instance discounts, and Savings Plans. This can result in a lower charge for your project, department, or company than with individual standalone accounts. For more information, see Volume discounts.

    - No extra fee – Consolidated billing is offered at no additional cost. 

Analytics

- Amazon Athena: Amazon Athena is an interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.

- Amazon Kinesis: Amazon Kinesis makes it easy to collect, process, and analyze real-time, streaming data so you can get timely insights and react quickly to new information. Amazon Kinesis offers key capabilities to cost-effectively process streaming data at any scale, along with the flexibility to choose the tools that best suit the requirements of your application. 

- Amazon QuickSight: Amazon QuickSight allows everyone in your organization to understand your data by asking questions in natural language, exploring through interactive dashboards, or automatically looking for patterns and outliers powered by machine learning.

Compute and Serverless

- AWS Batch: AWS Batch enables developers, scientists, and engineers to easily and efficiently run hundreds of thousands of batch computing jobs on AWS. AWS Batch dynamically provisions the optimal quantity and type of compute resources (e.g., CPU or memory optimized instances) based on the volume and specific resource requirements of the batch jobs submitted. With AWS Batch, there is no need to install and manage batch computing software or server clusters that you use to run your jobs, allowing you to focus on analyzing results and solving problems. 

- Batch jobs: In the simplest terms, a batch job is a scheduled program that is assigned to run on a computer without further user interaction. Batch jobs are often queued up during working hours, then executed during the evening or weekend when the computer is idle. Once the batch job is submitted, the job enters into a queue where it waits until the system is ready to process the job. If the job queue contains many jobs waiting to be processed, the system processes the jobs either in chronological order or by priority.  

- Amazon Lightsail: Amazon Lightsail offers easy-to-use virtual private server (VPS) instances, containers, storage, databases, and more at a cost-effective monthly price.

- Amazon Workspaces: Amazon WorkSpaces is a fully managed desktop virtualization service for Windows and Linux that enables you to access resources from any supported device.

Containers

- AWS Fargate: AWS Fargate is a serverless, pay-as-you-go compute engine that lets you focus on building applications without managing servers. AWS Fargate is compatible with both Amazon Elastic Container Service (ECS) and Amazon Elastic Kubernetes Service (EKS). AWS Fargate is a technology that provides on-demand, right-sized compute capacity for containers. 

- Amazon Elastic Kubernetes Service (EKS): Amazon Elastic Kubernetes Service (Amazon EKS) is a managed container service to run and scale Kubernetes applications in the cloud or on-premises. 

Database

- Amazon ElastiCache: Amazon ElastiCache is a fully managed, in-memory caching service supporting flexible, real-time use cases. You can use ElastiCache for caching, which accelerates application and database performance, or as a primary data store for use cases that don't require durability like session stores, gaming leaderboards, streaming, and analytics. ElastiCache is compatible with Redis and Memcached.  

- Amazon Redshift: Amazon Redshift uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes, using AWS-designed hardware and machine learning to deliver the best price performance at any scale.

Developer Tools

- AWS Codebuild: AWS CodeBuild is a fully managed continuous integration service that compiles source code, runs tests, and produces software packages that are ready to deploy. With CodeBuild, you don’t need to provision, manage, and scale your own build servers. CodeBuild scales continuously and processes multiple builds concurrently, so your builds are not left waiting in a queue. 

- AWS CodeCommit: AWS CodeCommit is a secure, highly scalable, managed source control service that hosts private Git repositories. It makes it easy for teams to securely collaborate on code with contributions encrypted in transit and at rest. CodeCommit eliminates the need for you to manage your own source control system or worry about scaling its infrastructure.

- AWS CodeDeploy: AWS CodeDeploy is a fully managed deployment service that automates software deployments to a variety of compute services such as Amazon EC2, AWS Fargate, AWS Lambda, and your on-premises servers. 

- AWS CodePipeline: AWS CodePipeline is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define.  

- AWS CodeStar: AWS CodeStar enables you to quickly develop, build, and deploy applications on AWS. AWS CodeStar provides a unified user interface, enabling you to easily manage your software development activities in one place. With AWS CodeStar, you can set up your entire continuous delivery toolchain in minutes, allowing you to start releasing code faster.  

Customer Engagement

- Amazon Connect: With Amazon Connect, you can set up a contact center in minutes that can scale to support millions of customers.

Management, Monitoring and Governance

- AWS Budgets: AWS Budgets allows you to set custom budgets to track your cost and usage from the simplest to the most complex use cases. With AWS Budgets, you can choose to be alerted by email or SNS notification when actual or forecasted cost and usage exceed your budget threshold, or when your actual RI and Savings Plans' utilization or coverage drops below your desired threshold. 

- AWS CloudFormation: AWS CloudFormation lets you model, provision, and manage AWS and third-party resources by treating infrastructure as code.

- AWS Organizations: AWS Organizations is an account management service that lets you consolidate multiple AWS accounts into an organization that you create and centrally manage. With Organizations, you can create member accounts and invite existing accounts to join your organization. You can organize those accounts into groups and attach policy-based controls. Using AWS Organizations, you can programmatically create new AWS accounts and allocate resources, group accounts to organize your workflows, apply policies to accounts or groups for governance, and simplify billing by using a single payment method for all of your accounts. 

- AWS Secrets Manager: AWS Secrets Manager helps you protect secrets needed to access your applications, services, and IT resources. The service enables you to easily rotate, manage, and retrieve database credentials, API keys, and other secrets throughout their lifecycle.

- AWS Systems Manager: Systems Manager helps you safely manage and operate your resources at scale.

- AWS Systems Manager Parameter Store: Parameter Store, a capability of AWS Systems Manager, provides secure, hierarchical storage for configuration data management and secrets management. You can store data such as passwords, database strings, Amazon Machine Image (AMI) IDs, and license codes as parameter values. 

Networking and Content Delivery

- AWS Direct Connect: The AWS Direct Connect cloud service is the shortest path to your AWS resources. While in transit, your network traffic remains on the AWS global network and never touches the public internet. This reduces the chance of hitting bottlenecks or unexpected increases in latency. When creating a new connection, you can choose a hosted connection provided by an AWS Direct Connect Delivery Partner, or choose a dedicated connection from AWS—and deploy at over 100 AWS Direct Connect locations around the globe. 

Security, Identity and Compliance

- AWS Artifact: AWS Artifact is your go-to, central resource for compliance-related information that matters to you. It provides on-demand access to AWS’ security and compliance reports and select online agreements. Reports available in AWS Artifact include our Service Organization Control (SOC) reports, Payment Card Industry (PCI) reports, and certifications from accreditation bodies across geographies and compliance verticals that validate the implementation and operating effectiveness of AWS security controls.

- AWS Certificate Manager (ACM): AWS Certificate Manager is a service that lets you easily provision, manage, and deploy public and private Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates for use with AWS services and your internal connected resources.

- AWS CloudHSM: AWS CloudHSM is a cloud-based hardware security module (HSM) that enables you to easily generate and use your own encryption keys on the AWS Cloud. 

- Amazon Cognito: Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily.

- Amazon Detective: Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities.

- Amazon GuardDuty: Amazon GuardDuty is a threat detection service that continuously monitors your AWS accounts and workloads for malicious activity and delivers detailed security findings for visibility and remediation.

- Amazon Inspector: Amazon Inspector is an automated vulnerability management service that continually scans AWS workloads for software vulnerabilities and unintended network exposure.

- Amazon Macie: Amazon Macie is an AI that is used to detect and secure sensitive data in your AWS environment. 

- AWS Shield: AWS Shield is a managed Distributed Denial of Service (DDoS) protection service that safeguards applications running on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency, so there is no need to engage AWS Support to benefit from DDoS protection. 

- AWS WAF: AWS WAF is a web application firewall that helps protect your web applications or APIs against common web exploits and bots that may affect availability, compromise security, or consume excessive resources.

Storage

- AWS Backup: Use AWS Backup to centralize and automate data protection across AWS services and hybrid workloads. AWS Backup offers a cost-effective, fully managed, policy-based service that further simplifies data protection at scale.

- AWS Snowball Edge: Accelerate moving offline data or remote storage to the cloud. Easily migrate terabytes of data to the cloud without limits in storage capacity or compute power. Protect your data in transit with Snowball’s ruggedized chassis, integrated logistics, and tamper-evident box, and get data to the right place quickly.  

- AWS Storage Gateway: AWS Storage Gateway is a set of hybrid cloud storage services that provide on-premises access to virtually unlimited cloud storage. 

## Exercise

### Sources
- https://aws.amazon.com/aws-cost-management/aws-cost-explorer/#:~:text=AWS%20Cost%20Explorer%20has%20an,analyze%20cost%20and%20usage%20data.
- https://stackify.com/what-is-infrastructure-as-code-how-it-works-best-practices-tutorials/
- https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html
- https://aws.amazon.com/tools/
- https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc
- https://aws.amazon.com/kinesis/
- https://aws.amazon.com/quicksight/
- https://aws.amazon.com/lightsail/
- https://aws.amazon.com/workspaces/
- https://aws.amazon.com/eks/
- https://aws.amazon.com/elasticache/
- https://aws.amazon.com/redshift/
- https://aws.amazon.com/codebuild/
- https://aws.amazon.com/codecommit/
- https://aws.amazon.com/codedeploy/
- https://aws.amazon.com/codepipeline/
- https://aws.amazon.com/codestar/
- https://aws.amazon.com/connect/
- https://aws.amazon.com/aws-cost-management/aws-budgets/
- https://aws.amazon.com/secrets-manager/
- https://aws.amazon.com/systems-manager/
- https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html
- https://aws.amazon.com/directconnect/
- https://aws.amazon.com/artifact/
- https://aws.amazon.com/certificate-manager/
- https://aws.amazon.com/cloudhsm/
- https://aws.amazon.com/cognito/
- https://aws.amazon.com/detective/
- https://aws.amazon.com/guardduty/
- https://aws.amazon.com/inspector/
- https://aws.amazon.com/macie/
- https://aws.amazon.com/shield/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc
- https://aws.amazon.com/waf/
- https://aws.amazon.com/backup/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc
- https://aws.amazon.com/snowball/
- https://aws.amazon.com/storagegateway/
- https://aws.amazon.com/batch/
- https://www.bmc.com/blogs/batch-jobs/
- https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/consolidated-billing.html
- https://aws.amazon.com/organizations/
- https://docs.aws.amazon.com/controltower/latest/userguide/organizations.html
- https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html
- https://docs.aws.amazon.com/eks/latest/userguide/fargate.html
- https://aws.amazon.com/fargate/
- https://aws.amazon.com/cdk/
- https://aws.amazon.com/cloudformation/

### Overcome challenges
- 

### Results
 -



