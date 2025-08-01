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

3. Check File Integrity
   
        Command: python integrity_check.py check logs
   
        Description: Verifies if any file was modified or tampered with. 

5. Update Hash (after legitimate changes)
   
       Command: python integrity_check.py update logs/app.log
   
       Description: Updates hash for a specific file. 

# Example Output: 

    python integrity_check.py init logs
 
Hashes stored successfully. 

    python integrity_check.py check logs/app.log
 
Status: Modified (Hash mismatch) 

Tampered files: logs/app.log
 
    python integrity_check.py check logs/auth.log

Status: Unmodified 

    python integrity_check.py update logs/app.log

Hash updated successfully. 

# Tech Stack: 
 • Python 3.10+ 
 
 • SHA-256 Hashing 
 
 • JSON-based hash storage 
