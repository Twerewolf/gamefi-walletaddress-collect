import requests

url = "https://api.footprint.network/api/v2/nft/collection/transfers?chain=BNB%20Chain&collection_contract_address=0xed8711fEff83b446158259981FD97645856e82A5"

headers = {
    "accept": "application/json",
    "API-KEY": "8IGN2Qtu01++R5xnomtFFmCBUFrgXfnDMKuhmn4n+ng2HQHkNL40cXAvSDKti9T7"
}

response = requests.get(url, headers=headers)

print(response.text)