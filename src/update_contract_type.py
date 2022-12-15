
import psycopg2
from configparser import ConfigParser
from sys import argv
# from src.getContracts import getContracts
import pprint
import requests
import json
from src.find_721 import find721
from src.find_1155 import find1155
from src.curl_721 import dataPath
from src.curl_721 import projectPath
class PostgreSQLPipeline(object):

    def normal_add(self, db_creds):
        conn = psycopg2.connect(database=db_creds['DB_NAME'], user=db_creds['USER'],
                                password=db_creds['PASSWORD'], host=db_creds['HOST'], port=db_creds['PORT'])
        try:
            cur = conn.cursor()
            # self.conn.query(sql_desc)
            #cur.execute("INSERT INTO ewrrw values(dict(item));")
            print("begin INSERT")
            cur.execute("""INSERT INTO gamefi_contract_collection
                (chain, contract_address, protocol_slug,)
                VALUES(%s, %s, %s);""",
                        ('BNB Chain',
                            '0x0627578d5d388e6ea417080461303af575d3eba2',
                            'mobox',
                         ),)
            conn.commit()

            print("Data added to PostgreSQL database!")

        except Exception:
            print('insert record into table failed')
            print(Exception)

    def process_items(self, db_creds, items):
        # sql_desc="INSERT INTO table_name(xxx, yyy)values(item['xxx'],item['yyy'])"
        conn = psycopg2.connect(database=db_creds['DB_NAME'], user=db_creds['USER'],
                                password=db_creds['PASSWORD'], host=db_creds['HOST'], port=db_creds['PORT'])
        try:
            cur = conn.cursor()
            # self.conn.query(sql_desc)
            #cur.execute("INSERT INTO ewrrw values(dict(item));")
            print("begin INSERT")
            for item in items:
                cur.execute("""INSERT INTO gamefi_contract_collection
                    (chain, contract_address, protocol_slug,)
                    VALUES(%s, %s, %s);""",
                            (item['chain'],
                             item['contract_address'],
                                item['protocol_slug'],
                             ),)
            conn.commit()

            print("Data added to PostgreSQL database!")

        except Exception:
            print('insert record into table failed')
            print(Exception)

        finally:
            if cur:
                cur.close()
        conn.close()
        return item
    
    def update_test(self, db_creds, type, addr):
        conn = psycopg2.connect(database=db_creds['DB_NAME'], user=db_creds['USER'],
                                password=db_creds['PASSWORD'], host=db_creds['HOST'], port=db_creds['PORT'])
        cur = conn.cursor()
        update_sql = "UPDATE gamefi_contract_collection SET contract_type='{t}' WHERE contract_address='{a}'".format(
                t=type, a=addr)
        print("begin UPDATE")
        cur.execute(update_sql)   
        conn.commit()
        print("Data added to PostgreSQL database!")     
        cur.close()
        conn.close()
        
    def update_contract_type(self, db_creds, type, addr):
        conn = psycopg2.connect(database=db_creds['DB_NAME'], user=db_creds['USER'],
                                password=db_creds['PASSWORD'], host=db_creds['HOST'], port=db_creds['PORT'])
        try:
            cur = conn.cursor()
            update_sql = "UPDATE gamefi_contract_collection SET contract_type='{t}' WHERE contract_address='{a}'".format(
                t=type, a=addr)
            insert_sql = "insert into gamefi_contract_collection (chain, contract_address, protocol_slug,contract_type) VALUES({c}, {a}, {s},{t})".format(
                c="BNB Chain", a=addr, s="", t=type)

            # self.conn.query(sql_desc)
            print("begin UPDATE")
            cur.execute(update_sql)
            if cur.rowcount == 0:  # 如果影响的行数为0，则表中没有满足条件的记录，则写入该行
                cur.execute(insert_sql)
            conn.commit()
            print("Data added to PostgreSQL database!")
        except Exception:
            print('update record into table failed')
            # print(Exception)
        finally:
            if cur:
                cur.close()
        conn.close()
    
    def readRecordDB(self, db_creds):
        conn = psycopg2.connect(database=db_creds['DB_NAME'], user=db_creds['USER'],
                                password=db_creds['PASSWORD'], host=db_creds['HOST'], port=db_creds['PORT'])
        try:
            cur = conn.cursor()
            print("begin FETCH TABLE")
            select_sql = "select * from gamefi_contract_collection"  # 从表格table中读取全表内容
            cur.execute(select_sql)  # 执行该sql语句
            List = cur.fetchall()

        except Exception:
            print('insert record into table failed')
            print(Exception)
        finally:
            cur.close()
            conn.close()
        
        return List


    # read DB to return the all gamefi contract addresses list
    def readAddressesFromDB(self, db_creds):
        conn = psycopg2.connect(database=db_creds['DB_NAME'], user=db_creds['USER'],
                                password=db_creds['PASSWORD'], host=db_creds['HOST'], port=db_creds['PORT'])
        try:
            cur = conn.cursor()
            print("begin FETCH TABLE")
            select_sql = "select contract_address from gamefi_contract_collection"  # 从表格table中读取全表内容
            cur.execute(select_sql)  # 执行该sql语句
            contractList = cur.fetchall()

        except Exception:
            print('insert record into table failed')
            print(Exception)
        finally:
            cur.close()
            conn.close()
        
        return contractList

    def checkTokenTypeFromApi(self, contract):
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
            action="tokensupply",
            contractaddress=contract,
            apikey="VUD9T6GQGXRGSJNMUMAAYVBJGY55DVHRUF"
        )
        response = requests.get(url, headers=headers)

        data = json.loads(response.text)
        # print("PROJECT Contract:", contract)
        pprint.pprint(data)
        result = int(data['result'])
        if (result > 0):
            print("是 ERC20 token! ")
            # update the db record
            self.update_contract_type(
                db_creds=self.db_creds, type='erc20', addr=contract)
    

    def checkTokenTypeFromHTML(self, contractAddress):
        web = projectPath + dataPath + contractAddress + ".html"
        try:
            if(find721(web)):
                # 写成721 ,上传到
                print(contractAddress+"是erc721, 开始update")
                self.update_contract_type(db_creds=self.db_creds,type='erc721',addr=contractAddress)
                print("update完成")
            if(find1155(web)):
                # 写成1155
                print(contractAddress+"是erc1155")
                self.update_contract_type(db_creds=self.db_creds,type='erc1155',addr=contractAddress)
                print("update完成")
            else:
                print("不是erc721或erc1155")
        except TimeoutError:
            print('time out error')
            exit()


    def readConfig(self, arg):
        # Read and parse configurations
        config = ConfigParser()  # 解析config
        #  Read argumentations
        try:
            config.read(f'config/{arg}.conf')  # dev configuration

            self.config = config
            self.db_creds=config['DB_CREDS']
            # pprint.pprint(config['DB_CREDS'])
        except IndexError:
            print(
                "Command should be of type: python <start file> <config name>. Example: python main.py local")
            print("Example: python3 main.py dev 'slug'")
            print("dev for dev database")
            print("slug for the project protocol")
            exit()


if __name__ == '__main__':
    # config = ConfigParser()  # 解析config
    # #  Read argumentations
    # try:
    #     config.read(f'config/{argv[1]}.conf')  # dev configuration

    #     pprint.pprint(config['DB_CREDS'])
    # except IndexError:
    #     print("Command should be of type: python <start file> <config name>. Example: python main.py local")
    #     print("Example: python3 main.py dev 'slug'")
    #     print("dev for dev database")
    #     print("slug for the project protocol")
    #     exit()

    pgsqlPipeline = PostgreSQLPipeline()
    pgsqlPipeline.readConfig(argv[1])
    config = pgsqlPipeline.config
    # pprint.pprint(config)
    db_creds = config['DB_CREDS']
    # Get the contracts list
    contractList = pgsqlPipeline.readAddressesFromDB(db_creds)


    
    for con in contractList:
        realCon = con[0]
        print(realCon)
        pgsqlPipeline.checkTokenTypeFromApi(realCon)
