# Assumptions document

In this document I will explain which assumptions I made and why.

# VPC's

I assumed that the customers are from the same country as mine. Based on this I made some choices for region. 
I choose to deploy my VPC's in the eu-central-1 region because that region is close to my own living place (latency). I could have chosen eu-west-1 which is also quite close by and is cheaper for EC2 usage, but I remained by my decision to use the Frankfurt region because I think latency is important for now. 

# NACL's

I assumed that the rules should be the same as the SG rules: Allow inbound HTTP and HTTPS traffic for the webserver and allow inbound SSH connection for the managementserver. 
 