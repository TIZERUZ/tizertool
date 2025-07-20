from mcstatus import JavaServer
from plugins.common import *
import time

def monitor(s):
    if not checkserver(s): logging.error('Iltimos, Real domen kiriting:'); return
    l=JavaServer.lookup(s);o=set()
    while True:
        try:
            n=set(l.query().players.names)
            for p in n-o: print(f'{p} serverga kirdi')
            for p in o-n: print(f'{p} serverdan chiqdi')
            o=n
        except Exception as e: logging.error(e)
        except KeyboardInterrupt: return