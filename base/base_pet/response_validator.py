from jsonschema import validate

class Response:
    def __init__(self, response):
        self.response = response
        self.json = response.json()
        self.status = response.status_code

    def validation(self, schema):
        if isinstance(self.json, list):
            for item in self.json:
                validate(item, schema)
        else:
            validate(self.json, schema)
        return self

    def validation_pydantic(self, schema):
        if isinstance(self.json, list):
            for item in self.json:
                schema.parse_obj(item)
                print(item)
        else:
            print(self)
            schema.parse_obj(self.json)
        return self

    def assert_status_code(self, status_code):
        assert self.status == status_code, f"Invalid status_code = {self.status}"
        return self

    def __str__(self):
        return (
            f"Response\nstatus code = {self.status}\njson: {self.json}"
        )