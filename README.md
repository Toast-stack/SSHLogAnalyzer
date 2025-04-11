# SSHLogAnalyzer
Python tool for analyzing SSH logs to detect potential brute force attacks. Parses logs to identify failed login attempts and flag suspicious IPs. Aimed at system admins and cybersecurity enthusiasts, with plans for GeoIP lookup and automated blocking enhancements. This is the second part of a different project that can be found [here](https://github.com/Toast-stack/VMs-Setup-for-SIEM-projects)

## Overview
This Python-based tool analyzes SSH logs (`auth.log`) to detect failed login attempts and identify potential brute force attackers. It was developed in a controlled virtualized environment to simulate real-world scenarios where system administrators and cybersecurity analysts must identify and respond to security incidents.

## Environmental Details
This project leverages a dual-VM setup to replicate an attacker-victim scenario, providing a practical and hands-on learning experience.

### **1. Victim Machine (Ubuntu VM)**
- **Operating System**: Ubuntu 20.04 LTS
- **Role**: Serves as the target machine running an SSH service.
- **Purpose**:
  - Hosts the SSH logs ('/var/log/auth.log') that the tool parses.
  - Demonstrates how real-world systems log login attempts and how attackers can exploit weak configurations.
- **Security Configurations**:
  - SSH server enabled with default settings.
  - Intentional use of weak or guessable credentials to facilitate brute force attempts (for testing purposes only).
  - VirtualBox Guest Additions installed to enable clipboard sharing and seamless interaction with host machine.
 
### **2. Attacker Machine (Kali Linux VM)**
- **Operating System**: Kali Linux
- **Role**: Simulates an external attacker performing brute force attempts on the victim machine.
- **Tools Used**: 
  - **Hydra**: A powerful brute-force tool used to attempt SSH login using a wordlist.
    ``` bash
    hydra -l root -P wordlist.txt ssh://<victim-IP>
    ```
  - **Nmap**: Used for reconnaissance to identify open SSH ports.
    ``` bash
    nmap -p 22 <victim-IP>
    ```
- **Purpose**:
  - Replicates a common attacker behavior: brute force attempts targeting SSH services.
  - Allows an Analyst to observe malicious activity in the logs and understand the attack pattern.

### **Why use a Virtualized Setup?**
- **Controlled Environment**: Virtual machines isolate test scenarios from critical systems, ensuring safety during experimentation
- **Realism**: Mimics real-world attack and defense scenarios, giving analysts hands-on experience.

## Why Understanding This is Important for Analysts
- **Log Analysis is Fundamental**: Logs are the first place analysts look to detect malicious activity. Familiarity with how systems log events (e.g., failed logins) is essential for effective threat detection.
- **Simulated Attacks Provide Insight**: By observing how attackers operate (e.g., brute force attempts), analysts can develop a deeper understanding of attack patterns and their corresponding log entries.
- **Incident Response Preparation**: Tools like this one align with the internal steps of the NIST Incident Response Framework: *Identification* and *Containment*. Analysts must know how to detect and validate incidents before escalating them.
- **Building a Foundation**: Mastering basic skills like SSH configuration, log analysis, and scripting is critical for entry-level roles like SOC Analyst or IT Security Analyst.

## Features

- Parses SSH logs to identify failed login attempts.
- Counts occurrences of failed attempts per IP address.
- Flags IPs with 5+ failed attempts as potential brute force attackers.

### Example Output
```Plaintext
Failed Login Attempts by IP Address:
192.168.56.101: 10 times

Suspicious IPs (5+ failed attempts):
192.168.56.101 - Potential brute force attacker
```
## Installations
1. Clone the repository:
   ```bash
   git clone https://github.com/Toast-stack/SSHLogAnalyzer.git
   cd SSHLogAnalyzer
   ```
2. Ensure Python 3.x is installed:
   ```bash
   python3 --version
   ```
3. Run the script:
   ```bash
   python3 SSHLogAnalyzer.py
   ```

## Usage Instructions
  * Place the script in a directory with access to your SSH log file (`auth.log`).
  * Run the script and review the output for flagged IPs.
  * Optionally, block malicious IPs using firewall rules:
```bash
sudo ufw deny from <attacker-IP>
```

## Future Enhancements
* **GeoIP Integration**: Determine the geographical location of suspicious IPs.
* **Automated Firewall Rules**: Automatically block flagged IPs.
* **Alerting System**: Send notifications (e.g., email or Slack) for detected brute force attacks.
* **Centralized Logging**: Integrate with SIEM platforms for real-time monitoring and response.

## Limitations
  * Currently requires manual intervention to block malicious IPs.
  * Only scans the default SSH log file (`auth.log`). Custom log paths must be configured manually.

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this software.
