from fastapi import FastAPI
app=FastAPI(title="DeliveryBridge")
@app.get("/")
def home():
    return { 
         "message": "DeliveryBridge is running!","staus": "online"}
