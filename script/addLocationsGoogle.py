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

def getGeometry(text):
    conf = config.getData()
    queryArray = {
        'key': conf['google']['key'],
        'query': text
    }

    data = curl.getJson(conf['google']['placeUrl'], queryArray)
    try:
        return data['results'][0]['geometry']['location']
    except:
        return []


if __name__ == '__main__':
    dbManager = DBManager();
    cursor = dbManager.getCursor();

    selectSql = "SELECT keyword FROM keywords WHERE type = 'LOCATION'"
    cursor.execute(selectSql)
    rows = cursor.fetchall()

    for row in rows:
        print(row[0])
        checkDb = DBManager();
        checkCurosr = checkDb.getCursor();
        checkSql = "SELECT keyword FROM locations WHERE keyword = '" + row[0] + "'"
        checkCurosr.execute(checkSql)

        if checkCurosr.rowcount == 0:
            try:
                geometry = getGeometry(row[0])
                print(geometry)
                if geometry != []:
                    insDb = DBManager();
                    insCurosr = insDb.getCursor();
                    insertSql = "INSERT IGNORE INTO locations (keyword, geometry) VALUES (%s, ST_GeomFromText('POINT(%s %s)'))"
                    insCurosr.execute(insertSql, (row[0], geometry['lat'], geometry['lng']))
                    insDb.finish();
                    print('added')
            except:
                print(sys.exc_info())
                pass
        checkDb.finish();
    dbManager.finish();
