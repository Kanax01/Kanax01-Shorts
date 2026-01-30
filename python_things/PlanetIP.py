import os
import requests

from argparse import ArgumentParser
from colorama import Fore, Style

logo = """
 _ __  _                     ____ __ 
( /  )//              _/_   ( /( /  )
 /--'// __,  _ _   _  /      /  /--' 
/   (/_(_/(_/ / /_(/_(__   _/_ /     
                                     
"""

args = ArgumentParser()
args.add_argument("ip", type=str)
options = args.parse_args()


ip = options.ip



def main():
    os.system("cls")
    print(Fore.RED + Style.BRIGHT + logo)
    os.system("title Planet IP - By, Kanax01")
    
    if ip is None:
       print(Fore.YELLOW + "[!] Please provide an IP Address to track.")
       exit()
        
    req = requests.get(f"http://ip-api.com/json/{ip}")
    result = req.json()

    
    print(Fore.CYAN + "[*] Fetching data for IP...\n")

    
    if result['status'] == 'fail':
        print(Fore.YELLOW + "[!] Invalid IP Address provided.")
        exit()
    
    print(Fore.RED + f"\n === LOCATION INFORMATION === \n")
    print(Fore.GREEN + f"[*] IP Address: "+ Fore.WHITE + ip)
    print(Fore.GREEN + f"[*] Country: " + Fore.WHITE + result["country"])
    print(Fore.GREEN + f"[*] Region: " + Fore.WHITE + result["regionName"])
    print(Fore.GREEN + f"[*] City: " + Fore.WHITE + result["city"])
    print(Fore.GREEN + f"[*] Zip: " + Fore.WHITE + result["zip"])
    print(Fore.GREEN + f"[*] Timezone: " + Fore.WHITE + result["timezone"])
    print(Fore.GREEN + f"[*] Lat/Lon: " + Fore.WHITE + f"{result["lat"]}, {result["lon"]}")
    
    print(Fore.RED + f"\n === ISP INFORMATION === \n")
    print(Fore.GREEN + f"[*] Isp: " + Fore.WHITE + result["isp"])
    print(Fore.GREEN + f"[*] Org: " + Fore.WHITE + result["org"])
    print(Fore.GREEN + f"[*] As: " + Fore.WHITE + result["as"])
    print("\n\n")
    exit = input(Fore.CYAN + f"Press ENTER To Exit\n" + Fore.WHITE + Style.NORMAL)

    

if __name__ == "__main__":
    main()
