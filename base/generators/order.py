

class Order:
    result = {}

    def __int__(self):
        self.result = {}

    def set_id(self, id=0):
        self.result['id'] = id
        return self

    def set_pet_id(self, pet_id=0):
        self.result['petId'] = pet_id
        return self

    def set_quantity(self, quantity=0):
        self.result['quantity'] = quantity
        return self

    def set_shipDate(self, shipDate="01.01.2000"):
        self.result['shipDate'] = shipDate
        return self

    def set_status(self, status="unknown"):
        self.result['status'] = status
        return self

    def set_complete(self, complete=False):
        self.result['complete'] = complete
        return self

    def get(self):
        self.set_id()
        self.set_pet_id()
        self.set_quantity()
        self.set_shipDate()
        self.set_status()
        self.set_complete()
        return self.result

    def build(self):
        return self.result
