import pytest
from base.generators.pet import Pet

@pytest.fixture
def say_hello(autouse=True):
    print("Hello, tests are running")

def _calculate(a, b):
    return a + b

@pytest.fixture
def calculate():
    return _calculate

@pytest.fixture()
def make_number():
    print("set up running")
    yield 14
    print("tear down running")

@pytest.fixture()
def pet_generator():
    return Pet()
