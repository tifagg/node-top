import psutil
import requests
import platform
import socket
import time
import os
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

# Config: add your services here
SERVICES = {
    "llama.cpp": 8080,
    "Kiwix": 8000,
    "Caliber-Web": 8083,
    "LAN IP": None # special case
}

def get_lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def check_port(port):
    try:
        r = requests.get(f"http://localhost:{port}", timeout=1)
        return True
    except:
        return False

def get_battery():
    batt = psutil.sensors_battery()
    if batt:
        return f"{batt.percent}% {'⚡' if batt.power_plugged else '🔋'}"
    return "N/A"

def clear():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def main():
    while True:
        clear()
        os_name = "Termux/Android" if "ANDROID_ROOT" in os.environ else platform.system()

        print(f"{Fore.CYAN}{Style.BRIGHT}[ VEX NODE STATUS ]{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Time: {datetime.now().strftime('%H:%M:%S')} OS: {os_name}")
        print("-" * 40)

        # System stats
        cpu = psutil.cpu_percent(interval=0.5)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        print(f"CPU: {cpu}% {Fore.GREEN if cpu < 60 else Fore.RED}")
        print(f"RAM: {ram.used/1e9:.1f}/{ram.total/1e9:.1f}GB ({ram.percent}%)")
        print(f"Disk: {disk.used/1e9:.1f}/{disk.total/1e9:.1f}GB ({disk.percent}%)")
        print(f"Battery: {get_battery()}")
        print("-" * 40)

        # Service check
        lan_ip = get_lan_ip()
        print(f"{Fore.CYAN}Services:{Style.RESET_ALL}")
        for name, port in SERVICES.items():
            if name == "LAN IP":
                print(f"LAN IP: {Fore.GREEN}{lan_ip}{Style.RESET_ALL}")
                continue

            status = check_port(port)
            color = Fore.GREEN if status else Fore.RED
            state = "UP" if status else "DOWN"
            print(f"{name:<12} :{port:<5} {color}{state}{Style.RESET_ALL} http://{lan_ip}:{port}")

        print("-" * 40)
        print(f"{Fore.YELLOW}Ctrl+C to exit. Refreshing 3s...{Style.RESET_ALL}")
        time.sleep(3)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.CYAN}VEX: Node-top offline, boss.{Style.RESET_ALL}")