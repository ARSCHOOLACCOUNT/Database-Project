#!/usr/bin/env python3
import mysql.connector, os
from dotenv import load_dotenv
load_dotenv()

def getConnection():
    return mysql.connector.connect(
        host=os.getenv('SQL_HOST'),
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PWD'),
        db=os.getenv('SQL_DB')
    )

def printTable():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from Manufacturer")
    result = cursor.fetchone()
    print("manufacturerID | companyName | Country | yearFounded")
    while result is not None:
        print(result)
        result = cursor.fetchone()
    connection.close()
    print()

def insertIntoTable():
    companyName = input("Company name: ")
    country = input("Country: ")
    yearFounded = input("Year founded: ")
    connection = getConnection()
    cursor = connection.cursor()
    query = "insert into Manufacturer (companyName, Country, yearFounded) values (%s, %s, %s);"
    cursor.execute(query, (companyName, country, yearFounded))
    connection.commit()
    connection.close()
    print("Inserted.\n")

def updateRow():
    manufacturerID = input("manufacturerID of the row to update: ")
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select * from Manufacturer where manufacturerID=%s", (manufacturerID,))
    current = cursor.fetchone()
    if current is None:
        print("No row with that ID.\n")
        connection.close()
        return
    print(f"Current value: {current}")
    companyName = input("New company name: ")
    country = input("New country: ")
    yearFounded = input("New year founded: ")
    cursor.execute(
        "update Manufacturer set companyName=%s, Country=%s, yearFounded=%s where manufacturerID=%s",
        (companyName, country, yearFounded, manufacturerID)
    )
    connection.commit()
    connection.close()
    print("Updated.\n")

def deleteRowFromTable():
    manufacturerID = input("manufacturerID of the row to delete: ")
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("delete from Manufacturer where manufacturerID=%s", (manufacturerID,))
    connection.commit()
    connection.close()
    print("Deleted.\n")

menuText = """Please select one of the following options:
1) Display contents of table
2) Insert new row to table
3) Update a row of the table
4) Delete a row of the table
q) Quit
"""

if __name__ == "__main__":
    option = "1"
    while option != 'q':
        option = input(menuText)
        if option == "1":
            printTable()
        elif option == "2":
            insertIntoTable()
        elif option == "3":
            updateRow()
        elif option == "4":
            deleteRowFromTable()
