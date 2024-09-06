import pymysql
 
# 打开数据库连接
db = pymysql.connect(host="localhost", user="test", password="test", database="SRS")
 
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
 
# SQL插入语句
sql = """INSERT INTO STUDENT(s_name, s_tel) VALUES (%s, %s)"""
values = ('张三', '15664322132')

try:
   # 执行sql语句
   cursor.execute(sql, values)
   # 提交到数据库执行
   db.commit()
except Exception as e:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()