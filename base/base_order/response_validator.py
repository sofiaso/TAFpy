import base.base_order.schemas as schemas
from jsonschema import validate
class Validator:
    def __init__(self, response):
        self.response = response
        self.status_code = response.status_code
        self.json = response.json()

    def validation_by_status(self, status):
        assert self.status_code == status, f"Invalid status code: {self.status_code}"
        return self

    def validation_by_json_pydantic(self):
        schemas.Order.parse_obj(self.json)
        return self

    def validation_by_json_schemas(self):
        validate(self.json, schemas.ORDER)
        return self

    def __str__(self):
        return (
            f"json:\n{self.json}\nstatus code:{self.status_code}"
        )