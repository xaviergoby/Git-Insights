import requests
import urllib
from urllib import parse


def get_etherscan_last_price(price_rounding=2):
	# https://api.etherscan.io/api?module=stats&action=ethprice&apikey=YourApiKeyToken
	base_url = "https://api.etherscan.io"
	module = "stats"
	action = "ethprice"
	# chborg_address = "0x5770815B0c2a09A43C9E5AEcb7e2f3886075B605"
	# tag = "latest"
	apikey = "V9QFCNC64ICJ98T1YP8WFVDDYGWZFVATUA"
	# params = {"module": module, "action": action, "address": chborg_address, "tag": tag, "apikey": apikey}
	params = {"module": module, "action": action, "apikey": apikey}
	url = f"{base_url}/api?{urllib.parse.urlencode(params)}"
	response = requests.get(url)
	# print(f"response.request.url: {response.request.url}")
	# print(response.json())
	price = float(response.json()["result"]["ethusd"])
	if price_rounding != False:
		return round(price, price_rounding)
	else:
		return price



def reformatted_balance(balance, decimals):
	if len(balance) == decimals:
		reformatted_balance = f"0.{balance}"
		return reformatted_balance
	else:
		reformatted_balance = f"{balance[:len(balance) - decimals]}.{balance[-decimals:]}"
		return reformatted_balance
