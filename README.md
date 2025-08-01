# File Integrity Checker

A Python-based CLI tool that verifies the integrity of log files to detect any unauthorized modifications or tampering.

This project was developed as part of a cybersecurity hands-on evaluation.

# Features: 
• Accepts a directory or single log file as input 

• Uses SHA-256 cryptographic hashing 

• Stores hashes for first-time initialization 

• Detects file tampering by comparing stored and current hashes 

• Allows manual hash updates after legitimate changes 

• Simple command-line usage  

# Project Structure:
file-integrity-checker/

├── integrity_check.py (Main script)

├── file_hashes.json (Stored hashes)

├── README.md (Documentation)

└── logs/

└── app.log (Sample log file)

# Usage: 
1. Initialize Hashes
   
        Command: python integrity_check.py init logs
    
        Description: Stores hashes for all files in the logs/ directory. 

2. Check File Integrity
   
        Command: python integrity_check.py check logs
   
        Description: Verifies if any file was modified or tampered with.

3. Update Hash (after legitimate changes)
   
       Command: python integrity_check.py update logs/app.log
   
       Description: Updates hash for a specific file. 

# Output: 

    python integrity_check.py init logs
  ![has](https://github.com/user-attachments/assets/d2c4a2ce-7da5-498d-9e36-13e27df86b14)


 
Hashes stored successfully. 

    python integrity_check.py check logs/app.log
 ![has3](https://github.com/user-attachments/assets/d12c5498-44da-496e-ba37-cc5c99a9d086)

Status: Modified (Hash mismatch) 

Tampered files: logs/app.log
 
    python integrity_check.py check logs/auth.log
   ![has2](https://github.com/user-attachments/assets/1f7ef483-13b0-4a84-ae36-cc8eb263ddad)
