#!/usr/bin/env python3

import os
import subprocess
import sys
from datetime import datetime

# -----------------------------
# Colors (CLI Styling)
# -----------------------------
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

# -----------------------------
# Utility Functions
# -----------------------------
def log(msg, color=BLUE):
    print(f"{color}[{datetime.now().strftime('%H:%M:%S')}] {msg}{RESET}")

def success(msg):
    print(f"{GREEN}[✔] {msg}{RESET}")

def error(msg):
    print(f"{RED}[✘] {msg}{RESET}")

def run(cmd, outfile=None):
    log(f"Running: {cmd}", YELLOW)
    try:
        if outfile:
            with open(outfile, "w") as f:
                result = subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.DEVNULL)
        else:
            result = subprocess.run(cmd, shell=True)

        if result.returncode == 0:
            success("Completed successfully")
        else:
            error("Command failed")

    except Exception as e:
        error(f"Error: {e}")

# -----------------------------
# Banner
# -----------------------------
def banner():
    print(f"""{BLUE}
   ____                        __  __
  / __ \\___  ____ ___  ____ _/ /_/ /
 / /_/ / _ \\/ __ `__ \\/ __ `/ __/ / 
/ _, _/  __/ / / / / / /_/ / /_/ /  
/_/ |_|\\___/_/ /_/ /_/\\__,_/\\__/_/   

   🔍 Recon Automation Tool
{RESET}""")

# -----------------------------
# Main Function
# -----------------------------
def main():
    banner()

    if len(sys.argv) != 2:
        print("Usage: python3 recon.py <target_domain>")
        sys.exit(1)

    target = sys.argv[1]
    base_dir = f"recon_{target}"
    os.makedirs(base_dir, exist_ok=True)

    log(f"Starting Recon on {target}")

    # 1. Nmap
    log("Step 1: Nmap Scan")
    run(f"nmap -sV -T4 {target}", f"{base_dir}/nmap_scan.txt")

    # 2. Nikto
    log("Step 2: Nikto Scan")
    run(f"nikto -h https://{target} -maxtime 300", f"{base_dir}/nikto.txt")

    # 3. WAF
    log("Step 3: WAF Detection")
    run(f"wafw00f https://{target}", f"{base_dir}/waf.txt")

    # 4. WHOIS
    log("Step 4: WHOIS Lookup")
    run(f"whois {target}", f"{base_dir}/whois.txt")

    # 5. Subdomains
    log("Step 5: Subdomain Enumeration")

    run(f"subfinder -d {target}", f"{base_dir}/subfinder.txt")
    run(f"assetfinder --subs-only {target}", f"{base_dir}/assetfinder.txt")

    sub_file = f"{base_dir}/subdomains.txt"
    run(f"cat {base_dir}/subfinder.txt {base_dir}/assetfinder.txt | sort -u > {sub_file}")

    # 6. Live Hosts
    log("Step 6: Live Host Detection")
    live_file = f"{base_dir}/live_hosts.txt"
    run(f"cat {sub_file} | httprobe -s -p https:443", live_file)

    # 7. Screenshots
    log("Step 7: Screenshot Capture")
    gowitness_dir = f"{base_dir}/gowitness"
    os.makedirs(gowitness_dir, exist_ok=True)
    run(f"gowitness scan file -f {live_file} --destination {gowitness_dir}")

    log("\nRecon completed successfully!", GREEN)
    log(f"Results saved in: {base_dir}", GREEN)

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()