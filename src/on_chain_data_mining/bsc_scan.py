import requests
from urllib import parse


class BscScan:

    def __init__(self, api_key):
        self.api_url = "https://api.bscscan.com"
        self.api_key = api_key
        self.decimals = 18

    def reformatted_balance(self, balance):
        """
        :param balance: e.g. '291656700132769807210'
        :type balance: str
        :return:
        :rtype:
        """
        if len(balance) == self.decimals:
            reformatted_balance = f"0.{balance}"
            return reformatted_balance
        else:
            reformatted_balance = f"{balance[:len(balance)-self.decimals]}.{balance[-self.decimals:]}"
            return reformatted_balance


    def get_wallet_bnb_balance(self, wallet_address, reformtted=False):
        """
        (Request) URL = API Endpoint URL + "Path URL"
        E.g.: API Endpoint URL = "https://api.bscscan.com"
        E.g.: Path URL = "/api?module=account&action=balance&address=0x8b6C8fd93%24%26%E2%82%AC%C2%A3d6F4CeA42Bbb345DBc6F0DFdb50000%2A%2A&tag=latest&apikey=163FIZ7ZGX2RKRUVFAM4C2RQBMZ8NHPY1H"
        # path_url = f"/api?module={params['module']}&action={params['action']}" \
        #            f"&address={params['address']}&tag={params['tag']}" \
        #            f"&tag={params['tag']}&apikey={params['apikey']}"
        :param wallet_address: e.g. "0x8b6C8fd93d6F4CeA42Bbb345DBc6F0DFdb5bEc73"
        https://bscscan.com/address/0x8b6c8fd93d6f4cea42bbb345dbc6f0dfdb5bec73
        e.g. "0x16091bFd5Eedc2E6292713246cd9e8188867B8Ff"
        https://bscscan.com/address/0x16091bfd5eedc2e6292713246cd9e8188867b8ff
        :type wallet_address: str
        :return: {'status': '1', 'message': 'OK', 'result': <bnb_balance>}
        where e.g. <bnb_balance> = (0.)'387063987548714447' (BNB)
        :rtype:dict
        """
        params = {"module": "account", "action": "balance", "address": wallet_address, "tag": "latest", "apikey": self.api_key}
        path_url = f"/api?{parse.urlencode(params)}"
        url = f"{self.api_url}{path_url}"
        response_obj = requests.get(url)
        if response_obj.status_code != 200:
            print(f"API GET request returned response with status code: {response_obj.status_code}")
            return response_obj
        else:
            # response_obj = requests.get(self.api_url, params=params)
            json_response = response_obj.json()
            wallet_balance = json_response["result"]
            if reformtted is False:
                return wallet_balance
            else:
                return self.reformatted_balance(wallet_balance)


if __name__ == "__main__":
    api_key = "163FIZ7ZGX2RKRUVFAM4C2RQBMZ8NHPY1G"
    bsc_scan = BscScan(api_key)

    wallet_address1 = "0x8b6C8fd93d6F4CeA42Bbb345DBc6F0DFdb5bEc73"
    wallet_address2 = "0x16091bFd5Eedc2E6292713246cd9e8188867B8Ff"
    wallet_address3 = "0xD6B231e41548Cb3D953ffA1cBeB52278F640382B"
    # wallet_balance = bsc_scan.get_wallet_bnb_balance(wallet_address)
    wallet_balance1 = bsc_scan.get_wallet_bnb_balance(wallet_address1, reformtted=True)
    wallet_balance2 = bsc_scan.get_wallet_bnb_balance(wallet_address2, reformtted=True)
    wallet_balance3 = bsc_scan.get_wallet_bnb_balance(wallet_address3, reformtted=True)

    print(f"Wallet BNB Balance= {wallet_balance1} BNB")
    print(f"Wallet BNB Balance= {wallet_balance2} BNB")
    print(f"Wallet BNB Balance= {wallet_balance3} BNB")



