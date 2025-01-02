def phone(number):
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone
    try:
        phones = phonenumbers.parse(number)
        if phonenumbers.is_valid_number(phones):
            print(f"Phone Number: {number}")
            print(f"Country: {geocoder.description_for_number(phones, 'en')}")
            print(f"Carrier: {carrier.name_for_number(phones, 'en')}")
            print(f"Time Zones: {timezone.time_zones_for_number(phones)}")
            print(f"International Format: {phonenumbers.format_number(phones, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        else:
            print(f"The number {number} is not valid.")
    except phonenumbers.phonenumberutil.NumberParseException as e:
        print(f"Error parsing the number: {e}")
def ipscan(ip, fast=False):
    import requests
    import socket
    from concurrent.futures import ThreadPoolExecutor

    def resolveip(domain):
        try:
            socket.inet_aton(domain)
            return domain
        except socket.error:
            return socket.gethostbyname(domain)

    def portscan(ipaddress, port):
        try:
            with socket.create_connection((ipaddress, port), timeout=1):
                return True
        except (socket.timeout, socket.error):
            return False

    def scanports(ipaddress):
        ports = range(1, 65536)
        with ThreadPoolExecutor(max_workers=100) as executor:
            results = executor.map(lambda port: portscan(ipaddress, port), ports)
        openports = [port for port, is_open in zip(ports, results) if is_open]
        if openports:
            print(f"Open ports on {ipaddress}: {openports}")
        else:
            print(f"No open ports found for {ipaddress}.")

    ipaddress = resolveip(ip)
    url = f"https://ipinfo.io/{ipaddress}/json"
    try:
        response = requests.get(url)
        data = response.json()
        print(f"\nIP Information for {ipaddress}:")
        print(f"IP: {data.get('ip', 'N/A')}")
        print(f"Location: {data.get('postal', 'N/A')}, {data.get('city', 'N/A')}, {data.get('region', 'N/A')}, {data.get('country', 'N/A')}")
        print(f"Organization/ISP: {data.get('org', 'N/A')}")
        print(f"Geolocation: {data.get('loc', 'N/A')}")
        print(f"Hostname: {data.get('hostname', 'N/A')}")
        print(f"Timezone: {data.get('timezone', 'N/A')}")
        if not fast:
            scanports(ipaddress)
    except requests.exceptions.RequestException as e:
        print(f"\nError with the request: {e}")
    except socket.gaierror:
        print(f"\nUnable to resolve domain or IP: {ip}")
def creditcard(card):
    import requests

    def luhn(cardnumber):
        total = 0
        reverse = cardnumber[::-1]
        for i, digit in enumerate(reverse):
            n = int(digit)
            if i % 2 == 1:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return total % 10 == 0

    if not luhn(card):
        print(f"\nInvalid card number: {card} (Luhn check failed).")
        return
    bin = card[:6]
    url = f"https://lookup.binlist.net/{bin}"
    headers = {"Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        print(f"\nCredit Card: {card}")
        print(f"Type: {data.get('scheme', 'N/A')}")
        print(f"Brand: {data.get('brand', 'N/A')}")
        print(f"Card Type: {data.get('type', 'N/A')}")
        print(f"Card Issuer: {data.get('bank', {}).get('name', 'N/A')}")
        print(f"Country: {data.get('country', {}).get('name', 'N/A')}")
        print(f"Currency: {data.get('country', {}).get('currency', 'N/A')}")
        print(f"Card Issuer Website: {data.get('bank', {}).get('url', 'N/A')}")
    except requests.exceptions.RequestException as e:
        print(f"\nError making request: {e}")
def email(email):
    import re
    import dns.resolver

    def validemailformat(email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    if not validemailformat(email):
        print(f"Invalid email format: {email}")
        return
    domain = email.split('@')[1]
    try:
        dns.resolver.resolve(domain, 'MX')
        print(f"\nEmail Information for {email}:")
        print(f"Domain: {domain}")
        print(f"Mail Server Found: Yes (MX records found)")
        print(f"Validity: Valid domain with mail server")
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        print(f"\nCould not retrieve information for email {email}.")
        print(f"Domain: {domain} does not have a valid mail server (MX record missing).")
def vinscan(vin):
    import requests
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVin/{vin}?format=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(f"\nFull response for VIN {vin}:\n")
            for item in data.get('Results', []):
                for key, value in item.items():
                    print(f"{key}: {value}")
        else:
            print(f"\nError: Unable to retrieve data. HTTP Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"\nError during the request: {e}")
def isin(isin):
    import re
    pattern = r'^[A-Z]{2}[A-Z0-9]{9}[0-9]$'
    if not re.match(pattern, isin):
        print("Invalid ISIN format.")
        return
    country = isin[:2]
    security = isin[2:11]
    checksum = isin[11]
    print(f"ISIN Information:")
    print(f"  ISIN: {isin}")
    print(f"  Country Code: {country}")
    print(f"  Security Identifier: {security}")
    print(f"  Checksum: {checksum}")
def isbn(isbn):
    import re
    isbn13 = r'^\d{13}$'
    isbn10 = r'^\d{9}[0-9X]$'
    if re.match(isbn13, isbn):
        print(f"ISBN-13 Information: {isbn}")
        print(f"  Book Group: {isbn[:3]}")
        print(f"  Publisher: {isbn[3:6]}")
        print(f"  Item Number: {isbn[6:12]}")
        print(f"  Checksum: {isbn[12]}")
    elif re.match(isbn10, isbn):
        print(f"ISBN-10 Information: {isbn}")
        print(f"  Identifier: {isbn[:9]}")
        print(f"  Checksum: {isbn[9]}")
    else:
        print("Invalid ISBN format.")