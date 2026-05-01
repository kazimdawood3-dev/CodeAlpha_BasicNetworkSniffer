from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        proto = packet["IP"].proto
        print(f"Source: {src_ip} | Destination: {dst_ip} | Protocol: {proto}")
print("Sniffing started...")
sniff(prn=packet_callback, store=0)
