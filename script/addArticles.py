import os
import sys
sys.path.append(os.getcwd())

import csv
from datetime import datetime
from model.dbmanager import DBManager
from model import config

def insertData(fileName, mediaName):
    f = open(fileName, "r")
    reader = csv.reader(f, delimiter = '\t')
    header = next(reader)

    dbManager = DBManager();
    cursor = dbManager.getCursor();

    for row in reader:
        if '夕刊' in row[2]:
            hour = '17:00'
        else:
            hour = '5:00'
        date = datetime.strptime(row[1] + ' ' + hour, '%Y/%m/%d %H:%M')
        title = row[0].strip(' ')
        sql = "INSERT IGNORE INTO articles (title, media_name, published_at) VALUES (%s, %s, %s)"
        cursor.execute(sql, (title, mediaName, date))

    f.close()
    dbManager.finish();

if __name__ == '__main__':
    config = config.getData()

    for data in config['datafile']:
        insertData(data['path'], data['media_name'])
