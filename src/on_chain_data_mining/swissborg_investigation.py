import requests
import urllib
from urllib import parse
from src.on_chain_data_mining import utils



# SwissBorg "address" Etherscan URL: https://etherscan.io/address/0x5770815b0c2a09a43c9e5aecb7e2f3886075b605
# SwissBorg (Etherscan) "address": 0x5770815B0c2a09A43C9E5AEcb7e2f3886075B605
chborg_address = "0x5770815B0c2a09A43C9E5AEcb7e2f3886075B605"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# How to get Ether balance for a single address with Etherscan API?
# https://algotrading101.com/learn/etherscan-api-guide/#:~:text=following%20article%20headers.-,
# How%20to%20get%20Ether%20balance%20for%20a%20single%20address%20with%20Etherscan%20API%3F,-To%20get%20Ether

# requests.get('https://api.etherscan.io/api?module=account&action=balance&address=0x4976a4a02f38326660d17bf34b431dc6e2eb2327&tag=latest&apikey
# =A1C15S3AXQHQ7PVVDX63VVK2IBAECS448Z').json()

# How to urlencode a querystring in Python?
# https://stackoverflow.com/questions/5607551/how-to-urlencode-a-querystring-in-python

base_url = "https://api.etherscan.io"

module = "account"
action = "balance"
address = chborg_address
tag = "latest"
apikey = "V9QFCNC64ICJ98T1YP8WFVDDYGWZFVATUA"

params = {"module": module, "action": action, "address": address, "tag": tag, "apikey": apikey}

# url = f"https://etherscan.io/token/{chborg_address}"
# encoded_url = f"{base_url}/api?{urllib.parse.urlencode(params)}"
url = f"{base_url}/api?{urllib.parse.urlencode(params)}"
response = requests.get(url)

print(f"response status_code:{response.status_code}")
print(f"response json:\n{response.json()}")
print(f"response result:\n{response.json()['result']}")
# print(f"response result (formatted): {utils.reformatted_balance(response.json()['result'], 18)}")
print(f"\n~~~~~~~~~~~~~~~~~~~~~~")
# res_true_eth_amount = utils.reformatted_balance(response.json()['result'], 18)
res_true_eth_amount = utils.reformatted_balance(response.json()['result'], 18)
res_true_eth_amount_rounded = round(float(res_true_eth_amount), 6)
print(f"CHBorg Etherscan API (acc balance req.) Response: {res_true_eth_amount_rounded} [ETH]")



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

cheth7 = 9219.219727718900036234
cheth6 = 1.873733868680945652
cheth5 = 0.1
cheth4 = 0.128657336533084898
cheth3 = 539.436152713534345836
cheth2 = 0.001895489642394395
cheth1 = 0.000531345844472042
# https://etherscan.io/address/0x5770815b0c2a09a43c9e5aecb7e2f3886075b605
cheth = 29112.5705589961370734

# true_eth_amount = "2911214976106048897441"
# chborg_ethscans_addresses_eth_amount = [cheth1, cheth2, cheth3, cheth4, cheth5, cheth6, cheth7]
chborg_ethscans_addresses_eth_amount = [cheth1, cheth2, cheth3, cheth4, cheth5, cheth6, cheth7, cheth]
# true_eth_amount = str(sum(chborg_ethscans_addresses_eth_amount))
true_eth_amount = str(cheth)
true_eth_amount_fmt_rounded = round(float(true_eth_amount), 6)
print(f"CHBorg Etherscan Address Web Page 'ETH BALANCE': {true_eth_amount_fmt_rounded} [ETH]")

print(f"true - response [ETH]: {true_eth_amount_fmt_rounded} - {res_true_eth_amount_rounded} = {true_eth_amount_fmt_rounded - res_true_eth_amount_rounded}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print(f"\n~~~~~~~~~~~~~~~~~~~~~~")

price = utils.get_etherscan_last_price(price_rounding=2)
print(f"ETH/USD latestprice: ${price}")

res_cheth_usd_val = round(res_true_eth_amount_rounded * price, 2)
print(f"API Response SwissBorg ETH Token Holdings USD val: $ {res_cheth_usd_val}")

true_cheth_usd_val = 55386374.36
print(f"API True (Etherscan) SwissBorg ETH Token Holdings USD val: $ {true_cheth_usd_val}")


print(f"true - response [USD]: ${true_cheth_usd_val} - ${res_cheth_usd_val} = ${true_cheth_usd_val - res_cheth_usd_val}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Can't Import Python3 Requests Module
# https://stackoverflow.com/questions/71074229/cant-import-python3-requests-module


# url = f"https://etherscan.io/token/{chborg_address}"
# page = requests.get(url)
# print(f"\n\n~~~~~~~~~~~~~~~~~~~~~~")
# print(page.text)
