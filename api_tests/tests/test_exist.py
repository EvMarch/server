import allure
import pytest
import requests
from api_tests.urls import Urls
from api_tests.endpoints import Endpoints
from api_tests.helps import NewEmailCreate
from api_tests.user_requests import Exist

@allure.title('Проверка шоковости')
@allure.description('''Отправляем запрос с указанием почты зарегистрированного пользователя''')
def test_exist_user(user_register):


    data = Exist.exist
    response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_exist}', json=data)
    assert response.status_code == 200

    responce = response.json()
    assert "exist" in responce
    assert responce["exist"] is True


@allure.title('Проверка шоковости')
@allure.description('''Отправляем запрос с указанием почты незарегистрированного пользователя''')
def test_not_exist_user():

    data = NewEmailCreate().get_email()
    
    response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_exist}', json=data)
    assert response.status_code == 200

    responce = response.json()
    assert "exist" in responce
    assert responce["exist"] is False