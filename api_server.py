# -*- coding: utf-8 -*-
"""
Created on Sat May 13 10:02:41 2023

@author: Stelios
"""

from fastapi import FastAPI, HTTPException
import random
from pydantic import BaseModel
from typing import Optional
import json
import asyncio
import uvicorn


print("Now creating api and establishing connection to server")

app = FastAPI(title="Forex Trading Platform API", \
              description="A RESTful API to simulate a Forex trading platform with WebSocket support for real-time order updates.", \
              version="1.0.0")

class orderlist(BaseModel):
    ord_id: Optional[int] = None
    Owner: str
    Details: str

with open('Dummy_DB.json','r') as f:
    list_of_orders = json.load(f)

#create array with only ids to avoid double entry 
only_ids=[]

for i in list_of_orders:
    only_ids.append(i['ord_id'])

#print(only_ids)
     
def random_delay():
    return random.uniform(0.1, 1.0)


@app.get('/orders',summary="Retrieve all orders",  \
         responses={200:{'description':'A list of orders'}})

async def get_orders():

    await asyncio.sleep(random_delay())  # Simulating aynchronous delay
    # Logic to retrieve and return all orders

    return {'List of orders': list_of_orders,'A list of orders':HTTPException(status_code=200,detail="Retrieve all orders")}
    

@app.post('/orders',summary="Place a new order",  \
         responses={201:{'description':'Order placed'}, \
                    400:{'description':'Invalid input'}})

async def place_order(order: orderlist):

    await asyncio.sleep(random_delay())  # Simulating aynchronous delay

    new_order = {
        "ord_id":order.ord_id,
        "Owner":order.Owner,
        "Details":order.Details
        }
           
    if order.ord_id not in only_ids:
    
        with open('Dummy_DB.json','w') as f:
            list_of_orders.append(new_order)
            json.dump(list_of_orders,f)
        
        #add the new value to the only_ids column to prevent double entry
        only_ids.append(order.ord_id)
        raise HTTPException(status_code=201, detail=f"Order with OrdId:{order.ord_id} has been placed")
        #return {"Order ID:":order.ord_id}
    else:
        return (HTTPException(status_code=400,detail="Invalid Input"))
    
       
@app.get('/orders/{orderId}',summary="Retrieve a specific order",  \
         responses={200:{'description':'Order found'},
                    404:{'description':'Order not found'}})

async def get_order(orderId: int):

    await asyncio.sleep(random_delay())  # Simulating aynchronous delay
    # Logic to retrieve and return all orders
    order_request = [o for o in list_of_orders if o['ord_id']==orderId]
    if len(order_request)>0:
        return order_request[0]
    else:
        raise HTTPException(status_code=404, detail="Order not found")


@app.delete('/orders/{orderId}',summary="Cancel an order", \
         responses={204:{'description':'Order canceled'}, \
                    404:{'description':'Order not found'}})

async def delete_order(orderId: int):
    
    order = [p for p in list_of_orders if p['ord_id']==orderId]
    if len(order)>0:
        list_of_orders.remove(order[0])
        with open('Dummy_DB.json','w') as f:
            json.dump(list_of_orders,f)

        raise HTTPException(status_code=204,detail='Order is canceled')
    else:
        raise HTTPException(status_code=404,detail='Order not found')
    return

if __name__ == "__main__":
    uvicorn.run("api_server:app", host="localhost", port=8080, log_level="info")