from pydantic import BaseModel

class Order(BaseModel):
    id: int
    petId: int
    quantity: int
    shipDate: str
    status: str
    complete: bool

ORDER = {
    "type": "object",
    "properties":{
        "id": {"type": "number"},
        "petId": {"type": "number"},
        "quantity": {"type": "number"},
        "shipDate": {"type": "string"},
        "status": {"type": "string"},
        "complete": {"type": "bool"}
    },
    "required": ["id", "petId", "quantity", "shipDate", "status", "complete"]
}