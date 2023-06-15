import pytest
import requests
from base.configuration import BASE_URL
from base.base_pet.response_validator import Response
from base.base_pet.schemas import PET

@pytest.mark.API
def test_return_pet(say_hello):
    '''
    Test if api returns a single pet
    :return: json pet
    '''

    #Arrange
    pet_id = 2
    url = f"{BASE_URL}v2/pet/{pet_id}"

    #Act
    r = requests.get(url=url)
    response = Response(r)

    #Assert
    response.assert_status_code(200).validation_pydantic(PET)

def test_try_method_in_method(calculate, make_number):
    print(make_number)
    assert True

@pytest.mark.API
def test_put_pet(pet_generator):
    print(pet_generator.get())