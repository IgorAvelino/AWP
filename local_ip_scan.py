import argparse
import pythonping
from concurrent.futures import ThreadPoolExecutor


parser = argparse.ArgumentParser(description='\033[31mLAN Scan by 0xS1f\033[0;0;0m')


def sys_options():
    parser.add_argument('-n', '--network', type=str, dest='network_ip', default=None,
                        help='The LAN Network base IP ex.:192.168.1 (REQUIRED)', required=True)

    return parser.parse_args()


def ping(ip):
    try:
        ping_result = pythonping.ping(target=ip, count=1, timeout=4)
        if ping_result.stats_success_ratio == 1:
            return ip
    
    except Exception as e:
        print(f'\n\033[31mFATAL-ERROR:\033[0;0;0m << {e} >>\n')
    return None


def scan_network(base_ip):
    network_ip = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(ping, f"{base_ip}.{i}") for i in range(1, 255)]
        for future in futures:
            ip = future.result()
            if ip:
                network_ip.append(ip)
    return network_ip


if __name__ == "__main__":

    args = sys_options()

    print(f"\033[33m[i]\033[0;0;0m Scanning \033[36m{args.network_ip}.0/24\033[0;0;0m")
    active = scan_network(args.network_ip)
    print("\n\033[32m[+]\033[0;0;0m Active IPs Found:")
    for ip in active:
        print(ip)
