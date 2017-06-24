import MySQLdb
import json



# DATABASE_NAME='mysql'
# HOST='594d02b639e4a.gz.cdb.myqcloud.com'
# PORT='8470'
# USER_NAME='cdb_outerroot'
# PASSWD='w85685216'
# CHAR_SET='utf8'

DATABASE_NAME='family'
HOST='localhost'
USER_NAME='root'
PASSWD='123456789'
CHAR_SET='utf8'

class mysql:
    def __init__(self):
        self.con=MySQLdb.connect(host=HOST,user=USER_NAME,passwd=PASSWD,db=DATABASE_NAME,charset=CHAR_SET)
        self.cursor=self.con.cursor()

    def __del__(self):
        if self.con!=None:
            self.con.close()
        if self.cursor!=None:
            self.cursor.close()

    def execute(self,sql,params=''):
        try:
            if params=='':
                ret=self.cursor.execute(sql)
            else:
                ret=self.cursor.execute(sql,params)
            self.con.commit()
            return ret
        except Exception:
            self.con.rollback()
            raise Exception("sql excute error")

    def create_table(self,sqltable):
        try:
            self.cursor.execute(sqltable)
        except Exception:
            raise Exception("create table error")

    def fetchall(self):
        return self.cursor.fetchall()

    def insert_table(self,sql,params):
         self.execute(sql,params)
         #self.con.commit()

    def query_table(self,table_name):
        if table_name!='':
            sql='select * from '+table_name
            self.execute(sql)
            for row in self.cursor.fetchall():
                print(row)

    def isExist(self,sql):
        return self.execute(sql)


'''db=mysql()

sql='insert into link_user(user,passwd) values(%s,%s)'
params=('lkk','kkkkk')
##db.create_table(sqlTable)
##result=db.insert_table(sql,params)

params1='lkk'
sql1="select * from link_user where user='%s'"%(params1)

cur=db.isExist(sql1)
result=db.fetchall()

for row in result:
    print(row)

#db.query_table('link_user')'''







