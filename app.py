from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from src.textSummarizer.pipeline.prediction import PredictionPipeline

app = FastAPI()

@app.get("/")
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        raise e
    
@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        summary = obj.predict(text)
        return summary
    except Exception as e: 
        raise e 
    

if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8000)
        


