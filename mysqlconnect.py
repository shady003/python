import mysql.connector
dbs = mysql.connector.connect(host='localhost', user='root', passwd='root')
mydb = dbs.cursor()
mydb.execute("show databases")
result = mydb.fetchall() # fetchone()
for i in result:
    print(i)
