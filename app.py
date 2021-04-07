from flask import Flask

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
<<<<<<< HEAD:app.py
    app.run(host="0.0.0.0")
=======
    app.run(debug=True)
>>>>>>> origin:main.py
