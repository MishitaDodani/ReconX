<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b0c10,50:1f2833,100:0b0c10&height=160&section=header&text=ReconMatt&fontSize=52&fontColor=00ff41&fontAlignY=42&desc=Automated%20Reconnaissance%20%26%20OSINT%20Tool&descAlignY=62&descSize=16&animation=fadeIn" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/MishitaDodani)
[![Kali Linux](https://img.shields.io/badge/Kali_Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white)](https://github.com/MishitaDodani)
[![Nmap](https://img.shields.io/badge/Nmap-0E83CD?style=for-the-badge&logo=nmap&logoColor=white)](https://github.com/MishitaDodani)
[![Shell](https://img.shields.io/badge/Bash-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)](https://github.com/MishitaDodani)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://github.com/MishitaDodani)

<br/>

> *"The quieter you become, the more you are able to hear."* — Kali Linux

</div>

---

## 🔍 What is ReconMatt?

**ReconMatt** is a **Python-based automated reconnaissance tool** designed for penetration testers and bug bounty hunters. It chains together industry-standard security tools into a single, clean pipeline — from port scanning to live host detection to screenshot capture — saving hours of manual recon work.

Built with colored CLI output and step-by-step logging, it gives you full visibility into every phase of the recon process.

---

## ⚡ Recon Pipeline

```
Target Domain
     │
     ├── 1️⃣  Nmap          →  Port & Service Version Scan
     ├── 2️⃣  Nikto         →  Web Vulnerability Scan
     ├── 3️⃣  wafw00f       →  WAF Detection
     ├── 4️⃣  WHOIS         →  Domain Registration Info
     ├── 5️⃣  subfinder     →  Passive Subdomain Enumeration
     │   + assetfinder   →  Additional Subdomain Discovery
     │   → Deduplicated subdomains.txt
     ├── 6️⃣  httprobe      →  Live Host Detection (HTTP/HTTPS)
     └── 7️⃣  gowitness     →  Screenshot Capture of Live Hosts
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎨 **Colored CLI Output** | Green ✔ / Red ✘ status per step with timestamps |
| 📁 **Auto Output Directory** | All results saved to `recon_<target>/` automatically |
| 🔗 **Tool Chaining** | Each phase feeds data into the next seamlessly |
| 🧹 **Deduplication** | Subdomains merged and sorted via `sort -u` |
| 🛡️ **WAF Detection** | Identifies Web Application Firewalls before attacking |
| 📸 **Visual Recon** | Screenshots all live hosts via gowitness |
| ⚡ **Simple Usage** | Single command, one argument — zero config needed |

---

## 🛠️ Tools Required

Install all dependencies before running:

```bash
# Package manager tools
sudo apt install nmap nikto whois -y

# Go-based tools
go install github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest
go install github.com/tomnomnom/assetfinder@latest
go install github.com/tomnomnom/httprobe@latest
go install github.com/sensepost/gowitness@latest

# Python tool
pip install wafw00f
```

---

## 🚀 Installation & Usage

```bash
# Clone the repository
git clone https://github.com/MishitaDodani/ReconMatt.git
cd ReconMatt

# Run against a target
python3 recon.py <target_domain>
```

**Example:**
```bash
python3 recon.py example.com
```

---

## 📂 Output Structure

```
recon_example.com/
│
├── nmap_scan.txt        # Open ports & running services
├── nikto.txt            # Web vulnerabilities found
├── waf.txt              # WAF type & detection result
├── whois.txt            # Domain registration data
├── subfinder.txt        # Subdomains from subfinder
├── assetfinder.txt      # Subdomains from assetfinder
├── subdomains.txt       # Merged & deduplicated list
├── live_hosts.txt       # Confirmed live HTTP/HTTPS hosts
└── gowitness/           # Screenshots of live hosts
    ├── screenshot_1.png
    └── ...
```

---

## 🖥️ CLI Preview

```
   ____                        __  __
  / __ \___  ____ ___  ____ _/ /_/ /
 / /_/ / _ \/ __ `__ \/ __ `/ __/ / 
/ _, _/  __/ / / / / / /_/ / /_/ /  
/_/ |_|\___/_/ /_/ /_/\__,_/\__/_/   
   🔍 Recon Automation Tool

[10:23:01] Starting Recon on example.com
[10:23:01] Step 1: Nmap Scan
[10:23:01] Running: nmap -sV -T4 example.com
[✔] Completed successfully
[10:23:45] Step 2: Nikto Scan
[10:23:45] Running: nikto -h https://example.com -maxtime 300
[✔] Completed successfully
...
[✔] Recon completed successfully!
[✔] Results saved in: recon_example.com
```

---

## ⚠️ Legal Disclaimer

> This tool is intended **strictly for authorized penetration testing, bug bounty programs, and educational use only.**
> Running this tool against targets **without explicit written permission** is **illegal** and unethical.
> The author holds **no responsibility** for any misuse of this tool.
> **Always hack ethically and responsibly. 🔐**

---

## 🎯 Roadmap

- [ ] Add `--fast` / `--full` scan mode flag
- [ ] JSON report export
- [ ] Slack / Discord webhook notifications
- [ ] Auto-install missing tools
- [ ] HTML report dashboard

---

## 👩‍💻 Author

<div align="center">

**Mishita Dodani**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/mishita-dodani)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/MishitaDodani)
[![Email](https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:mishitadodani068@gmail.com)

*Cybersecurity Enthusiast | Penetration Tester in Training*

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0b0c10,50:1f2833,100:0b0c10&height=100&section=footer&animation=fadeIn" width="100%"/>

⭐ **Star this repo if it helped your recon workflow!**

</div>
