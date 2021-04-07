from flask import Flask


def test_index(app, client):
    res = client.get("/")
    assert res.status_code == 200


def test_food(app, client):
    res = client.get("/food")
    assert res.status_code == 200


def test_pizza(app, client):
    res = client.get("/food/pizza")
    assert res.status_code == 200


def test_404(app, client):
    res = client.get("/food/burgers")
    assert res.status_code == 404
