from enum import Enum


class MyEnum(Enum):
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
