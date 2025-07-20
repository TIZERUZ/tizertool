import dns.resolver
from plugins.common import *

def lookup(domain):
    if not checkserver(domain):
        logging.error(f"{red}Iltimos haqiqiy domen kiriting:{white}")
        return

    print(f"\n{gray}[{red}#{gray}] {white}DNS Serverlar {red}{domain}{white} domen uchun tekshirilmoqda...")

    records = ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'TXT']
    for record in records:
        try:
            results = [r.to_text() for r in dns.resolver.resolve(domain, record)]
            print(f"{white}\n• {red}[{record}]:{white}")
            if results:
                for r in results:
                    print(f"{gray}•{white} {r}")
            else:
                print(f"{gray}•{red}Rekordlar topolmadik")
        except (dns.resolver.NoAnswer, dns.resolver.NoNameservers):
            print(f"\n{white}• {red}[{record}]:{white}")
            print(f"{gray}• Rekordlar topolmadik")
        except dns.resolver.NXDOMAIN:
            logging.error(f"{red}Domain mavjud emas{white}")
            return
        except Exception as e:
            logging.error(f"{red}Xatolik!: {e}{white}")

    print()
