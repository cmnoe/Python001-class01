# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'root',
    'db' : 'douban'
}

sql = """CREATE TABLE shorts (
    id  INT PRIMARY KEY AUTO_INCREMENT,
    user CHAR(255),
    star INT(6),
    content CHAR(255)
)ENGINE=innodb DEFAULT CHARSET=utf8;"""

class ConnDB(object):
    def __init__(self):
        self.host = dbInfo['host']
        self.port = dbInfo['port']
        self.user = dbInfo['user']
        self.password = dbInfo['password']
        self.db = dbInfo['db']
        self.conn = None

    # self.run()
    def run(self, sql):
        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.db
        )
        # 游标建立的时候就开启了一个隐形的事务
        cur = self.conn.cursor()
        try:
            # for command in self.sqls:
            cur.execute(sql)
            # 关闭游标
            cur.close()
            self.conn.commit()
        except:
            self.conn.rollback()

    # 插入数据到数据库
    def insert(self, value):
        cur = self.conn.cursor("")
        try:
            sql = """INSERT INTO shorts (user, star, content) VALUES(%s, %s, %s)"""
            cur.execute(sql, value)
            cur.close()
            self.conn.commit()
        except:
            self.conn.rollback()


    # 关闭数据库连接
    def close(self):
        self.conn.close()

    


class ShortsPipeline:
    def __init__(self):
        self.db = ConnDB()

    def process_item(self, item, spider):
        self.db.insert((item['user'], int(item['star']), item['content']))
        return item
    
    def open_spider(self, spider):
        self.db.run(sql)

    def close_spider(self, spider):
        self.db.close()
