import json
import logging
import sqlite3
from typing import Union

from pydantic import ValidationError
import uvicorn
from fastapi import FastAPI, Depends, Request

from actions import *
from models import Features, query_model

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
cursor: sqlite3.Cursor


@app.lifespan("startup")
def get_or_create_db():
    global cursor
    cursor = get_sql_cursor()
    init_db(cursor=cursor)










@app.post("/features")
async def write_features(features: Features) -> Features:    
    return features




@app.post("/features/raw")
async def write_features(r: Request) -> Features | str:
    req_body = await r.body()
    body_dict = json.loads(req_body)
    try:
        features = Features(**body_dict)
    except ValidationError as e:
        return f"Failed input validation. {e}"
    
    return features



    # write_features_to_db(features=features, cursor=cursor)
    
    
    
    
    
    
    
    
    
    
    
    


@app.get("/features")
def get_features(params: query_model = Depends()) -> Union[Features, str]:
    query_dict = params.dict()
    features = get_feature_by_id(cursor=cursor, id=query_dict.get("row_number"))
    return features


if __name__ == "__main__":
    uvicorn.run(app, port=8080)