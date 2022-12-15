from src.update_contract_type import PostgreSQLPipeline

if __name__ == '__main__':
    pgsqlObject = PostgreSQLPipeline()

    pgsqlObject.readConfig('dev')
    config = pgsqlObject.config
    db_creds = config['DB_CREDS']
    pgsqlObject.update_test(
        db_creds, "erc666", "0x0627578d5d388e6ea417080461303af575d3eba2")
