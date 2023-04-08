import requests
from base.configuration import BASE_URL
from base.response_validator import Response
from base.schemas import PET

def test_return_pet():
    '''
    Test if api returns a single pet
    :return: json pet
    '''

    #Arrange
    pet_id = "2"
    url = BASE_URL + "v2/pet/" + pet_id

    #Act
    r = requests.get(url=url)
    response = Response(r)

    #Assert
    response.assert_status_code(200).validation_pydantic(PET)
