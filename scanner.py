import os
import socket
import threading
import subprocess
import platform
import sys
import json
import re
from scapy.all import ARP, Ether, srp

results = {}
lock = threading.Lock()


# -----------------------------
#   Add Device to Results
# -----------------------------
def add_device(ip, hostname, mac):
    with lock:
        results[ip] = {
            "ip": ip,
            "hostname": hostname,
            "mac": mac
        }


# -----------------------------
#   Get Local IP
# -----------------------------
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()


# -----------------------------
#   Clean MAC Address With Regex
# -----------------------------
def get_mac_from_arp(ip):
    try:
        # Windows and Linux ARP command
        if platform.system().lower() == "windows":
            output = subprocess.check_output("arp -a", shell=True).decode(errors="ignore")
        else:
            output = subprocess.check_output("arp -n", shell=True).decode(errors="ignore")

        # Regex to match MAC xx:xx:xx:xx:xx:xx or xx-xx-xx-xx-xx-xx
        mac_regex = r"((?:[0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2})"

        for line in output.splitlines():
            if ip in line:
                match = re.search(mac_regex, line)
                if match:
                    mac = match.group(1)
                    return mac.replace("-", ":")  # Normalize format
    except:
        pass

    return "Unknown"


# -----------------------------
#   Ping Scan
# -----------------------------
if platform.system().lower() == "windows":
    ping_cmd = "ping -n 1 -w 200 {} > nul"
else:
    ping_cmd = "ping -c 1 -W 200 {} > /dev/null 2>&1"


def ping_scan(ip):
    if os.system(ping_cmd.format(ip)) == 0:
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "No hostname"

        mac = get_mac_from_arp(ip)
        add_device(ip, hostname, mac)


# -----------------------------
#   Scapy ARP Scan
# -----------------------------
def arp_scan(network_prefix):
    target = network_prefix + "0/24"
    arp = ARP(pdst=target)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    answered = srp(packet, timeout=2, verbose=0)[0]

    for sent, received in answered:
        ip = received.psrc
        mac = received.hwsrc.replace("-", ":")
        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "No hostname"

        add_device(ip, hostname, mac)


# -----------------------------
#   Manual Scan (Single IP)
# -----------------------------
def scan_manual(target_ip):
    ping_scan(target_ip)
    mac = get_mac_from_arp(target_ip)
    try:
        hostname = socket.gethostbyaddr(target_ip)[0]
    except:
        hostname = "No hostname"

    add_device(target_ip, hostname, mac)


# -----------------------------
#   Automatic Full Subnet Scan
# -----------------------------
def scan_auto():
    local_ip = get_local_ip()
    prefix = ".".join(local_ip.split(".")[:3]) + "."

    # 1) ARP scan → finds most devices
    arp_scan(prefix)

    # 2) Ping scan to find remaining ones
    threads = []
    for i in range(1, 255):
        ip = prefix + str(i)
        t = threading.Thread(target=ping_scan, args=(ip,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


# -----------------------------
#   Main
# -----------------------------
if __name__ == "__main__":
    if len(sys.argv) > 1:
        scan_manual(sys.argv[1])
    else:
        scan_auto()

    print(json.dumps(list(results.values())))
