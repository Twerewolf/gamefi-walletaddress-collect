import requests

url = "https://api.footprint.network/api/v2/nft/info?chain=BNB%20Chain&collection_contract_address=0xaf1e565cf3bec4a673268b1b4e2c8c6bdd5e43ba"

headers = {
    "accept": "application/json",
    "API-KEY": "8IGN2Qtu01++R5xnomtFFmCBUFrgXfnDMKuhmn4n+ng2HQHkNL40cXAvSDKti9T7"
}

response = requests.get(url, headers=headers)

print(response.text)