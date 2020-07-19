from flask import Flask, render_template
from flask_bootstrap import Bootstrap

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
    return render_template('api.html')

@app.route("/csvdata")
def csv():
    return render_template('csv.html')

if __name__ == '__main__':
    app.run(debug=True)