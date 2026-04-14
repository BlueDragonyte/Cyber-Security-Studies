# Splunk SIEM Lab Build - Stage 1

## Overview
This project documents the full build of a Splunk SIEM lab from scratch using Ubuntu Server on VMware.

---

## Lab Objective
Build a dedicated Ubuntu-based Splunk SIEM server for a personal SOC lab.

---

## Architecture
- Ubuntu VM → Splunk SIEM
- Ubuntu VM → BookStack
- Windows VM → Log Source (future)
- Kali VM → Attack simulation

---

## Splunk VMware Configuration
- CPU: 1 processor / 4 cores
- RAM: 8GB
- Disk: 80GB
- Network: NAT (after fix)

---

## Ubuntu Installation
- Ubuntu Server (minimized)
- DHCP during install
- OpenSSH enabled
- LVM enabled

---

## Networking Issue & Fix
Problem:
- apt update failed

Cause:
- Host-only network + VPN

Fix:
```bash
ip a
sudo apt update
```

---

## File Transfer (Shared Folder)
```bash
sudo apt install open-vm-tools -y
sudo mkdir -p /mnt/hgfs
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```

---

## Copy Splunk Installer
```bash
cp splunk-*.deb ~/
```

---

## Install Splunk
```bash
sudo dpkg -i splunk-*.deb
sudo apt --fix-broken install -y
```

---

## Start Splunk
```bash
sudo /opt/splunk/bin/splunk start --accept-license
```

---

## Fix splunkd not running
```bash
sudo chown -R splunk:splunk /opt/splunk
sudo su - splunk
/opt/splunk/bin/splunk start --accept-license
```

---

## Access Web UI
http://<vm-ip>:8000

---

## Current Status
- Ubuntu installed
- Network fixed
- Splunk installed
- Splunk running
- Web UI accessible

---

## Next Steps
- Configure static IP
- Add Windows logs
- Install Sysmon
- Forward logs to Splunk
- Simulate attacks
