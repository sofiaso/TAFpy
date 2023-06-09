from pydantic import BaseModel, validator, Field

class Category(BaseModel):
    id: int
    name: str

class Tags(BaseModel):
    id: int
    name: str

class PET(BaseModel):
    id: int = Field(le=10)
    category: Category
    name: str
    photoUrls: list[str]
    tags: list[Tags]
    status: str

    #@validator("id")
    #def check_id(cls, v):
    #    if v != 2987:
    #        raise ValueError("id is bigger then two")
    #    else:
    #        return v

PET_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "number"},
        "category": {
            "type": "object",
            "properties":{
                "id": {"type": "number"},
                "name": {"type": "string"},
            }
        },
        "name": {"type": "string"},
        "photoUrls": {
            "type": "array",
            "properties": {
            }
        },
        "tags": {
            "type": "array",
            "properties": {
                "id": {"type": "number"},
                "name": {"type": "string"}
            }
        },
        "status": {"type": "string"}
    },
    "required": ["id"]
}