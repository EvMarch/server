import requests
import pytest
from api_tests.urls import Urls
from api_tests.endpoints import Endpoints
from api_tests.user_requests import User
from api_tests.helps import NewNameCreate

# фикстура регистрации юзера
@pytest.fixture()
def user_register():
    user_create = User().user_registration_in_the_system_and_get_user_data()
    yield user_create

# фикстура авторизации юзера
@pytest.fixture()
def user_login():
    user_create = User().user_registration_in_the_system_and_get_user_data()
    token = User().user_login_in_the_system_and_get_token(user_create)
    return token



