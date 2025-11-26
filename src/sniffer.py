"""Sniffer (v2) - detecta IPs com taxa alta de pacotes em intervalos e sinaliza.
Usa scapy (requer root para captura ao vivo).
"""
import time
from collections import defaultdict
try:
    from scapy.all import sniff, IP
except Exception:
    sniff = None
    IP = None

THRESHOLD = 40  # pacotes por intervalo

def packet_callback_factory(packet_count, blocked_ips, start_time):
    def packet_callback(packet):
        if IP is None:
            return
        if not packet.haslayer(IP):
            return
        src_ip = packet[IP].src
        packet_count[src_ip] += 1
        current_time = time.time()
        interval = current_time - start_time[0]
        if interval >= 1:
            for ip, count in list(packet_count.items()):
                rate = count / interval
                if rate > THRESHOLD and ip not in blocked_ips:
                    print(f"[ALERT] Blocking IP: {ip}, packet rate: {rate:.1f}")
                    # NOTE: system iptables call commented for safety in generic repo
                    # os.system(f"iptables -A INPUT -s {ip} -j DROP")
                    blocked_ips.add(ip)
            packet_count.clear()
            start_time[0] = current_time
    return packet_callback

def run_sniffer(filter_exp='ip'):
    packet_count = defaultdict(int)
    blocked_ips = set()
    start_time = [time.time()]
    cb = packet_callback_factory(packet_count, blocked_ips, start_time)
    if sniff is None:
        print('Scapy not available in this environment. This module requires scapy and root.')
        return
    print('Starting sniffer... (CTRL+C to stop)')
    sniff(filter=filter_exp, prn=cb)

if __name__ == '__main__':
    run_sniffer()
