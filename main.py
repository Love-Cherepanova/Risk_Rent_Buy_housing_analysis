from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
  price: float
  rent: float
  risk: float

@app.post("/predict")
def predict(data: InputData):
  score = data.price / (data.rent + 1) - data.risk
  return {"score": score}




#Add FastAPI main.py
      
