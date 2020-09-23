import requests
def run(config, search):
    
    apikey = config['token']
    # Assume IP for now

    url =  f"https://www.virustotal.com/api/v3/ip_addresses/{search}"

    headers = {
        "x-apikey" : apikey
    }

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r.json()