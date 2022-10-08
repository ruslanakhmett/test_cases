import re
import subprocess

import netfilterqueue
import scapy.all as scapy
from flashtext import KeywordProcessor


def word_replacer(html_text):
    keyword_processor = KeywordProcessor()
    keyword_dictionary = {"!_!_!_!": ["parameters",
                                      "together",
                                      "GET",
                                      "October",
                                      ]}
    keyword_processor.add_keywords_from_dict(keyword_dictionary)
    new_text = keyword_processor.replace_keywords(html_text.decode())
    return new_text.encode()


def set_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.TCP].chksum
    return packet


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print("[+] Request")
            modified_load = re.sub(
                r"Accept-Encoding:.*\r\n".encode(),
                "",
                scapy_packet[scapy.Raw].load,
            )
            new_packet = set_load(scapy_packet, modified_load)
            packet.set_payload(bytes(new_packet))
        elif scapy_packet[scapy.TCP].sport == 80:
            print("[+] Response")
            modified_load = word_replacer(scapy_packet[scapy.Raw].load)
            new_packet = set_load(scapy_packet, modified_load)
            packet.set_payload(bytes(new_packet))
    packet.accept()


if __name__ == "__main__":
    try:
        subprocess.call("iptables -I INPUT -j NFQUEUE --queue-num 0",
                        shell=True
                        )
        subprocess.call("iptables -I OUTPUT -j NFQUEUE --queue-num 0",
                        shell=True
                        )

        queue = netfilterqueue.NetfilterQueue()
        queue.bind(0, process_packet)
        queue.run()
    except KeyboardInterrupt:
        print("\nFlushing IP Tables")
        subprocess.call("iptables --flush", shell=True)
