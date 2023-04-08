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
            schema.parse_obj(self.json)
            print(self.json)
        return self

    def assert_status_code(self, status_code):
        assert self.status == status_code, "Invalid status_code = " + str(self.status)
        return self