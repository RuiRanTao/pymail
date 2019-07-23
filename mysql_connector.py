# import mysql.connector
import MySQLdb

mydb = MySQLdb.connect(
    host="127.0.0.1",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="990526", # 数据库密码
    database="test",
    charset='utf8'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM MyGuests WHERE id >0")

myresult = mycursor.fetchall()  # fetchall() 获取所有记录

for x in myresult:
    print(x)