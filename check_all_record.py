from sys import argv
from src.update_contract_type import PostgreSQLPipeline
import pprint
from src.curl_721 import curl_web
from src.curl_721 import dataPath
from src.curl_721 import projectPath
from src.find_1155 import find1155
from src.find_721 import find721


# 读取每一个已获取的bscscan的网页，找到721/1155的关键信息，标识类型 
if __name__ == '__main__':
    pgsqlObject = PostgreSQLPipeline()

    pgsqlObject.readConfig('dev')
    config = pgsqlObject.config
    db_creds = config['DB_CREDS']
    recordList = pgsqlObject.readRecordDB(db_creds)
    size = len(recordList)
    print("合约地址数量： ", size)
    for i in range(size):

        record = recordList[i]
        contractAddress = record[1]
        # print(recordList[i])
        # print(recordList)
        print("处理第{now}/{total}个合约: {addr}".format(now=i,
              total=size, addr=contractAddress))
        if (record[0] != 'BNB Chain'):
            print(contractAddress+"不是BNB Chain项目")
            continue
        if (record[3] == 'erc20'):
            print(contractAddress+"已判断是erc20")
            continue
        print("当前获取网页合约地址:"+contractAddress)
        # curl_web(contractAddress)  # 获得contract的web到/data目录下
        # 根据获取的html直接判断类型，然后累计10个之后更新信息
        # pgsqlObject.checkTokenTypeFromHTML(contractAddress)
