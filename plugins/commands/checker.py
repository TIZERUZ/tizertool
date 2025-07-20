from mcstatus import JavaServer
from plugins.common import *

def check(file):
    with open(file, 'r') as f:
             servers = [line.strip() for line in f if line.strip()]
    for server in servers:
        try:
                lookup = JavaServer.lookup(server)
                status = lookup.status()
                logging.success(f"{red}({white}{server}{red})({white}{status.players.online}/{status.players.max}{red})({white}{round(status.latency)}ms{red})({white}{status.version.name}{red})({white}{status.version.protocol}{red})")
        except TimeoutError: pass
        except Exception: pass