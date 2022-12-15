#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psycopg2
from configparser import ConfigParser
from sys import argv
from src.getContracts import getContracts
from src.gamefi_protocol_to_pgsql import PostgreSQLPipeline

if __name__ == "__main__":
    
    # app.run('0.0.0.0', 8090, threaded=True, debug=True)
    
     # Read and parse configurations
    config = ConfigParser()  # 解析config
    try:
        config.read(f'config/{argv[1]}.conf')  # dev configuration
        db_creds = config['DB_CREDS']
        apikeys = config['APIKEYS']
    except IndexError:
        print("Command should be of type: python <start file> <config name>. Example: python main.py local")
        exit()
    
    # Get the contracts list from json file

    pgsqlPipeline = PostgreSQLPipeline()
    print("----------------------------------------------")
    pgsqlPipeline.check_version(db_creds=db_creds)
    print("----------------------------------------------")
    infopen = open('./clean_protocol_slugs.txt', 'r', encoding="utf-8")
    slugs = infopen.readlines()
    i = 0
    for slug in slugs:
        i+=1
        if i<int(argv[2]):
            continue
        slug = slug[:-1]
        print("Start Get No.",i," slug: ",slug)
        num = 'KEY'+argv[3]
        print(num)
        key = apikeys[num]
        print(key)
        contracts = getContracts(slug=slug,apiKey=key) # input the apikey number
        if(contracts=="already found"):
            print("已经获取过当前项目"+slug)
            continue # 跳过当前已经成功过的一条
        if(len(contracts)==0):
            f=open("errorlog.txt",'a',encoding='utf-8')
            f.write(slug+'\n')
            f.close()
            continue
        pgsqlPipeline.process_items(db_creds=db_creds, items=contracts)
    
    print("----------------------------------------------")