# SEC-08 Detection, response and analysis
With this exercise I learned what can be done to prevent malware attacks. I also learned what you (as a company) can do to fix breaches or attacks from malware. 

## Key terminology
- Detection phase: In this phase you detecting a attempted attack. Detecting an (attempted) attack is the first step to stopping an attack and to preventing future attempts. Tools like Wireshark can help analyse a network to detect anomalies. Intrusion detection systems (IDS) and intrusion prevention systems (IPS) are also used for this purpose.
- Response phase: In this phase you respnse to the dtected attack. The first thing to do in response to a detected attack is trying to contain the damage. Depending on the kind of attack, the way you do this might differ. After the attack is contained, you can try to figure out the root cause of the attack, so that you can stop it.   
- Analysis phase: In this phase you analyse what has happened and you document what you learned and do the necessary thing to prevent this from rehappening.  
- Malicious software (malware): Malware, short for “malicious software,” refers to any intrusive software developed by cybercriminals (often called “hackers”) to steal data and damage or destroy computers and computer systems. Examples of common malware include viruses, worms, Trojan viruses, spyware, adware, and ransomware. Recent malware attacks have exfiltrated data in mass amounts.  
- Social Engineering: Social engineering is a manipulation technique that exploits human error to gain private information, access, or valuables. In cybercrime, these “human hacking” scams tend to lure unsuspecting users into exposing data, spreading malware infections, or giving access to restricted systems. Attacks can happen online, in-person, and via other interactions.
- Intrusion detection systems (IDS): An Intrusion Detection System (IDS) is a monitoring system that detects suspicious activities and generates alerts when they are detected. Based upon these alerts, a security operations center (SOC) analyst or incident responder can investigate the issue and take the appropriate actions to remediate the threat.
- Intrusion prevention systems (IPS): An intrusion prevention system (IPS) is a network security tool (which can be a hardware device or software) that continuously monitors a network for malicious activity and takes action to prevent it, including reporting, blocking, or dropping it, when it does occur. It is more advanced than an intrusion detection system (IDS), which simply detects malicious activity but cannot take action against it beyond alerting an administrator   
- Disaster recovery plan: Disaster recovery plans (DRP) seek to quickly redirect available resources into restoring data and information systems following a disaster. A disaster can be classified as a sudden event, including an accident or natural disaster, that creates wide scoping, detrimental damage. Response and analysis are part of the disaster plan. 
- Recovery Point Objective (RPO): Recovery Point Objective (RPO) generally refers to the amount of data that can be lost within a period most relevant to a business, before significant harm occurs, from the point of a critical event to the most preceding backup.
- Recovery Time Objective (RTO): Recovery Time Objective (RTO) often refers to the quantity of time that an application, system and/or process, can be down for without causing significant damage to the business as well as the time spent restoring the application and its data.
- System hardening: Systems hardening is a collection of tools, techniques, and best practices to reduce vulnerability in technology applications, systems, infrastructure, firmware, and other areas. The goal of systems hardening is to reduce security risk by eliminating potential attack vectors and condensing the system’s attack surface. By removing superfluous programs, accounts functions, applications, ports, permissions, access, etc. attackers and malware have fewer opportunities to gain a foothold within your IT ecosystem. 

## Exercise
- A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?
- An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?

### Sources
- https://www.cisco.com/c/en/us/products/security/advanced-malware-protection/what-is-malware.html
- https://www.kaspersky.com/resource-center/definitions/what-is-social-engineering 
- https://www.checkpoint.com/cyber-hub/network-security/what-is-an-intrusion-detection-system-ids/#
- https://www.vmware.com/topics/glossary/content/intrusion-prevention-system.html#:~:text=An%20intrusion%20prevention%20system%20(IPS,it%2C%20when%20it%20does%20occur. 
- https://www.cisecurity.org/insights/spotlight/cybersecurity-spotlight-disaster-recovery-plan-drp#:~:text=Disaster%20recovery%20plans%20(DRP)%20seek,creates%20wide%20scoping%2C%20detrimental%20damage. 
- https://www.acronis.com/en-us/blog/posts/rto-rpo/ 
- https://securityboulevard.com/2019/11/5-tips-for-responding-to-cyber-attacks/ 
- https://www.beyondtrust.com/resources/glossary/systems-hardening
- https://sados.com/blog/types-of-disaster-recovery-plans/ 

### Overcome challenges
- I first had to study what all the different key terminilogy means.

### Results
- Hack response strategies:

    - Recovering from a hacking attack can be expensive, complicated, and time-consuming. With that in mind, it’s smart for companies to prepare on the front end, rather than merely responding once the attack happens. Here are 5 tips to respond to hacking attacks:

    1. Follow a communication plan
    2. Secure IT Systems
    3. Launch backups
    4. Notify authorities
    5. Create redundancy in your data

- Different types of disaster recovery options:

    1. Data Center Disaster Recovery Plans: A Data Center DR plan focuses on the entire building where a business houses its servers. It’s more comprehensive than simply protecting computers. Physical security, support employees, backup power sources, HVAC, internet and electric providers, and fire prevention and suppression plans all impact a data center DR plan. 

    2. Data Back-up Disaster Recovery Plans: Some businesses do not have the resources or want to drastically cut costs, so they choose the most basic disaster recovery plan—data back-up. This DR plan typically includes companies backing up their data with a cloud provider. Instead of investing money in their own data center, businesses utilize their cloud provider’s data center. 

    3. Virtual Disaster Recovery Plans: A virtual disaster recovery plan is another budget-friendly DR option, but it provides more functional recovery than simply backing up data. If you choose a virtual DR plan, your managed service provider (MSP) replicates your entire computing environment, including your server(s), storage, operating system(s), software, apps, and data. These replicas, referred to as ‘virtual machines’ can run anywhere without configuration.   

    There are more types, you can check te link I used for this. 

- A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?

    - They lose a maximum of 1 day of data. This is because the company makes daily backups, so in the case of a failure they have all the data of the previous day. 

- An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?

    - The website has a downtime around 8 minutes. So your RTO is around 8 minutes.
