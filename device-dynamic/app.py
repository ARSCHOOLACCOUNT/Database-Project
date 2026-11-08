from flask import Flask, render_template, request, redirect
import mysql.connector, os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

def getConnection():
    return mysql.connector.connect(
        host=os.getenv('SQL_HOST'),
        user=os.getenv('SQL_USER'),
        password=os.getenv('SQL_PWD'),
        db=os.getenv('SQL_DB')
    )

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/result")
def result():
    connection = getConnection()
    cursor = connection.cursor()
    modelName = request.args.get("modelName")
    if modelName:
        query = "insert into Device (modelName, releaseYear, basePrice) values (%s, %s, %s)"
        cursor.execute(query, (modelName, request.args.get("releaseYear"), request.args.get("basePrice")))
        connection.commit()
        connection.close()
        return redirect("/result")  # avoids re-insert
    cursor.execute("select deviceID, modelName, releaseYear, basePrice from Device")
    rows = cursor.fetchall()
    connection.close()
    return render_template("result.html", rows=rows)

@app.route("/edit/<deviceID>")
def edit(deviceID):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select deviceID, modelName, releaseYear, basePrice from Device where deviceID=%s", (deviceID,))
    device = cursor.fetchone()
    connection.close()
    return render_template("edit.html", device=device)

@app.route("/update")
def update():
    connection = getConnection()
    cursor = connection.cursor()
    query = "update Device set modelName=%s, releaseYear=%s, basePrice=%s where deviceID=%s"
    cursor.execute(query, (request.args.get("modelName"), request.args.get("releaseYear"), request.args.get("basePrice"), request.args.get("deviceID")))
    connection.commit()
    connection.close()
    return redirect("/result")

@app.route("/delete/<deviceID>")
def delete(deviceID):
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("delete from Device where deviceID=%s", (deviceID,))
    connection.commit()
    connection.close()
    return redirect("/result")

@app.route("/devices")

def devices():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select deviceID, modelName from Device")
    rows = cursor.fetchall()
    connection.close()
    return render_template("devices.html", rows=rows)

@app.route("/device_os")
def device_os():
    deviceID = request.args.get("deviceID")
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select modelName from Device where deviceID = %s", (deviceID,))
    device = cursor.fetchone()
    cursor.execute(
        "select osName, versionNumber, Developer from Operating_System "
        "join Device_OS on Operating_System.osID = Device_OS.osID "
        "where Device_OS.deviceID = %s", (deviceID,)
    )
    rows = cursor.fetchall()
    connection.close()
    return render_template("device_os.html", device=device, rows=rows)

@app.route("/os")
def os_list():
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select osID, osName, versionNumber from Operating_System")
    rows = cursor.fetchall()
    connection.close()
    return render_template("os.html", rows=rows)

@app.route("/os_devices")
def os_devices():
    osID = request.args.get("osID")
    connection = getConnection()
    cursor = connection.cursor()
    cursor.execute("select osName, versionNumber from Operating_System where osID = %s", (osID,))
    os_row = cursor.fetchone()
    cursor.execute(
        "select modelName, releaseYear, basePrice from Device "
        "join Device_OS on Device.deviceID = Device_OS.deviceID "
        "where Device_OS.osID = %s", (osID,)
    )
    rows = cursor.fetchall()
    connection.close()
    return render_template("os_devices.html", os_row=os_row, rows=rows)

@app.route("/add_os")
def add_os():
    deviceID = request.args.get("deviceID")
    osID = request.args.get("osID")
    connection = getConnection()
    cursor = connection.cursor()
    if deviceID and osID:
        cursor.execute("insert into Device_OS (deviceID, osID) values (%s, %s)", (deviceID, osID))
        connection.commit()
        connection.close()
        return redirect("/device_os?deviceID=" + deviceID)
    cursor.execute("select deviceID, modelName from Device")
    deviceRows = cursor.fetchall()
    cursor.execute("select osID, osName, versionNumber from Operating_System")
    osRows = cursor.fetchall()
    connection.close()
    return render_template("add_os.html", devices=deviceRows, oses=osRows)

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)