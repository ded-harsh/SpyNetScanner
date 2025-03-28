import os
import socket
import subprocess
import datetime
import re

# Create log file
log_file = f"network_scan_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"

def log_data(data):
    with open(log_file, "a") as log:
        log.write(data + "\n")
    print(data)

# Scan for open ports (common range)
def scan_ports():
    log_data("\n[+] Scanning for open ports...\n")
    open_ports = []
    for port in range(1, 1025):  # Scans well-known ports
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex(("127.0.0.1", port))
        if result == 0:
            log_data(f"[*] Port {port} is open")
            open_ports.append(port)
        sock.close()
    return open_ports

# Check services running on open ports
def check_services(ports):
    log_data("\n[+] Checking services running on open ports...\n")
    for port in ports:
        try:
            service = socket.getservbyport(port)
        except:
            service = "Unknown"
        log_data(f"[*] Port {port} is running service: {service}")

# Run netstat to check established connections
def check_netstat():
    log_data("\n[+] Checking active network connections (netstat -ano)...\n")
    result = subprocess.getoutput('netstat -ano | findstr ESTABLISHED')
    log_data(result)
    return result

# Extract and analyze PIDs from netstat
def analyze_pids(netstat_output):
    log_data("\n[+] Checking processes linked to active connections...\n")
    pids = set(re.findall(r'\d+$', netstat_output, re.MULTILINE))
    for pid in pids:
        task_output = subprocess.getoutput(f'tasklist | findstr {pid}')
        log_data(f"[*] PID {pid} - {task_output}")

# Identify external suspicious IPs
def check_external_ips(netstat_output):
    log_data("\n[+] Checking for external IP connections...\n")
    external_ips = re.findall(r'(\d+\.\d+\.\d+\.\d+):\d+', netstat_output)
    suspicious_ips = [ip for ip in external_ips if not ip.startswith("192.168.") and not ip.startswith("127.")]

    if suspicious_ips:
        log_data("[!] Potential suspicious external IPs detected:")
        for ip in suspicious_ips:
            log_data(f" - {ip}")
    else:
        log_data("[+] No suspicious external IPs detected.")

# Main function
def main():
    log_data(f"=== Network Scan Log - {datetime.datetime.now()} ===")
    open_ports = scan_ports()
    check_services(open_ports)
    netstat_output = check_netstat()
    analyze_pids(netstat_output)
    check_external_ips(netstat_output)
    log_data("\n[+] Scan completed. Log saved.")

if __name__ == "__main__":
    main()
