
import requests
import json
import pprint


# url = "https://eth-mainnet.g.alchemy.com/v2/docs-demo"

# payload = {
#     "id": 1,
#     "jsonrpc": "2.0",
#     "method": "alchemy_getTokenBalances",
#     "params": ["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"]
# }
# headers = {
#     "accept": "application/json",
#     "content-type": "application/json"
# }

# response = requests.post(url, json=payload, headers=headers)

# print(response.text)

# erc721查询会返回result：0，erc20则会返回supply量

def checkTokenType(contract):
    '''
    https://api.bscscan.com/api
    ?module=stats
    &action=tokenCsupply
    &contractaddress=0xe9e7cea3dedca5984780bafc599bd69add087d56
    &apikey=YourApiKeyToken
    '''
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    url = "https://api.bscscan.com/api?module=stats&action={action}&contractaddress={contractaddress}&apikey={apikey}".format(
        action = "tokensupply",
        contractaddress = contract,
        apikey="VUD9T6GQGXRGSJNMUMAAYVBJGY55DVHRUF"
    )
    response = requests.get(url, headers=headers)

    data = json.loads(response.text)
    print("PROJECT Contract:", contract)
    pprint.pprint(data)


if __name__=='__main__':
    con = "0x07D971C03553011a48E951a53F48632D37652Ba1"
    checkTokenType(con)
    pass