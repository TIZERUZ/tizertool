from plugins.common import *
from os import getlogin
import shutil
import requests
import subprocess

def pkgmngr():
    if shutil.which('apt'):
        return 1
    elif shutil.which('dnf'):
        return 2
    elif shutil.which('pacman'):
        return 3
    else: return None

def node():
    print('Downloading nodeJS')

    if os.name == 'nt':
        os.system('winget install OpenJS.NodeJS')
        time.sleep(2)
        logging.info("O'rnatilyapti mineflayer, express")
        subprocess.run(fr'"C:\Program Files/nodejs/npm.cmd" install mineflayer express socks', shell=True)


    elif os.name == 'posix':
        pm = pkgmngr()
        if pm == 1:
            os.system('sudo apt update')
            os.system('sudo apt install nodejs npm')
            os.system('node -v')
            os.system('npm -v')
            os.system('npm install mineflayer express socks')

        if pm == 2:
            os.system('sudo dnf update')
            os.system('sudo dnf install nodejs npm')
            os.system('node -v')
            os.system('npm -v')
            os.system('npm install mineflayer express socks')

        if pm == 3:
            os.system('sudo pacman -S nodejs npm')
            os.system('node -v')
            os.system('npm -v')
            os.system('npm install mineflayer express socks')

def velocity():
    logging.info('Downloading Velocity [PaperMC]')

    r = requests.get("https://api.papermc.io/v2/projects/velocity").json()
    v, b = r["versions"][-1], requests.get(f"https://api.papermc.io/v2/projects/velocity/versions/{r['versions'][-1]}").json()["builds"][-1]
    url = f"https://api.papermc.io/v2/projects/velocity/versions/{v}/builds/{b}/downloads/velocity-{v}-{b}.jar"
    jar = requests.get(url).content

    os.makedirs('./proxy/velocity/', exist_ok=True)
    with open('./proxy/velocity/velocity.jar', 'wb') as f: f.write(jar)
    logging.success(f'Yuklandi velocity-{v}-{b}.jar')

    logging.info('FakeProksi Sozlanmoqda')
    os.makedirs('./proxy/fakeproxy/plugins/', exist_ok=True)

    with open('./proxy/fakeproxy/velocity.jar', 'wb') as f: f.write(jar)
    fp = requests.get("https://github.com/Renovsk/Plantain/releases/download/fp-1/plantain-fakeproxy-1.0.jar").content
    with open('./proxy/fakeproxy/plugins/plantain-fakeproxy-1.0.jar', 'wb') as f: f.write(fp)

    logging.success('Done downloading plantain-fakeproxy-1.0.jar')
    time.sleep(1)
def upd(): # this is prob retarded way to do it ik
    node()
    velocity()

def initialize():
    if firstload() == True:
        print(fr'''{red}
 /$$$$$$$$/$$                                     /$$$$$$$$                  /$$
|__  $$__/__/                                    |__  $$__/                 | $$
   | $$   /$$ /$$$$$$$$  /$$$$$$   /$$$$$$          | $$  /$$$$$$   /$$$$$$ | $$ {getstring('inithello')} {white}{getlogin()}{red},
   | $$  | $$|____ /$$/ /$$__  $$ /$$__  $$         | $$ /$$__  $$ /$$__  $$| $$ {getstring('initmsg')}
   | $$  | $$   /$$$$/ | $$$$$$$$| $$  \__/         | $$| $$  \ $$| $$  \ $$| $$
   | $$  | $$  /$$__/  | $$_____/| $$               | $$| $$  | $$| $$  | $$| $$
   | $$  | $$ /$$$$$$$$|  $$$$$$$| $$               | $$|  $$$$$$/|  $$$$$$/| $$
   |__/  |__/|________/ \_______/|__/               |__/ \______/  \______/ |__/
                                                                                
                                                                                
                                                                                
        ''')
        node()
        velocity()
        animate()
        loadmenu()

    elif firstload() == False: animate(); loadmenu()
    