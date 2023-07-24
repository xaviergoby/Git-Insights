import requests
import json
from urllib import parse

url = "https://rpc.mainnet.near.org/"


# https://www.nearscan.org/accounts/ovcharov.near


payload = json.dumps({
	"jsonrpc": "2.0",
	"id": "dontcare",
	"method": "query",
	"params": {
		"request_type": "view_account",
		"finality": "final",
		"account_id": "ovcharov.near"
	}
})
headers = {
	'Content-Type': 'application/json'
}

# response = requests.request("POST", url, headers=headers, data=payload)

response_obj = requests.post(url, headers=headers, data=payload)
json_response = response_obj.json()


print(f"JSON Response: {json_response}")


def reformatted_balance(balance, decimals):
	if len(balance) == decimals:
		reformatted_balance = f"0.{balance}"
		return reformatted_balance
	else:
		reformatted_balance = f"{balance[:len(balance) - decimals]}.{balance[-decimals:]}"
		return reformatted_balance

wallet_balance = json_response["result"]["amount"]
balance = reformatted_balance(wallet_balance, 24)

print(f"Balance: {balance} NEAR")




# ####
test_base_url = "https://rpc.mainnet.near.org"
# test_params = json.loads(response_obj.request.body)
test_params = {"jsonrpc": "2.0", "id": "dontcare", "method": "query", "params": {"request_type": "view_account", "finality": "final", "account_id": "ovcharov.near"}}
# test_encoded_url = f"/api?{parse.urlencode(test_params)}"
test_encoded_url = f"/?{parse.urlencode(test_params)}"
# test_encoded_url = f"{parse.urlencode(test_params)}"
test_url = f"{test_base_url}{test_encoded_url}"
print(test_url)




