from pydantic import BaseModel
from typing import List, Optional

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tags: List[str] = []

# from JSON
item_json = '{"name": "Widget", "description": "A fancy widget.", "price": 15.99, "tags": ["fancy", "widget"]}'
item_model = Item.parse_raw(item_json)

print(item_model)
print(item_model.dict())

# to JSON
print(item_model.json())