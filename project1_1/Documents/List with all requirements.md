# List with all requirements
This document contains a list with a clear point by point description of the requirements for the project. The main goal of this project is to improve and automate an existing architecture. I am responsible for migrating the current servers to the cloud and for automating the deployment of the infrastructure. This have to be done in CDK and you have to make an Infrasctructure as Code (IAC) app. 

Requirements:

1. [All the VM disks must be encrypted.](![REQ1] (../../00_includes/v1_1_encrypted.png)) 
2. The webserver must have a daily backup. The backups have to be kept for 7 days.
3. The webserver must be automatically installed.
4. The admin/management server must be reachable with a public IP.
5. The admin/management server only must be reachable from trusted locations (office/admins's home).
6. The following IP ranges should be used: 10.10.10.0/24 & 10.20.20.0/24.
7. All the subnets have to be protected by a firewall on the subnet level.
8. SSH or RDP connections to the webserver are only allowed from the managementserver.
9. Don't be afraid to propose or make changes to the architecture, but make hard choices, so you can reach the deadline.
10. There is a maximum budget of €150, don't exceed it.

11. Security best practices must be implemented. 
12. There should be a proxy connection between the adminserver and the webserver.
13. The webserver should not have a public IP address. 
14. HTTP connections to the Load Balancer should automatically be upgraded to HTTPS connections. 
15. Connections should be secured with a minimum of TLS 1.2 or higher.
16. The webserver should have regularly health checks.
17. When a health check fails, the webserver should be automatically recovered and restored. 
18. When there is to much load on the webserver, there should automatically be new webserver deployed. No more than 3 needs to be deployed.  

Deliverables:

1. A working CDK app from the MVP
2. A design document with the new Architecture
3. A decission document
4. Time Logs
5. End presentation








