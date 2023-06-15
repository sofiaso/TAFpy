import pytest
import requests
from tests.orders.urls import URL
from base.base_order.response_validator import Validator

@pytest.mark.API
def test_get_order():
    #Arrange
    _order_id = 3
    url = f"{URL}{_order_id}"

    #Act
    r = requests.get(url=url)
    response = Validator(r)

    #Assert
    response.validation_by_status(200).validation_by_json_pydantic()


@pytest.mark.API
def test_put_order(order_generator):
    #Arrange
    print(order_generator.get())
