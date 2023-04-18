import pytest

@pytest.fixture
def say_hello():
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