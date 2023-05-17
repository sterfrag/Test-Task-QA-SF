# -*- coding: utf-8 -*-
"""
Created on Sun May 14 19:36:46 2023

@author: Stelios
"""
import random
import pytest
from fastapi.testclient import TestClient
from api_server import app
import requests
import json
import random



ENDPOINT="http://localhost:8080/orders"
response = requests.get(ENDPOINT)
print (response)
client = TestClient(app)
with open('Dummy_DB.json','r') as f:
    list_of_orders = json.load(f)

#dummy order id that is going to be used for testing purposes
ordnum =random.randint(20,100)

def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert response.json() == {'A list of orders': {'detail': 'Retrieve all orders',
                      'headers': None,
                      'status_code': 200},'List of orders': list_of_orders}

def test_place_order_positive():

    payload = {
        "ord_id": ordnum,
        "Owner": "John",
        "Details": "Order details"
    }
    response = client.post("/orders", json=payload)
    assert response.status_code == 201
    assert response.json() == {'detail': f'Order with OrdId:{ordnum} has been placed'}

def test_place_order_duplicate_id():
    payload = {
        "ord_id": 1,
        "Owner": "Jane",
        "Details": "Duplicate order ID"
    }
    response = client.post("/orders", json=payload)
    assert response.status_code == 200
    assert response.json() == {'detail': 'Invalid Input', 'headers': None, 'status_code': 400}

def test_place_order_missing_field():
    payload = {
        "ord_id": 2,
        "Details": "Missing owner field"
    }
    response = client.post("/orders", json=payload)
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "loc": [
                    "body",
                    "Owner"
                ],
                "msg": "field required",
                "type": "value_error.missing"
            }
        ]
    }

def test_get_order():
    # Here test a valid number that can be found
    response = client.get(f"/orders/{ordnum}")
    assert response.status_code == 200
    assert response.json() == {"Details": "Order details","Owner": "John", "ord_id": ordnum}

def test_get_order_not_found():
    # Here test an invalid number that cannot be found
    response = client.get("/orders/999")
    assert response.status_code == 404
    assert response.json() == {'detail':"Order not found"}

def test_delete_order():
    #delete the order that was created previously

    response = client.delete(f"/orders/{ordnum}")

    if response.status_code == 204 :
    # status code 204 does not return a body and that is why
    # it is not checked
        assert response.status_code == 204
        pass
    else:
        assert response.status_code == 200
        assert response.json() == {"Details": "Order details","Owner": "John", "ord_id": ordnum}

def test_delete_order_not_found():
    # use the same order id that was deleted previously to show the correct status code
    # and the correct response
    response = client.delete(f"/orders/{ordnum}")
    assert response.status_code == 404
    assert response.json() == {'detail':"Order not found"}
