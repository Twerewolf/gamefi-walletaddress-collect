# 用于获取合约地址的对应bscscan网页页面，保存到/data路径下，用于后续提取标识信息。
# 不仅可用于721，20/1155同样可以直接使用

import requests
import os
projectPath = '/home/tjw/gamefi-walletaddress-collect'
dataPath = "/data/bscscan-token-"
def curl_web(contractAddress):
    # 使用requests库会被检测为robot，使用os库执行curl代替
    url = "https://www.bscscan.com/token/{addr}".format(addr=contractAddress)
    command = "curl " + url + " > "+projectPath+ dataPath+ contractAddress + ".html"

    res = os.system(command)
    print("获取网页结束")
    # response = requests.get(url=url)
    # web = response.text
    # f = open('../data/bscscan-token-{addr}.html'.format(addr=contractAddress),'w',encoding='utf-8')
    # f.write(web)
    # f.close()
    # print("写入结束")
# print(response.text)

if __name__=='__main__':
    curl_web("0x97667aeb10b6916001b5431f980c30fb8a9ce4b4")