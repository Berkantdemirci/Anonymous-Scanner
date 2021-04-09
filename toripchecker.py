import requests

def ip():
    url = "https://check.torproject.org/api/ip"
    response = requests.get(url)
    tor_check = response.json()["IsTor"]
    tor_ip = response.json()["IP"]
    print(f"Tor Check : {tor_check}\nIP : {tor_ip}")
    
ip()