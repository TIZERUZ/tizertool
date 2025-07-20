from mcstatus import JavaServer
from plugins.common import *
import socket

def server(server):
    try:
        if not checkserver(server):
            logging.error('Iltimos, Real domen kiriting:')
            return

        lookup = JavaServer.lookup(server, timeout=5)
        status = lookup.status()
        ip = lookup.address.resolve_ip()

        print(f"\n{gray}[{red}#{gray}] {white}Tekshirilmoqda {red}{server}{white} bilan {gray}mcstatus{white}...\n")
        print(f"{white}• {red}IP:{white} {ip} {red}({is_protected(ip)})")
        print(f"{white}• {red}MOTD:{white}")
        motd = status.motd.to_ansi().splitlines()
        for line in motd:
            print(f"  {gray}•{white} {line}")
        print(f"{white}• {red}Versiya:{white} {status.version.name}")
        print(f"{white}• {red}Protokol:{white} {status.version.protocol}")
        print(f"{white}• {red}O'yinchilar:{white} {status.players.online}/{status.players.max}")
        print(f"{white}• {red}Ping:{white} {round(status.latency)}ms\n")

    except TimeoutError: logging.info('Server offlayn')
