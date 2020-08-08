from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_googlemaps import GoogleMaps, Map
from Realtorapi import get_realtor_data, get_csv_data, set_markers
from webscraping import coastcapital
app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = "AIzaSyBgk4xlA90gmaW-itRDlPgokqU5SgETb4k"
GoogleMaps(app)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/map")
def mapview():
    map_data = get_realtor_data()
    map_markers = set_markers(map_data)
    mymap = Map(
        identifier="mymap",
        lat=49.0305287,
        lng=-122.80,
        zoom=12,
        markers=map_markers,
    )
    return render_template('map.html', flask_gmap=mymap)


@app.route("/apidata")
def api():
    data = get_realtor_data()
    return jsonify(data)


@app.route("/csvdata")
def csv():
    csvdata = get_csv_data('data/property-sample.csv')
    return jsonify(csvdata)


@app.route("/scraper")
def scraper():
    html = coastcapital()
    return render_template("scraper.html", data = html)


if __name__ == '__main__':
    app.run(debug=True)