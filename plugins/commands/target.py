import requests
from plugins.common import *

def target(domain):
    if not checkserver(domain): logging.error('Iltimos, Real domen kiriting:'); return

    r = requests.get(f'https://api.hackertarget.com/hostsearch/?q={domain}')
    results = r.text.strip().split('\n')
    iplen = max(len(x.split(',')[1]) for x in results) + 1
    domlen = max(len(x.split(',')[0]) for x in results) + 1

    print(f"\n{gray}[{red}#{gray}] {white}Tekshirilmoqda {red}{domain}{white} bilan {gray}hackertarget.com{white}...\n")
    print(f"{white}• {red}Hostlar topildi:{white}")
    for result in results:
        dom, ip = result.split(',')
        print(f"  {gray}•{white} {ip.ljust(iplen)}  {dom.ljust(domlen)}  {red}({is_protected(ip)})")
    print('\n')