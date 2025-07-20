from plugins.common import *
import json
import os

default = {
    "language": "english",
    "theme": "banana",
    "server": {
        "port": 23457,
        "randomize_port": False
    }
}

# languages = ["arabic", "chinese", "czech", "english", "french", "german", "hindi", "japanese", "korean", "russian", "spanish", "turkish"]
languages = ["english"]
themes = ["banana", "charcoal", "lily", "sunset", "snow"]

def edit(tf, value=None):
    global default
    if not os.path.exists("config.json"): logging.error("Config fayl mavjud emas"); return
    with open("config.json", 'r', encoding='utf-8') as f: config = json.load(f)

    keys = tf.split('.')
    ohio = default
    for k in keys:
        if not isinstance(ohio, dict) or k not in ohio: logging.error(f"Kalitda Xatolik: {'.'.join(keys)}") ;return
        ohio = ohio[k]

    d = config
    for k in keys[:-1]:
        if not isinstance(d, dict) or k not in d: logging.error(f"Xato Kalit: {'.'.join(keys)}"); return
        d = d[k]
    
    final_key = keys[-1]
    if value is None:
        if tf == "language": logging.info(f"Til uchun qiymatlar: {white}{','.join(languages)}"); return
        elif tf == "theme": logging.info(f"Mavzu uchun qiymatlar: {white}{','.join(themes)}"); return
    
    if isinstance(d.get(final_key), bool) and isinstance(value, str):
        if value.lower() in ['true', '1', 'yes']: value = True
        elif value.lower() in ['false', '0', 'no']: value = False
    elif isinstance(d.get(final_key), int):
        try: value = int(value)
        except ValueError: logging.error("Qiymat raqam bo'lishi kerak"); return

    d[final_key] = value
    with open('config.json', 'w', encoding='utf-8') as f: json.dump(config, f, indent=2)
    logging.success(f"{tf} = {value}")