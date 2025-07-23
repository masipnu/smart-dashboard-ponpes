from flask import Flask, render_template
# import requests
import random

app = Flask(__name__)

@app.route("/")
def index():
    kwh = round(random.uniform(500,1000),2)
    return render_template('index.html', meter=kwh)

if __name__ == "__main__":
    app.run(debug=True, port=80)