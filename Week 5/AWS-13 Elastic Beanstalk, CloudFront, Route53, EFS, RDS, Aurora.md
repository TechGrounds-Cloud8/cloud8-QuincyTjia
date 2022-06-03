# AWS-13 Elastic Beanstalk, CLoudFront, Route53, EFS, Aurora
With this exercise I had to study and learn a few services and practice how to use it. For EFS and RDS I tried to use it for real. The other services are more theoretical. 

## Key terminology
- AWS Elastic Beanstalk: AWS Elastic Beanstalk is an easy-to-use service for deploying and scaling web applications and services developed with Java, .NET, PHP, Node.js, Python, Ruby, Go, and Docker on familiar servers such as Apache, Nginx, Passenger, and IIS. You can simply upload your code and Elastic Beanstalk automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring. At the same time, you retain full control over the AWS resources powering your application and can access the underlying resources at any time. There is no additional charge for Elastic Beanstalk - you pay only for the AWS resources needed to store and run your applications.

![AWS-13](../00_includes/AWS13-1.png)

- Amazon CloudFront: Amazon CloudFront is a web service that speeds up distribution of your static and dynamic web content, such as .html, .css, .js, and image files, to your users. CloudFront delivers your content through a worldwide network of data centers called edge locations. When a user requests content that you're serving with CloudFront, the request is routed to the edge location that provides the lowest latency (time delay), so that content is delivered with the best possible performance. If the content is already in the edge location with the lowest latency, CloudFront delivers it immediately. If the content is not in that edge location, CloudFront retrieves it from an origin that you've defined—such as an Amazon S3 bucket, a MediaPackage channel, or an HTTP server (for example, a web server) that you have identified as the source for the definitive version of your content. You also get increased reliability and availability because copies of your files (also known as objects) are now held (or cached) in multiple edge locations around the world. 

![AWS-13](../00_includes/AWS13-2.png)

- Content Delivery Network (CDN): A content delivery network (CDN) refers to a geographically distributed group of servers which work together to provide fast delivery of Internet content. A CDN allows for the quick transfer of assets needed for loading Internet content including HTML pages, javascript files, stylesheets, images, and videos. The popularity of CDN services continues to grow, and today the majority of web traffic is served through CDNs, including traffic from major sites like Facebook, Netflix, and Amazon. 

- Route53: Amazon Route 53 is a highly available and scalable cloud Domain Name System (DNS) web service. It is designed to give developers and businesses an extremely reliable and cost effective way to route end users to Internet applications by translating names like www.example.com into the numeric IP addresses like 192.0.2.1 that computers use to connect to each other. Amazon Route 53 is fully compliant with IPv6 as well. Amazon Route 53 effectively connects user requests to infrastructure running in AWS – such as Amazon EC2 instances, Elastic Load Balancing load balancers, or Amazon S3 buckets – and can also be used to route users to infrastructure outside of AWS. You can use Amazon Route 53 to configure DNS health checks, then continuously monitor your applications’ ability to recover from failures and control application recovery with Route 53 Application Recovery Controller. 

- Domain Name System (DNS): The Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources. Each device connected to the Internet has a unique IP address which other machines use to find the device. DNS servers eliminate the need for humans to memorize IP addresses such as 192.168.1.1 (in IPv4), or more complex newer alphanumeric IP addresses such as 2400:cb00:2048:1::c629:d7a2 (in IPv6).

- Amazon Elastic File System (EFS): Amazon Elastic File System (Amazon EFS) provides a simple, serverless, set-and-forget elastic file system for use with AWS Cloud services and on-premises resources. It is built to scale on demand to petabytes without disrupting applications, growing and shrinking automatically as you add and remove files, eliminating the need to provision and manage capacity to accommodate growth. Amazon EFS has a simple web services interface that allows you to create and configure file systems quickly and easily. The service manages all the file storage infrastructure for you, meaning that you can avoid the complexity of deploying, patching, and maintaining complex file system configurations. Its different from S3 and EBS. S3 is object file storage and EFS is a file storage. With object storages you store stuff and retrieve them when you need it. EFS is more for OS or apps that require high I/O. You can create an EFS and mount it to the EC2 intances and then you have a kind of hard disk that is connected to multiple EC2 instances. You only pay for the storage you use.   

![AWS-13](../00_includes/AWS13-3.png)

![AWS-13](../00_includes/AWS13-4.png)

- Network File System (NFSv4) protocol: NFS, or Network File System, was designed in 1984 by Sun Microsystems. This distributed file system protocol allows a user on a client computer to access files over a network in the same way they would access a local storage file. Because it is an open standard, anyone can implement the protocol. NFS started in-system as an experiment but the second version was publicly released after the initial success. To access data stored on another machine (i.e. a server) the server would implement NFS daemon processes to make data available to clients. The server administrator determines what to make available and ensures it can recognize validated clients. From the client's side, the machine requests access to exported data, typically by issuing a mount command. If successful, the client machine can then view and interact with the file systems within the decided parameters. 

- Relational Database Service (RDS): Amazon Relational Database Service (RDS) is a collection of managed web services that makes it simple to set up, operate, and scale databases in the cloud. Choose from seven popular engines — Amazon Aurora with MySQL compatibility, Amazon Aurora with PostgreSQL compatibility, MySQL, MariaDB, PostgreSQL, Oracle, and SQL Server — and deploy on-premises with Amazon RDS on AWS Outposts.

- MySQL: MySQL is a relational database management system (RDBMS) developed by Oracle that is based on structured query language (SQL). A database is a structured collection of data. It may be anything from a simple shopping list to a picture gallery or a place to hold the vast amounts of information in a corporate network. In particular, a relational database is a digital store collecting data and organizing it according to the relational model. In this model, tables consist of rows and columns, and relationships between data elements all follow a strict logical structure. An RDBMS is simply the set of software tools used to actually implement, manage, and query such a database. MySQL is integral to many of the most popular software stacks for building and maintaining everything from customer-facing web applications to powerful, data-driven B2B services. Its open-source nature, stability, and rich feature set, paired with ongoing development and support from Oracle, have meant that internet-critical organizations such as Facebook, Flickr, Twitter, Wikipedia, and YouTube all employ MySQL backends. 

Amazon Aurora: Amazon Aurora (Aurora) is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. Aurora includes a high-performance storage subsystem. Its MySQL- and PostgreSQL-compatible database engines are customized to take advantage of that fast distributed storage. The underlying storage grows automatically as needed. An Aurora cluster volume can grow to a maximum size of 128 tebibytes (TiB). Aurora is part of the managed database service Amazon Relational Database Service (Amazon RDS). Amazon RDS is a web service that makes it easier to set up, operate, and scale a relational database in the cloud.    

## Exercise
Study

- Elastic Beanstalk
- CloudFront
- Route53

Practice

- EFS
- RDS, Aurora 


### Sources
- https://aws.amazon.com/elasticbeanstalk/
- https://youtu.be/uiM1xzOX8Qg
- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html
- https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html
- https://aws.amazon.com/cloudfront/
- https://www.youtube.com/watch?v=AT-nHW3_SVI
- https://www.cloudflare.com/learning/cdn/what-is-a-cdn/
- https://www.cloudflare.com/learning/dns/what-is-dns/
- https://aws.amazon.com/route53/
- https://youtu.be/RGWgfhZByAI
- https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html
- https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html
- https://aws.amazon.com/efs/features/
- https://www.youtube.com/watch?v=6ZIPBC78U0s
- https://www.extrahop.com/resources/protocols/nfs/#:~:text=Network%20File%20System%20(NFS)%20Protocol,-What%20is%20NFS&text=NFS%2C%20or%20Network%20File%20System,access%20a%20local%20storage%20file.
- https://www.youtube.com/watch?v=vAV4ASDnbN0 
- https://docs.aws.amazon.com/efs/latest/ug/gs-step-two-create-efs-resources.html
- https://aws.amazon.com/rds/#:~:text=Amazon%20Relational%20Database%20Service%20(RDS,scale%20databases%20in%20the%20cloud.
- https://www.youtube.com/watch?v=eMzCI7S1P9M
- https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html
- https://www.talend.com/resources/what-is-mysql/
- https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html 
- https://www.youtube.com/watch?v=FzxqIdIZ9wc
- https://www.youtube.com/watch?v=ciRbXZqBl7M 
- https://dev.mysql.com/downloads/workbench/

### Overcome challenges
- I first hard to study the Elastic Beanstalk service
- Then I had to study what CloudFront is and how it works.
- After that I had to study what Route53 is and how it works.
- After that I needed to study what EFS is and do some practice with it. 
- I couldn't log in to my instance, turned out I needed to remove and add the inbound rule (SSH)
- I thought that the efs was mounted automatically but it turned out I had to do it myself. Even when you checked the box to do it automatically. Edit: It turned out it was mounted but 
- After that I had to study RDS and Aurora and do some practice with it. 
- After I made a Database I didn't know how to connect to it, I had to find that out. It turned out I needed a tool, so I donwloaded the MySQL Workbench.

### Results
EFS:

I first made a EFS: 

![AWS-13](../00_includes/AWS13-5.png)

After that I made two EC2 instances. And I used the default SG (SSH and All traffic). 

![AWS-13](../00_includes/AWS13-6.png)

Then I logged in on the first one and mounted the efs. Remember: First make a new directory in de dev map. To know the command to mount the efs, go to your efs dashboard and go to attach. 

![AWS-13](../00_includes/AWS13-7.png)

![AWS-13](../00_includes/AWS13-8.png)

I then made a text file in the efs. After that I went to the other instance and mounted the efs again. After that I went to the efs on the second instance to see if I could see the text file.

![AWS-13](../00_includes/AWS13-9.png)

Setting up a RDS Aurora (Serverless) instance with MySQL compatibility:

I first made a database (I used the youtube tutorial at the sources). It took quite some time to get it started. 

![AWS-13](../00_includes/AWS13-10.png)

To connect to the database I used the MySQL workbench. I found out that I had choosen that the database was only accessible within the VPC (private). I had to change it to public to connect with it via MySQL Workbench. The screenshots below are from my reader instance. Not from my writer instance because it took to long to change to public (modify). 

![AWS-13](../00_includes/AWS13-13.png)

![AWS-13](../00_includes/AWS13-11.png)

![AWS-13](../00_includes/AWS13-12.png)


















    



