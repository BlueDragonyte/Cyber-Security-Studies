# Cyber Security Cheat Sheet — Nmap

## What is Nmap?
- **Nmap (Network Mapper)** = tool for network discovery and security auditing
- Used to identify:
  - Open ports
  - Services
  - Versions
  - OS detection
  - Vulnerabilities (via scripts)

---

## Basic Syntax

```bash
nmap [scan type] [options] <target>
```

---

## Common Scan Types

| Command | Description |
|--------|------------|
| `nmap <IP>` | Basic scan (top 1000 TCP ports) |
| `nmap -p- <IP>` | Scan all 65535 ports |
| `nmap -sS <IP>` | SYN scan (stealth / half-open) |
| `nmap -sT <IP>` | TCP connect scan |
| `nmap -sU <IP>` | UDP scan |
| `nmap -sn <IP>` | Ping scan (host discovery only) |

---

## Port & Target Options

| Command | Description |
|--------|------------|
| `nmap -p 80,443 <IP>` | Scan specific ports |
| `nmap -p 1-1000 <IP>` | Scan port range |
| `nmap -iL targets.txt` | Scan list of targets |
| `nmap 192.168.1.0/24` | Scan subnet |

---

## Service & Version Detection

| Command | Description |
|--------|------------|
| `nmap -sV <IP>` | Detect service versions |
| `nmap -A <IP>` | Aggressive scan (OS, version, scripts, traceroute) |
| `nmap -O <IP>` | OS detection |

---

## Timing & Performance

| Command | Description |
|--------|------------|
| `nmap -T0` | Paranoid (slowest) |
| `nmap -T3` | Normal (default) |
| `nmap -T4` | Faster scan |
| `nmap -T5` | Aggressive (fastest, noisy) |

---

## Evasion Techniques

| Command | Description |
|--------|------------|
| `nmap -Pn <IP>` | Skip host discovery |
| `nmap -f <IP>` | Fragment packets |
| `nmap --source-port 53 <IP>` | Spoof source port |
| `nmap -D RND:10 <IP>` | Decoy scan |

---

## NSE (Nmap Scripting Engine)

| Command | Description |
|--------|------------|
| `nmap --script=vuln <IP>` | Run vulnerability scripts |
| `nmap --script=default <IP>` | Default scripts |
| `nmap --script=http-enum <IP>` | Web enumeration |
| `nmap --script=smb-enum-shares <IP>` | SMB enumeration |

---

## Output Options

| Command | Description |
|--------|------------|
| `nmap -oN output.txt <IP>` | Normal output |
| `nmap -oX output.xml <IP>` | XML output |
| `nmap -oG output.gnmap <IP>` | Greppable output |

---

## Practical Combos (Real-World Use)

### Full Recon Scan
```bash
nmap -sS -sV -O -T4 -p- <IP>
```

### Quick Scan
```bash
nmap -T4 -F <IP>
```

### Stealthy Scan
```bash
nmap -sS -T2 <IP>
```

### Vulnerability Scan
```bash
nmap --script=vuln -sV <IP>
```

---

## Key Notes

- SYN scan (`-sS`) = stealthier than TCP connect  
- UDP scans are slower and less reliable  
- `-A` is noisy → avoid in stealth scenarios  
- `-Pn` useful when ICMP is blocked  
- Always scan **only authorised targets**
- “Nmap is used for network discovery, port scanning, and service enumeration.”
- “Different scan types balance stealth vs accuracy.”
- “NSE scripts extend Nmap for vulnerability detection and enumeration.”
