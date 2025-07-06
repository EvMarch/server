import allure
import pytest
import requests
from api_tests.urls import Urls
from api_tests.endpoints import Endpoints
from api_tests.data import NewName
from api_tests.helps import NewNameCreate

@allure.title('Проверка смены имени авторизированного пользователя')
@allure.description('Отправляем запрос о переименовании с предварительной авторизацией')
def test_change_user_name_auth(user_login):

    new_name = NewNameCreate().get_name()
    headers = {
        'Authorization': f'Bearer {user_login}'


    }

    response = requests.patch(f'{Urls.BASE_URL}{Endpoints.user_rename}', json=new_name, headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert 'name' in data['user']
    assert data['user']['name'] == new_name['name']

@allure.title('Проверка смены имени без авторизации')
@allure.description('Отправляем запрос о переименовании без авторизации')
def test_change_user_name_not_auth():

    new_name = NewNameCreate().get_name()

    response = requests.patch(f'{Urls.BASE_URL}{Endpoints.user_rename}', json=new_name)
    assert response.status_code == 401
    data = response.json()
    assert data['message'] == 'Authorization header required'

@allure.title('Проверка смены имени на пустое значение')
@allure.description('Отправляем запрос о переименовании на новое имя, поле оставляем пустым')
def test_change_user_name_validation_error(user_login):

    new_name = NewName.empty
    headers = {
        'Authorization': f'Bearer {user_login}'
    }
    payload = {
        'name': new_name
    }
    response = requests.patch(f'{Urls.BASE_URL}{Endpoints.user_rename}', json=payload, headers=headers)
    assert response.status_code == 422
    data = response.json()
    assert data ['type'] == 'validation'




