from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://www.themealdb.com/api/json/v1/1/search.php?s="

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_query = request.form["recipe"]
        response = requests.get(API_URL + search_query)
        data = response.json()

        if data["meals"]:
            return render_template("result.html", recipes=data["meals"])
        else:
            return render_template("index.html", error="Recipe Not Found!")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
