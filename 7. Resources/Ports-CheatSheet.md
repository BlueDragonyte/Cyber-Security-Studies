# Network Ports - Cheat Sheet

## Port Basics
- **Port** = logical endpoint for network communication  
- Format: `IP:PORT` (e.g. `10.0.0.1:443`)  
- Used to identify **services/applications**

---

## Port Ranges

| Range | Type | Description |
|------|------|------------|
| 0–1023 | Well-known | Standard services |
| 1024–49151 | Registered | Applications |
| 49152–65535 | Dynamic/Ephemeral | Temporary client ports |

---

## Web

| Port | Protocol | Description |
|------|---------|------------|
| 80 | HTTP | Web traffic |
| 443 | HTTPS | Secure web (TLS) |
| 8080 | HTTP Alt | Proxy/Web apps |

---

## Remote Access

| Port | Protocol | Description |
|------|---------|------------|
| 22 | SSH | Secure remote login |
| 23 | Telnet | Remote login |
| 3389 | RDP | Windows remote desktop |

---

## Email

| Port | Protocol | Description |
|------|---------|------------|
| 25 | SMTP | Email sending |
| 587 | SMTP TLS | Secure sending |
| 465 | SMTPS | Secure SMTP |
| 110 | POP3 | Retrieve email |
| 995 | POP3S | Secure POP3 |
| 143 | IMAP | Sync email |
| 993 | IMAPS | Secure IMAP |

---

## File Transfer

| Port | Protocol | Description |
|------|---------|------------|
| 20 | FTP Data | Data transfer |
| 21 | FTP Control | File transfer |
| 22 | SFTP | Secure file transfer |

---

## Infrastructure / Enterprise

| Port | Protocol | Description |
|------|---------|------------|
| 53 | DNS | Name resolution |
| 67/68 | DHCP | IP assignment |
| 88 | Kerberos | Authentication (AD) |
| 123 | NTP | Time sync |
| 137–139 | NetBIOS | Legacy Windows |
| 389 | LDAP | Directory services |
| 636 | LDAPS | Secure LDAP |
| 445 | SMB | File sharing |
| 161 | SNMP | Monitoring |
| 162 | SNMP Trap | Alerts |

---

## Databases

| Port | Service | Description |
|------|--------|------------|
| 1433 | MSSQL | Microsoft SQL Server |
| 1521 | Oracle DB | Oracle database |
| 3306 | MySQL | MySQL database |
| 5432 | PostgreSQL | PostgreSQL |

---

## High-Risk Ports

| Port | Risk |
|------|------|
| 21 | FTP (plaintext credentials) |
| 23 | Telnet (plaintext) |
| 3389 | RDP brute force |
| 445 | SMB exploits (e.g. EternalBlue) |
| 389 | LDAP (unencrypted) |

-