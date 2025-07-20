import requests
import socket
from plugins.common import *

def ipinfo(server):
    try:
        try: ip = socket.gethostbyname(server)
        except socket.gaierror: ip = server

        if not checkip(ip):
            logging.error('Iltimos haqiqiy IP Address yoki Domen kiriting.')
            return

        response = requests.get(f"http://ip-api.com/json/{ip}?fields=status,message,country,isp,org,proxy,mobile,hosting")
        data = response.json()

        if data.get("status") != "success":
            logging.error(f"API error: {data.get('message')}")
            return

        print(f"\n{gray}[{red}#{gray}] {white}Tekshirilyapti {red}{ip}{white} bilan {gray}ip-api.com{white}...\n")
        print(f"{white}• {red}IP Ma'lumoti:{white}")
        print(f"  {gray}•{white} {'Davlat:'.ljust(15)}{green}{data['country']}")
        print(f"  {gray}•{white} {'ISP:'.ljust(15)}{white}{data['isp']}")
        print(f"  {gray}•{white} {'Tashkilot:'.ljust(15)}{white}{data['org']}")
        print(f"  {gray}•{white} {'Proksi/VPN:'.ljust(15)}{green if not data['proxy'] else red}{data['proxy']}")
        print(f"  {gray}•{white} {'Hosting/DC:'.ljust(15)}{green}{data['hosting']}")
        print(f"  {gray}•{white} {'Mobile Conn:'.ljust(15)}{green}{data['mobile']}\n")

    except Exception as e:
        logging.error(f"Xatolik: {e}")
