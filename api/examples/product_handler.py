from fastapi import FastAPI, HTTPException
from typing import Dict
import json
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRODUCTS_DIR = os.path.join(BASE_DIR, "api", "schemas")

def load_product(product_code: str) -> Dict:
    try:
        product_file = os.path.join(PRODUCTS_DIR, f"{product_code}.json")
        with open(product_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="产品不存在")

@app.get("/products/{product_code}")
async def get_product(product_code: str):
    product = load_product(product_code)
    return {
        "code": 200,
        "message": "success",
        "data": product
    }