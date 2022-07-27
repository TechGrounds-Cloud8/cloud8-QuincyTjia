# Assumptions

In this document I will explain which assumptions I made and why.

## VPC's, region and AZ's

I assumed that the customers are from the same country as mine. Based on this I made some choices for region. 
I choose to deploy my VPC's in the eu-central-1 region because that region is close to my own living place (latency). I could have chosen eu-west-1 which is also quite close by and is cheaper for EC2 usage, but I remained by my decision to use the Frankfurt region because I think latency is important for now.

I have made two AZ's per VPC, but all the instances are deployed in AZ a. I choose for this because in my opinion it isn't necessary to deploy it in two different AZ's. If a AZ would have a downtime, you cannot login or use the webserver. So I choose to deploy everything in one AZ. 

## Instances

The types of instances I used are the one which are the default ones. 

## Encryption

All the data in rest and in transit is encrypted. This is encrypted witht the default key from AWS. 

## Backup

I had to choose a time for the backup to be made. So I choose that a backup will be made everyday at 14:00 CET.
