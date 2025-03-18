from fastapi import FastAPI, HTTPException
from typing import Dict
import json

app = FastAPI()

# 读取产品信息
def load_product(product_code: str) -> Dict:
    try:
        with open(f'd:/文档/GitHub/docs/api-reference/products/{product_code}.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="产品不存在")

# API路由
@app.get("/api/products/{product_code}")
async def get_product(product_code: str):
    product = load_product(product_code)
    return {
        "code": 200,
        "message": "success",
        "data": product
    }

@app.post("/api/products")
async def update_product(product_data: Dict):
    try:
        product_code = product_data.get("productCode")
        with open(f'd:/文档/GitHub/docs/api-reference/products/{product_code}.json', 'w', encoding='utf-8') as f:
            json.dump(product_data, f, ensure_ascii=False, indent=2)
        return {
            "code": 200,
            "message": "更新成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))