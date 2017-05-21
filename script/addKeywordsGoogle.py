import os
import sys
sys.path.append(os.getcwd())

import time
from model.dbmanager import DBManager
from model import curl
from model import config
from io import BytesIO
import pycurl
import urllib
import urllib.parse
import json
import argparse

import googleapiclient.discovery

def getEntity(text):
    try:
        body = {
            'document': {
                'type': 'PLAIN_TEXT',
                'language': 'ja',
                'content': text,
            },
            'encoding_type': 'UTF8',
        }

        service = googleapiclient.discovery.build('language', 'v1')
        request = service.documents().analyzeEntities(body=body)
        response = request.execute()
        return response['entities']
    except:
        print(sys.exc_info())
        return[]


if __name__ == '__main__':
    dbManager = DBManager();
    cursor = dbManager.getCursor();

    selectSql = 'SELECT id, title FROM articles'
    cursor.execute(selectSql)
    rows = cursor.fetchall()

    for row in rows:
        print(row[0])
        checkDb = DBManager();
        checkCurosr = checkDb.getCursor();
        checkSql = "SELECT keyword FROM keywords WHERE article_id = " + str(row[0])
        checkCurosr.execute(checkSql)

        if checkCurosr.rowcount == 0:
            insDb = DBManager();
            insCurosr = insDb.getCursor();
            print('title is: ' + row[1])
            entities = getEntity(row[1])

            for entity in entities:
                try:
                    print(entity['name'] + ':' + entity['type'])
                    insertSql = "INSERT IGNORE INTO keywords (article_id, keyword, type) VALUES (%s, %s, %s)"
                    insCurosr.execute(insertSql, (row[0], entity['name'], entity['type']))
                except:
                    print(sys.exc_info())
                    pass
            insDb.finish();
        checkDb.finish()
    dbManager.finish();
