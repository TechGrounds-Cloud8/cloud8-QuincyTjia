# AWS-08 Security Groups
With this exercise I had to study what Security Groups are and what a Network Access Control List is.

## Key terminology
- Security Groups: A security group acts as a virtual (stateful) firewall for your EC2 instances to control incoming and outgoing traffic. Inbound rules control the incoming traffic to your instance, and outbound rules control the outgoing traffic from your instance. When you launch an instance, you can specify one or more security groups. If you don't specify a security group, Amazon EC2 uses the default security group. You can add rules to each security group that allow traffic to or from its associated instances. You can modify the rules for a security group at any time. 
One Security Group can be assigned to multiple instances. The other way around, one instance can have up to 5 Security Groups. Security Groups only have allow rules. Everything not explicitly allowed is automatically implicitly denied.
 
- VPC: Amazon Virtual Private Cloud (Amazon VPC) enables you to launch AWS resources into a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

- Network Access Control List (NACL): A network access control list (ACL) is an optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC. A Network Access Control List (NACL) is a stateless firewall that runs on the subnet level in a VPC.
A NACL has both explicit allow and deny rules. Rules have a number assigned to them. This number indicates the order in which the rules are applied.
By default, a NACL is configured to allow all traffic in and out of the network.

## Exercise
Study

- Security Groups in AWS

- Network Access Control Lists in AWS

### Sources
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html
- https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html
- https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html  

### Overcome challenges  
- I didn't had any challenges to overcome, it was just searching for the right information.

### Results
I had to study the key terminology.







