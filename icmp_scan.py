import random
import socket
import time
import ipaddress
import struct
import sys
from threading import Thread

SIGNAL = True


def checksum(source_string):
    sum = 0
    count_to = (len(source_string) / 2) * 2
    count = 0
    while count < count_to:
        this_val = source_string[count + 1] * 256 + source_string[count]
        sum = sum + this_val
        sum = sum & 0xffffffff
        count = count + 2
    if count_to < len(source_string):
        sum = sum + source_string[len(source_string) - 1]
        sum = sum & 0xffffffff
    sum = (sum >> 16) + (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def create_packet(id):
    header = struct.pack('bbHHh', 8, 0, 0, id, 1)
    data = 192 * 'Q'
    my_checksum = checksum(header + data.encode())
    header = struct.pack('bbHHh', 8, 0, socket.htons(my_checksum), id, 1)
    return header + data.encode()


def ping(addr, timeout=1):
    try:
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        packet_id = int((id(timeout) * random.random()) % 65535)
        packet = create_packet(packet_id)
        my_socket.connect((addr, 80))
        my_socket.sendall(packet)
        my_socket.close()
    except PermissionError:
        pass
    except Exception as e:
        print(e)


def rotate(addr, wait, responses):
    print("Sending Packets", time.strftime("< %X %x >"))
    for ip in addr:
        ping(str(ip))
        time.sleep(wait)
    print("All packets sent", time.strftime("< %X %x >"))

    print("Waiting for all responses")
    time.sleep(2)

    # Stoping listen
    global SIGNAL
    SIGNAL = False
    ping('127.0.0.1')  # Final ping to trigger the false signal in listen

    print(len(responses), "hosts found!")
    hosts = []
    for response in sorted(responses):
        ip = struct.unpack('BBBB', response)
        ip = f"{ip[0]}.{ip[1]}.{ip[2]}.{ip[3]}"
        hosts.append(ip)
    
    for ipddr in hosts:
        print(f'[*] {str(ipddr)}')

    print("Done", time.strftime("< %X %x >"))


def listen(responses, ip_network):
    global SIGNAL
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
    s.bind(('', 1))
    print("Listening")
    while SIGNAL:
        packet = s.recv(1024)[:20][-8:-4]
        if packet not in responses and ipaddress.ip_address(packet) in ip_network:
            responses.append(packet)
    print("Stop Listening")
    s.close()


if __name__ == "__main__":
    responses = []
    
    if len(sys.argv) >= 2:
        ip = sys.argv[1]
        ips = f'{ip}/24'  # Internet network

        wait = 0.02  # Adjust this based in your bandwidth (Faster link is Lower wait)

        ip_network = ipaddress.ip_network(ips, strict=False)

        t_server = Thread(target=listen, args=[responses, ip_network])
        t_server.start()

        t_ping = Thread(target=rotate, args=[ip_network, wait, responses])
        t_ping.start()
    
    else:
        print('Usage: py icmp_scan.py < ip > (no need "/24")')
