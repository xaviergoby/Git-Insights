import requests

headers = {
	'Content-Type': 'application/json',
	'X-API-Key': 'af581641c58641b69ca8f9dbd6d19cbe',
}

json_data = {
	'address': '5CNChyk2fnVgVSZDLAVVFb4QBTMGm6WfuQvseBG6hj8xWzKP',
}

response = requests.post('https://alephzero.api.subscan.io/api/scan/account/tokens', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
# data = '{\n    "address": "5CNChyk2fnVgVSZDLAVVFb4QBTMGm6WfuQvseBG6hj8xWzKP"\n  }'
# response = requests.post('https://alephzero.api.subscan.io/api/scan/account/tokens', headers=headers, data=data)

json_response = response.json()
print(f"JSON Response: {json_response}")


def reformatted_balance(balance, decimals):
	if len(balance) == decimals:
		reformatted_balance = f"0.{balance}"
		return reformatted_balance
	else:
		reformatted_balance = f"{balance[:len(balance) - decimals]}.{balance[-decimals:]}"
		return reformatted_balance


wallet_balance = json_response["data"]["native"][0]["balance"]
balance = reformatted_balance(wallet_balance, 12)

print(f"Wallet Balance: {wallet_balance} NEAR")
print(f"Balance: {balance} NEAR")




# LOCAL_RPC = "http://localhost:9933"
# addr = LOCAL_RPC

# json_data = {"jsonrpc":"2.0", "id":"1", "method":"system_unstable_networkState", "params":[]}

# r = requests.post(addr, json={"jsonrpc":"2.0","id":"1","method":"system_unstable_networkState","params":[]})


# curl -H "Content-Type: application/json" -d '{"id":1, "jsonrpc":"2.0", "method": "state_getStorage",
# "params":[
# "0x26aa394eea5630e07c48ae0c9558cef7b99d880ec681799c0cf30e8886371da95e0bd5326aa7e9fa72c036a33d96d381a60e515cdbf7e1426e9d708bc78ee0ed7d0f4c5c04951be09e37e70ad31a487c"]}'
# https://westend-rpc.polkadot.io


# https://polkadot.js.org/apps/?rpc=wss%3A%2F%2Ftest-api.alephzero.org#/explorer






# addr_param_str = '{"address":"5Dbtx5f9ez7jvHdWZ6YTWT6UmBagifJNRoDphUNk6USUHdcj"}'
# addr_dict = json.loads(addr_param_str)
# addr = addr_dict["address"]
