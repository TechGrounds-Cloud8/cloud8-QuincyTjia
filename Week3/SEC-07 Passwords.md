# SEC-07 Passwords

## Key terminology
- Password managers: A password manager is an advanced tool that helps individuals and businesses securely store and manage all of their login credentials. This tool is commonly used to generate strong, unique passwords for web applications. Once generated, they are put in a centralized vault, and encrypted with one master password. Users only need to remember one password to access their services. 
- Hashing: Hasing is the process of converting a input of any given length into a fixed size string of text using a mathemetical function. 
- Rainbow Table: A rainbow table is a precomputed compilation of plaintexts and matching ciphertexts (typically passwords and their matching hashes). Rainbow tables greatly speed up many types of password cracking attacks, often taking minutes to crack where other methods (such as dictionary, hybrid, and brute-force password cracking attempts) may take much longer.
- Salting:
 
## Exercise
- Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.
- Find out how a Rainbow Table can be used to crack hashed passwords.
- Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.
03F6D7D1D9AAE7160C05F71CE485AD31
03D086C9B98F90D628F2D1BD84CFA6CA
- Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.
- Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted. To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.

### Sources
- https://www.techopedia.com/definition/14316/hashing-cybersecurity
- https://www.youtube.com/watch?v=2BldESGZKB8 
- https://www.encryptionconsulting.com/education-center/encryption-vs-hashing/#:~:text=Since%20encryption%20is%20two%2Dway,salt%2C%20that%20cannot%20be%20decrypted. 
- https://www.zoho.com/vault/educational-content/what-is-a-password-manager.html#:~:text=A%20password%20manager%20is%20an,encrypted%20with%20one%20master%20password.
- https://www.sciencedirect.com/topics/computer-science/rainbow-table
- 

### Overcome challenges
- First I had to find out what the key terminology mean.
- After that I had to find out why hashing is preffered to store passwords instead of encryption.
- After that I had to find out what a rainbow table is and how it can be used to crack a hashed password.
- 

### Results
- Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.

    - Hasing is the process of converting a input of any given length into a fixed size string of text using a mathemetical function. 

    - Encryption is a two-way function where data is passed in as plaintext and comes out as ciphertext, which is unreadable. Since encryption is two-way, the data can be decrypted so it is readable again. Hashing, on the other hand, is one-way, meaning the plaintext is scrambled into a unique digest, that cannot be decrypted. Hashing is preffered over encryption for passwords because it is irreversible. With encryption you can decrypt the message again and then you can see the plain text. 

 - Find out how a Rainbow Table can be used to crack hashed passwords.

    

The differnces between Encrypting and Hashing

![SEC-07](../00_includes/SEC07-1.png)