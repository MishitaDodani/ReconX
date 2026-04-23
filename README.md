# 🔍 ReconX – Automated Web Reconnaissance Framework

ReconX is a Python-based automation tool designed to streamline the **reconnaissance phase of web penetration testing and bug bounty hunting**.

It integrates multiple industry-standard tools into a single workflow, reducing manual effort and improving efficiency.

---

## 🚀 Features

* 🔎 **Port & Service Scanning** using Nmap
* 🛡️ **WAF Detection** using Wafw00f
* 📜 **WHOIS Lookup**
* 🌍 **Subdomain Enumeration** (Subfinder + Assetfinder)
* 📡 **Live Host Detection** using Httprobe
* 📸 **Website Screenshot Capture** using Gowitness
* 🔍 **Web Vulnerability Scanning** using Nikto (time-limited)
* ⚡ **Fast & Full Scan Modes**
* 🧠 **Tool Availability Check (Auto-Skip if missing)**
* 📁 Structured output storage

---

## 🛠️ Tech Stack

* Python 3
* Subprocess automation
* Linux-based security tools:

  * Nmap
  * Nikto
  * Wafw00f
  * Subfinder
  * Assetfinder
  * Httprobe
  * Gowitness
  * Whois

---

## 📂 Project Structure

```bash
recon_<target>/
├── nmap_scan.txt
├── waf.txt
├── whois.txt
├── subfinder.txt
├── assetfinder.txt
├── subdomains.txt
├── live_hosts.txt
├── nikto.txt
├── dns_brute.txt (full mode only)
└── gowitness/
```

---

## ▶️ Usage

### Fast Mode (Recommended)

```bash
python3 recon.py example.com fast
```

### Full Mode (Deep Scan)

```bash
python3 recon.py example.com full
```

---

## ⚙️ Requirements

Ensure the following tools are installed and available in PATH:

```bash
nmap nikto wafw00f subfinder assetfinder httprobe gowitness whois
```

---

## ⚡ Notes

* Fast mode is optimized for quick reconnaissance.
* Full mode performs deeper scans (may take longer).
* Nikto scan is limited using `-maxtime` to prevent long delays.
* Missing tools are automatically skipped.
* Output files are overwritten on each run.

---

## 🎯 Use Cases

* Bug bounty reconnaissance
* Web penetration testing
* Cybersecurity automation practice
* Learning tool integration in Python

---

## 👩‍💻 Author

Mishita Dodani
Ethical Hacker & Web Penetration Tester

---

## ⭐ Future Improvements

* Parallel scanning for faster execution
* HTML report generation
* Colored CLI output
* Integration with vulnerability scanners (e.g., Nuclei)
* Docker support
