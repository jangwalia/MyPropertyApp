from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from Realtorapi import get_realtor_data

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/apidata")
def api():
    data = get_realtor_data()
    return jsonify(data)

@app.route("/csvdata")
def csv():
    return render_template('csv.html')



if __name__ == '__main__':
    app.run(debug=True)