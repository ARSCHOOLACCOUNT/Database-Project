from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/result")
def result():
    modelName = request.args.get("modelName", "")
    releaseYear = request.args.get("releaseYear", "")
    basePrice = request.args.get("basePrice", "")
    return render_template("result.html", modelName=modelName, releaseYear=releaseYear, basePrice=basePrice)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)