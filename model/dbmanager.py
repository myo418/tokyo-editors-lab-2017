import MySQLdb
from . import config

class DBManager:
    def __init__(self):
        conf = config.getData()
        mysqlConf = conf['mysql']
        self.connection = MySQLdb.connect(
            host=mysqlConf['host'],
            db=mysqlConf['db'],
            user=mysqlConf['user'],
            passwd=mysqlConf['password']
        )
        self.cursor = self.connection.cursor()

    def getCursor(self):
        return self.cursor

    def finish(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()
