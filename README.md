# SpyNetScanner 🕵️‍♂️🚀  
A powerful **network security tool** that scans open ports, checks running services, monitors active network connections, and logs suspicious external IPs.  

## Features 🔍  
✅ **Port Scanning** – Detects open ports (1-1024).  
✅ **Service Detection** – Identifies services running on open ports.  
✅ **Active Connections Monitoring** – Uses `netstat -ano` to list established connections.  
✅ **Process Analysis** – Finds which processes (PIDs) are using network connections.  
✅ **Suspicious IP Detection** – Flags external IPs that might be a security risk.  
✅ **Logging** – Saves all results in a detailed log file.  

## Installation & Usage 🛠  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/ded-harsh/SpyNetScanner.git
cd SpyNetScanner

2️⃣ Run the Script
bash
Copy
Edit
python network_scan.py
3️⃣ Check the Log File
A log file (spynetscanner_YYYY-MM-DD_HH-MM-SS.log) will be created in the same directory, containing all scan details.

Example Output 📜
kotlin
Copy
Edit
[+] Scanning for open ports...
[*] Port 80 is open
[*] Port 443 is open
...
[+] Checking active network connections (netstat -ano)...
TCP    192.168.1.9:52546    23.54.83.201:443    ESTABLISHED    10192
...
[+] Checking for external IP connections...
[!] Potential suspicious external IPs detected:
 - 4.213.25.241
 - 163.70.138.61
Disclaimer ⚠️
This tool is for educational and security research purposes only. Do not use it on unauthorized networks.

Contributing 🤝
Feel free to fork this repo and submit pull requests!

License 📜
MIT License – Free to use and modify.
