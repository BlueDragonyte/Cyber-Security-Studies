# Brute Force

## 1.1. Category

Identity & Authentication Attacks → Credential Attacks

## 1.2. MITRE ATT&CK Mapping

T1110 – Brute Force

Sub-techniques:

- T1110.001 – Password Guessing
- T1110.002 – Password Cracking
- T1110.003 – Password Spraying
- T1110.004 – Credential Stuffing

## 1.3. Definition

A Brute Force Attack is a credential attack where an adversary attempts multiple password combinations against a user account or authentication service until the correct password is discovered.

Attackers automate this process using scripts or specialised tools to rapidly test password combinations.

Brute force attacks typically target:

- User login portals
- Remote access services
- Active Directory authentication
- VPN portals
- Web applications
- SSH or RDP services

## 1.4. Technical Flow

Attacker identifies an authentication service.

Examples:
- VPN login portal
- Microsoft RDP
- SSH server
- Web application login

1. Attacker selects a target account.
2. Automated tool attempts multiple password combinations. Examples: Password123
3. Authentication service processes login attempts
4. Once a valid password is found, attacker gains access, which can lead to: privilege escalation, lateral movement, data exfiltration

## 1.5. Example Attack Scenario

An attacker targets a corporate VPN login portal.

Steps:
- Identifies VPN endpoint exposed to internet
- Targets common account names
- Uses automated tool to test thousands of passwords
- Successfully logs in with weak password

Example compromised account:

```[bash]
Bobs.Uncle
Password: Summer2026
}
```
## 1.6. Tools Used by Attackers

Hydra: Fast password cracking tool supporting multiple protocols.

```[bash]
hydra -l admin -P passwords.txt ssh://192.168.1.10
```
Medusa: Parallel login brute forcing tool. Performs parallel brute-force authentication attempts against network services such as SSH, FTP, SMB, and RDP.

```[bash]
medusa -h 192.168.1.10 -u admin -P passwords.txt -M ssh
```
Ncrack: Network authentication cracking tool. Designed for high-speed network authentication cracking across services like:

- RDP
- SSH
- FTP
- SMB
- Telnet

```[bash]
ncrack -p ssh -U users.txt -P passwords.txt 192.168.1.10
ncrack -p rdp -U users.txt -P passwords.txt 192.168.1.10
```

Burp Suite: Used to brute force web logins. Burp Suite’s Intruder module can automate login attempts against web applications.

Example Flow
1.  Capture login request via Burp Proxy
2. Send request to Intruder
```[bash]
POST /login HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

username=admin&password=test
```
4. Define payload positions
Example payload list:
 - password123
 - welcome123
 - admin123

Burp Suite will automate the login attempts.

CrackMapExec: Used in Active Directory environments.

```[bash]
crackmapexec smb 10.10.10.0/24 -u admin -p passwords.txt
```

## 1.7. Detection Methods

Windows Event Logs
 - Windows Event ID 4625 – Failed login
 - Windows Event ID 4624 – Successful login
 - Kerberos Event 4771 – Pre-auth failure

Indicators:
 - multiple failed logins from same IP
 - repeated attempts across multiple accounts
 - login attempts at abnormal times


### Network Detection
Security tools may detect:
 - unusual login volume
 - authentication bursts
 - login attempts from foreign countries

## 1.8. Mitigation / Prevention

Account lockout policies
 - failed attempts → account locked for 15 minutes