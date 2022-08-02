# List with all requirements
Requirements:

1. Security best practices must be implemented. 
2. There should be a proxy connection between the adminserver and the webserver. (Check!)
3. The webserver should not have a public IP address. (Check!)
4. HTTP connections to the Load Balancer should automatically be upgraded to HTTPS connections.
5. Connections should be secured with a minimum of TLS 1.2 or higher.
6. The webserver should have regularly health checks. 
7. When a health check fails, the webserver should be automatically recovered and restored.
8. When there is to much load on the webserver, there should automatically be new webserver deployed. No more than 3 needs to be deployed.  

Deliverables:

1. A working CDK app from the MVP
2. A design document with the new Architecture
3. A decission document
4. Time Logs
5. End presentation








