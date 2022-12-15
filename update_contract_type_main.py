from sys import argv
from src.update_contract_type import PostgreSQLPipeline

if __name__ == '__main__':
    pgsqlObject = PostgreSQLPipeline()

    pgsqlObject.readConfig('dev')
    config = pgsqlObject.config
    db_creds = config['DB_CREDS']
    contractList = pgsqlObject.readAddressesFromDB(db_creds)
    # 2128
    size = len(contractList)
    print("合约地址数量： ", size)
    # 输入开始位置
    beginNumber = argv[1]

    for i in range(size):
        if(i<int(beginNumber)):
            continue
        realCon = contractList[i][0]
        
        print("处理第{now}/{total}个合约: {addr}".format(now=i,total=size,addr=realCon))
        pgsqlObject.checkTokenTypeFromApi(realCon)

   