#!/usr/bin/env python3

import os
import subprocess
import sys
import shutil
from datetime import datetime

# -----------------------------
# Utility Functions
# -----------------------------

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def check_tool(tool):
    return shutil.which(tool) is not None

def run(cmd, outfile=None):
    log(f"Running: {cmd}")
    try:
        if outfile:
            with open(outfile, "w") as f:
                subprocess.run(cmd, shell=True, stdout=f, stderr=subprocess.DEVNULL)
        else:
            subprocess.run(cmd, shell=True)
    except Exception as e:
        log(f"[!] Error running command: {e}")

# -----------------------------
# Main Function
# -----------------------------

def main():
    if len(sys.argv) < 2:
        print("Usage: ./recon.py <target_domain> [fast/full]")
        sys.exit(1)

    target = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) == 3 else "fast"

    base_dir = f"recon_{target}"
    os.makedirs(base_dir, exist_ok=True)

    log(f"Starting Recon on {target} (Mode: {mode.upper()})")

    # -----------------------------
    # 1. Nmap Scan
    # -----------------------------
    if check_tool("nmap"):
        if mode == "fast":
            cmd = f"nmap -sV -T4 {target}"
        else:
            cmd = f"nmap -p- -sV {target}"

        run(cmd, f"{base_dir}/nmap_scan.txt")
        log("[✔] Nmap completed")
    else:
        log("[!] nmap not found, skipping...")

    # -----------------------------
    # 2. WAF Detection
    # -----------------------------
    if check_tool("wafw00f"):
        run(f"wafw00f https://{target}", f"{base_dir}/waf.txt")
        log("[✔] WAF detection completed")
    else:
        log("[!] wafw00f not found, skipping...")

    # -----------------------------
    # 3. WHOIS
    # -----------------------------
    if check_tool("whois"):
        run(f"whois {target}", f"{base_dir}/whois.txt")
        log("[✔] WHOIS completed")
    else:
        log("[!] whois not found, skipping...")

    # -----------------------------
    # 4. Subdomain Enumeration
    # -----------------------------
    sub_file = f"{base_dir}/subdomains.txt"

    if check_tool("subfinder"):
        run(f"subfinder -d {target}", f"{base_dir}/subfinder.txt")
    else:
        log("[!] subfinder not found")

    if check_tool("assetfinder"):
        run(f"assetfinder --subs-only {target}", f"{base_dir}/assetfinder.txt")
    else:
        log("[!] assetfinder not found")

    # Combine results
    run(
        f"cat {base_dir}/*.txt 2>/dev/null | sort -u > {sub_file}"
    )
    log("[✔] Subdomain enumeration completed")

    # -----------------------------
    # 5. Live Host Check
    # -----------------------------
    live_file = f"{base_dir}/live_hosts.txt"

    if check_tool("httprobe"):
        run(f"cat {sub_file} | httprobe -s -p https:443", live_file)
        log("[✔] Live hosts identified")
    else:
        log("[!] httprobe not found")

    # -----------------------------
    # 6. Screenshots
    # -----------------------------
    if check_tool("gowitness"):
        gowitness_dir = f"{base_dir}/gowitness"
        os.makedirs(gowitness_dir, exist_ok=True)
        run(f"gowitness scan file -f {live_file} --destination {gowitness_dir}")
        log("[✔] Screenshots captured")
    else:
        log("[!] gowitness not found")

    # -----------------------------
    # 7. Nikto (LAST – slow)
    # -----------------------------
    if check_tool("nikto"):
        run(
            f"nikto -h https://{target} -maxtime 300",
            f"{base_dir}/nikto.txt"
        )
        log("[✔] Nikto scan completed")
    else:
        log("[!] nikto not found")

    # -----------------------------
    # 8. Optional Deep Scan
    # -----------------------------
    if mode == "full" and check_tool("nmap"):
        run(
            f"nmap --script dns-brute {target}",
            f"{base_dir}/dns_brute.txt"
        )
        log("[✔] DNS brute completed")

    log("\n[🎉] Recon completed successfully!")
    log(f"[📁] Results saved in: {base_dir}")

# -----------------------------
# Entry Point
# -----------------------------
if __name__ == "__main__":
    main()