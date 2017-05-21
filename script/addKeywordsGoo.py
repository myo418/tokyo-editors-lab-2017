import os
import sys
sys.path.append(os.getcwd())

from model.dbmanager import DBManager
from model import curl

def getMorph(text):
    url = 'https://labs.goo.ne.jp/api/morph'
    queryArray = {
        'app_id': '42c7d6eb5e74d80f1d361cd1c6df9aa30c74983ec8118a0519bbba7030f9e534',
        'sentence': text,
        'pos_filter': '名詞'
    }
    data = curl.getJson(url, queryArray)
    print(data)
    try:
        return data['word_list'][0]
    except:
        return []

if __name__ == '__main__':
    dbManager = DBManager();
    cursor = dbManager.getCursor();

    selectSql = 'SELECT article_id, title, body FROM article limit 3'
    cursor.execute(selectSql)  # select文を実行

    for row in cursor:
        print(row[1])
        words = getMorph(row[1])

        for word in words:
            print(word)
            insertSql = "INSERT IGNORE INTO word_goo (article_id, word) VALUES (%s,%s)"
            cursor.execute(insertSql, (row[0], word[0]))

    dbManager.finish();
