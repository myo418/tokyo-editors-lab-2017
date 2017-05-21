import os
import sys
sys.path.append(os.getcwd())

import time
from model.dbmanager import DBManager
from model import curl
from model import config

def getLocations(text):
    conf = config.getData()
    queryArray = {
        'app_id': conf['goo']['app_id'],
        'sentence': text,
        'class_filter': 'LOC'
    }

    data = curl.postJson(conf['goo']['entityUrl'], queryArray)
    try:
        return data['ne_list']
    except:
        return []

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

    selectSql = 'SELECT id, title FROM articles'
    cursor.execute(selectSql)

    for row in cursor:
        insDb = DBManager();
        insCurosr = insDb.getCursor();
        time.sleep(1)
        print('title is: ' + row[1])
        locations = getLocations(row[1])
        for location in locations:
            geometry = getGeometry(location[0])
            print('location is: ')
            print(location[0])
            print('geometry is: ')
            print(geometry)

            if geometry != []:
                insertSql = "INSERT IGNORE INTO locations (article_id, word, geometry) VALUES (%s, %s, ST_GeomFromText('POINT(%s %s)'))"
                insCurosr.execute(insertSql, (row[0], location[0], geometry['lat'], geometry['lng']))
        
        insDb.finish();

    dbManager.finish();
