import pymysql

dbInfo = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'password' : 'root',
    'db' : 'test'
}

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
            sql = """INSERT INTO FILMS (film_title, film_type, plan_date) VALUES(%s, %s, %s)"""
            cur.execute(sql, value)
            cur.close()
            self.conn.commit()
        except:
            self.conn.rollback()


    # 关闭数据库连接
    def close(self):
        self.conn.close()
    
