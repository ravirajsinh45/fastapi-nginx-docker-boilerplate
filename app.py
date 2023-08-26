import os, sys
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

import warnings
warnings.filterwarnings("ignore")


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



## Home endpoint
@app.get("/")
async def home():
    return {"message:": "docker deploy test!!"}





if __name__=="__main__":
    uvicorn.run("app:app",host="127.0.0.1",port=8080, reload=True, workers=1)