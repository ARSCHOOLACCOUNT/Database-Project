import mysql.connector

mydb = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='www',
    password='140865Ar!@'
)
cursor = mydb.cursor()
cursor.execute("SHOW DATABASES")
for row in cursor:
    print(row)
mydb.close()
