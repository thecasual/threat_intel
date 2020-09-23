import requests

# SHODAN will attempt to resolve the address and give back data

def run(config, search):
    
    apikey = config['token']

    # Assume IP for now
    #url = f"https://urlscan.io/api/v1/search/?q=ip:{search}"
    #https://api.shodan.io/shodan/host/{ip}?key={YOUR_API_KEY}
    url = f"https://api.shodan.io/shodan/host/{search}?key={apikey}"

    #headers = {
    #    "API-Key" : apikey
    #}

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()