import json
from dataclasses import asdict, dataclass, field
from typing import List

@dataclass
class Tag:
    id: int
    name: str

@dataclass
class Item:
    name: str
    price: float
    description: str = field(default=None)
    tags: List[Tag] = field(default_factory=list())

# from JSON
item_json = '{"name": "Widget", "description": "A fancy widget.", "price": 15.99, "tags": [{"id": 1, "name": "fancy"}, {"id": 2, "name": "widget"}]}'
item_dict = json.loads(item_json)

item_model = Item(
    name=item_dict["name"], 
    price=item_dict["price"], 
    description=item_dict["description"], 
    tags=[Tag(id=tag["id"], name=tag["name"]) for tag in item_dict["tags"]]
)
print(item_model)

# To JSON
print(json.dumps(asdict(item_model)))