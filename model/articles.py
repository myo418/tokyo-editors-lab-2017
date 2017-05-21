import os
from model.dbmanager import DBManager

def getKeywords(location):
    result = []
    print('loc' + location)
    with open(os.path.dirname(__file__)  + '/../sql/selectKeywordsByLocation.sql', 'r') as sqlFile:
        sqltmp = sqlFile.read().replace('\n', ' ')
        dbManager = DBManager()
        cursor = dbManager.getCursor()
        sql = sqltmp % (location,)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

def getKeywordsNum(location, date):
    result = []
    print('loc' + location)
    with open(os.path.dirname(__file__)  + '/../sql/selectKeywordsNumByLocation.sql', 'r') as sqlFile:
        sqltmp = sqlFile.read().replace('\n', ' ')
        dbManager = DBManager()
        cursor = dbManager.getCursor()
        sql = sqltmp % (location, date)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

def getLocations(lat, lng):
    result = []
    with open(os.path.dirname(__file__)  + '/../sql/selectLocationsByGeo.sql', 'r') as sqlFile:
        sql = sqlFile.read().replace('\n', ' ')
        dbManager = DBManager()
        cursor = dbManager.getCursor()
        cursor.execute(sql, (lat, lng))
        result = cursor.fetchall()
    return result

def getArticles(lat, lng, date):
    locations = getLocations(lat, lng);
    data = []
    for location in locations:
        keywordsNum = getKeywordsNum(location[0], date);
        # keywords = getKeywords(location[0]);
        # print(keywordsNum)
        # print()

        if len(keywordsNum) != 0:
            data.append({
                "word": location[0],
                "location": {
                    "lat": location[1],
                    "lng": location[2]
                },
                "data": keywordsNum
            })
    return data

def getArticlesByWord(word):
    result = []
    with open(os.path.dirname(__file__)  + '/../sql/selectArticlesByWord.sql', 'r') as sqlFile:
        sqltmp = sqlFile.read().replace('\n', ' ')
        dbManager = DBManager()
        cursor = dbManager.getCursor()
        sql = sqltmp % (word,)
        cursor.execute(sql)
        result = cursor.fetchall()
    return result
