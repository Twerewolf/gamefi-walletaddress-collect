import psycopg2
from configparser import ConfigParser
from sys import argv
# from src.getContracts import getContracts


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


if __name__ == '__main__':
    # Read and parse configurations
    config = ConfigParser()  # 解析config
    #  Read argumentations
    try:
        config.read(f'config/{argv[1]}.conf')  # dev configuration

    except IndexError:
        print("Command should be of type: python <start file> <config name>. Example: python main.py local")
        print("Example: python3 main.py dev 'slug'")
        print("dev for dev database")
        print("slug for the project protocol")
        exit()
    db_creds = config['DB_CREDS']
    # Get the contracts list from json file

    pgsqlPipeline = PostgreSQLPipeline()
    # contracts = getContracts(slug=argv[2])
    pgsqlPipeline.process_items(db_creds=db_creds, items=contracts)
