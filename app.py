from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Home"


@app.route("/food")
def food():
    return "Yummy!"


@app.route("/food/pizza")
def pizza():
    return "Pepperoni Please!"


if __name__ == "__main__":
    app.run(debug=True)
