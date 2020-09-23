import requests

# SANS will attempt to resolve the address + domain and give back data

def run(config, search):
    
    #apikey = config['token']

    # Assume IP for now
    #url = f"https://urlscan.io/api/v1/search/?q=ip:{search}"
    url = f"http://isc.sans.edu/api/ip/{search}?json"

    #headers = {
    #    "API-Key" : apikey
    #}

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()