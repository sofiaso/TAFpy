import pytest
from base.generators.order import Order

@pytest.fixture()
def order_generator():
    return Order()
