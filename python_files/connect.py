import mysql.connector
mydb = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='www',
    password='140865Ar!@',
    db='sakila'
)
# interact with the database here

mycursor = mydb.cursor()
mycursor.execute("select * from device limit 10")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)




mydb.close()
