import requests

# Urlscan will attempt to resolve the address and give back data

def run(config, search):
    
    apikey = config['token']

    # Assume IP for now
    url = f"https://urlscan.io/api/v1/search/?q=ip:{search}"

    headers = {
        "API-Key" : apikey
    }

    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        return r.json()