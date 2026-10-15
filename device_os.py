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

def printRows(query, values=()):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute(query, values)
    for row in cursor.fetchall():
        print(*row, sep=" | ")
    connection.close()
    print()

def printDevices():
    print("deviceID | modelName | releaseYear | basePrice")
    printRows("select deviceID, modelName, releaseYear, basePrice from Device")

def printOperatingSystems():
    print("osID | osName | versionNumber | Developer")
    printRows("select * from Operating_System")

def printOSesForDevice(deviceID):
    print("osID | osName | versionNumber | Developer")
    printRows("select Operating_System.* from Operating_System "
              "join Device_OS on Operating_System.osID = Device_OS.osID "
              "where Device_OS.deviceID = %s", (deviceID,))

def printDevicesForOS(osID):
    print("deviceID | modelName | releaseYear | basePrice")
    printRows("select Device.deviceID, modelName, releaseYear, basePrice from Device "
              "join Device_OS on Device.deviceID = Device_OS.deviceID "
              "where Device_OS.osID = %s", (osID,))

def addOSToDevice():
    printDevices()
    deviceID = input("deviceID: ")
    printOperatingSystems()
    osID = input("osID to add: ")
    connection = getConnection()
    cursor = connection.cursor()
    try:
        cursor.execute("insert into Device_OS (deviceID, osID) values (%s, %s)", (deviceID, osID))
        connection.commit()
        print("Added.\n")
    except mysql.connector.Error:
        print("Could not add (bad ID or already added).\n")
    connection.close()

def removeOSFromDevice():
    printDevices()
    deviceID = input("deviceID: ")
    printOSesForDevice(deviceID)
    osID = input("osID to remove: ")
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("delete from Device_OS where deviceID=%s and osID=%s", (deviceID, osID))
    connection.commit()
    if cursor.rowcount == 0:
        print("That device does not run that OS.\n")
    else:
        print("Removed.\n")
    connection.close()

menuText = """Please select one of the following options:
1) Print Devices
2) Print Operating Systems
3) Print Operating Systems a device runs
4) Print Devices running an operating system
5) Add an operating system to a device
6) Remove an operating system from a device
q) Quit
"""

if __name__ == "__main__":
    option = "1"
    while option != 'q':
        option = input(menuText)
        if option == "1":
            printDevices()
        elif option == "2":
            printOperatingSystems()
        elif option == "3":
            printDevices()
            printOSesForDevice(input("deviceID: "))
        elif option == "4":
            printOperatingSystems()
            printDevicesForOS(input("osID: "))
        elif option == "5":
            addOSToDevice()
        elif option == "6":
            removeOSFromDevice()