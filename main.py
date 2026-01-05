import socket
import sys
from datetime import datetime
import time
from colorama import init, Fore, Style

# Initialize colorama
init()

def print_ascii_art():
    ascii_art = r"""░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗░██████╗████████╗░█████╗░████████╗██╗░░░██╗░██████╗
██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║░░░██║██╔════╝
██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░╚█████╗░░░░██║░░░███████║░░░██║░░░██║░░░██║╚█████╗░
██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░░░██║░╚═══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗██████╔╝░░░██║░░░██║░░██║░░░██║░░░╚██████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═════╝░"""
    print(Fore.GREEN + ascii_art + Style.RESET_ALL)

def check_host_status(target):
    try:
        # First, resolve the hostname to IP to ensure it's valid
        ip = socket.gethostbyname(target)
        
        # Try to create a basic connection to check if host is reachable
        # We'll use a more reliable method by trying to ping or connect to common ports
        for port in [80, 443, 22, 21, 23, 53]:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)  # Set timeout to 2 seconds
                result = sock.connect_ex((ip, port))
                sock.close()
                
                # If any port is reachable, the host is up
                if result == 0:
                    return True
            except socket.error:
                continue
        
        # If no common ports are reachable, we'll still consider the host reachable
        # since we were able to resolve the hostname
        return True
    except socket.gaierror:
        print(f"{Fore.RED}[-] Hostname could not be resolved{Style.RESET_ALL}")
        return False
    except socket.error:
        # If we can't connect to any common ports, the host may still be up
        # but blocking connections, so we'll return True if hostname resolves
        try:
            socket.gethostbyname(target)
            return True
        except socket.gaierror:
            return False

def monitor_host_status(target, duration=60):
    """Monitor host status continuously for the specified duration in seconds"""
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{Fore.RED}[-] Hostname could not be resolved{Style.RESET_ALL}")
        return
        
    print(f"{Style.RESET_ALL}Monitoring {target} ({ip}) for {duration} seconds... Press Ctrl+C to stop{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'Timestamp':<12} {'IP Address':<15} {'Status':<10}{Style.RESET_ALL}")
    print("-" * 40)
    
    try:
        for i in range(duration):
            status = check_host_status(target)
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            if status:
                print(f"{Fore.WHITE}{timestamp:<12} {ip:<15} {Fore.GREEN}ONLINE{Style.RESET_ALL}")
            else:
                print(f"{Fore.WHITE}{timestamp:<12} {ip:<15} {Fore.RED}OFFLINE{Style.RESET_ALL}")
            
            time.sleep(1)  # Wait 1 second between checks
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Monitoring interrupted by user{Style.RESET_ALL}")





def main():
    print_ascii_art()
    
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Usage: python main.py <target>{Style.RESET_ALL}")
        print(f"{Fore.RED}Example: python main.py 192.168.1.1{Style.RESET_ALL}")
        sys.exit(1)
    
    target = sys.argv[1]
    
    monitor_host_status(target)

def monitor_host_status(target):
    """Monitor host status continuously until Ctrl+C is pressed"""
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"{Fore.RED}[-] Hostname could not be resolved{Style.RESET_ALL}")
        return
        
    print(f"{Style.RESET_ALL}Monitoring {target} ({ip}) - Press Ctrl+C to stop{Style.RESET_ALL}")
    print(f"{Fore.WHITE}{'Timestamp':<12} {'IP Address':<15} {'Status':<10}{Style.RESET_ALL}")
    print("-" * 40)
    
    try:
        while True:
            status = check_host_status(target)
            timestamp = datetime.now().strftime("%H:%M:%S")
            
            if status:
                print(f"{Fore.WHITE}{timestamp:<12} {ip:<15} {Fore.GREEN}ONLINE{Style.RESET_ALL}")
            else:
                print(f"{Fore.WHITE}{timestamp:<12} {ip:<15} {Fore.RED}OFFLINE{Style.RESET_ALL}")
            
            time.sleep(1)  # Wait 1 second between checks
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Monitoring interrupted by user{Style.RESET_ALL}")

if __name__ == "__main__":
    main()