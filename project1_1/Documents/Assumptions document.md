# Assumptions

In this document I will explain which assumptions I made and why.

## VPC's, region and AZ's

I assumed that the customers are from the same country as mine. Based on this I made some choices for region. 
I choose to deploy my VPC's in the eu-central-1 region because that region is close to my own living place (latency). I could have chosen eu-west-1 which is also quite close by and is cheaper for EC2 usage, but I remained by my decision to use the Frankfurt region because I think latency is important for now.

The webserver is deployed in AZ-a, and the ASG is deployed in AZ-a but could also be deployed in b and c when there is a high load. The managmenet sever is deployed in AZ-a.

## Instances

The types of instances I used are the t3.nano.

## Encryption

All the data in rest and in transit is encrypted. This is encrypted witht the default key from AWS. 

## Backup

I had to choose a time for the backup to be made. So I choose that a backup will be made everyday at 14:00 CET.