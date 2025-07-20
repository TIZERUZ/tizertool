from mcrcon import MCRcon
from plugins.common import *

def rcon(server, password):
    if checkserver(server) == False: logging.error('Iltimos, Real domen kiriting:'); return
    try:
        with MCRcon(server, password) as mcr:
            logging.info(f'Chiqish uchun "chiqish" deb yozing')
            while True:
               rcmd = input(f'{red}/')
               if rcmd == 'chiqish': mcr.disconnect(); return False
               resp = mcr.command(f"{rcmd}")
               print(resp)

    except Exception as e:
        print(e)