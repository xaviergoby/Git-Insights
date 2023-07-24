from urllib import parse
import json
import requests


# https://api.bscscan.com/api
#    ?module=account
#    &action=balance
#    &address=0x70F657164e5b75689b64B7fd1fA275F334f28e18
#    &apikey=YourApiKeyToken

# api_key = "163FIZ7ZGX2RKRUVFAM4C2RQBMZ8NHPY1G" # My ACTUAL TRUE API KEY
api_key = "163FIZ7ZGX2RKRUVFAM4C2RQBMZ8NHPY1H"

# address = "0x8b6C8fd93d6F4CeA42Bbb345DBc6F0DFdb5bEc73"
address = "0x8b6C8fd93$&€£d6F4CeA42Bbb345DBc6F0DFdb50000**"

# Mainnet Endpoint URL: https://api.bscscan.com/
# Test#1: api?module=account&action=balance&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a&tag=latest&apikey=YourApiKeyToken


# https://api.bscscan.com/api?module=account&action=balance&address=0x8b6C8fd93d6F4CeA42Bbb345DBc6F0DFdb5bEc73&tag=latest&apikey=163FIZ7ZGX2RKRUVFAM4C2RQBMZ8NHPY1G

params = {"module":"account", "action":"balance", "address":address, "tag":"latest", "apikey":api_key}

api_base_url = "https://api.bscscan.com/api"
response = requests.get(api_base_url, params=params)

res = response.json()


print(f"Response content:\n{response.content}\n\n\nJSON format response:\n{res}")



# api_base_url = "https://api.bscscan.com/api"
api_base_url = "https://api.bscscan.com"

path_url = f"/api?{parse.urlencode(params)}"
print(f"url_path:{path_url}")


url = f"{api_base_url}{path_url}"
url_split = parse.urlsplit(url)

print(f"URL:\n{url}\n")
print(f"URL Split:\n{url_split}\n")

requests.get()
