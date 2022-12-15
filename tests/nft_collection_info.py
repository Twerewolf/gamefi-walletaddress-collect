import requests
import json
from sys import argv
offset = argv[1]
url = "https://api.footprint.network/api/v2/nft/collection/info?chain=BNB%20Chain&offset={o}".format(
    o=str(offset)
)

headers = {
    "accept": "application/json",
    "API-KEY": "8IGN2Qtu01++R5xnomtFFmCBUFrgXfnDMKuhmn4n+ng2HQHkNL40cXAvSDKti9T7"
}

response = requests.get(url, headers=headers)

# print(response.text)
data = json.loads(response.text)
f = open('./res-nft-collection-info-{o}.json'.format(o=offset),'w',encoding='utf-8')
json.dump(data,f) # 写入
f.close()
print("写入结束")