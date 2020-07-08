from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/about")
def about():
    return "This is about me page"

@app.route("/contact")
def contact():
    return "This is Contact Us page"

if __name__ == '__main__':
    app.run(debug=True)