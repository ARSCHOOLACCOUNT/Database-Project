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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)