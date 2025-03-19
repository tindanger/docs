from fastapi import FastAPI, HTTPException
from typing import Dict
import json
import os

app = FastAPI()

# 获取当前文件所在目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 产品信息文件目录
PRODUCTS_DIR = os.path.join(BASE_DIR, "api-reference", "products")

# 读取产品信息
def load_product(product_code: str) -> Dict:
    try:
        # 使用相对路径
        product_file = os.path.join(PRODUCTS_DIR, f"{product_code}.json")
        with open(product_file, 'r', encoding='utf-8') as f:
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
        product_file = os.path.join(PRODUCTS_DIR, f"{product_code}.json")
        with open(product_file, 'w', encoding='utf-8') as f:
            json.dump(product_data, f, ensure_ascii=False, indent=2)
        return {
            "code": 200,
            "message": "更新成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))