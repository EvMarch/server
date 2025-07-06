import requests
from api_tests.helps import DataCreate
from api_tests.endpoints import Endpoints
from api_tests.urls import Urls
from api_tests.helps import DataCreate



class DataUser:
    # логин зарегистрированного пользователя и неверным паролем
    def wrong_password():
        email = User.user_registration_in_the_system_and_get_user_data()['email']
        password = DataCreate.generating_fake_valid_data_to_register_user()['password']
        data = {
            "email": email,
            "password": password
        }

        return data


    # логин незарегистрированного пользователя и верным паролем
    def wrong_email():
        email = DataCreate.generating_fake_valid_data_to_register_user()['email']
        password = User.user_registration_in_the_system_and_get_user_data()['password']
        data = {
            "email": email,
            "password": password
        }

        return data


    # данные для логина без поля "email"
    def invalid_data_login_without_email():
        password = User.user_registration_in_the_system_and_get_user_data()['password']
        data = {
            "email": "",
            "password": password
        }

        return data

    # данные для логина без поля "Password"
    def invalid_data_login_without_password():
        email = User.user_registration_in_the_system_and_get_user_data()['email']
        data = {
            "email": email,
            "password": ""
        }

        return data

    # пустые поля
    def null_data_login():
        data = {
            "email": "",
            "password": ""
        }


class User:

    # функция регистрации в системе с возвратом email и пароля
    @staticmethod
    def user_registration_in_the_system_and_get_user_data():
        data = DataCreate.generating_fake_valid_data_to_register_user()
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_register}', json=data)
        reg = {k: data[k] for k in ("email", "password")}
        return reg

    # функция логина в системе с возвратом ответа и токена
    @staticmethod
    def user_login_in_the_system_and_get_token(user_data):
        response = requests.post(f'{Urls.BASE_URL}{Endpoints.user_login}', json=user_data)
        #response_json = response.json()
        return response.json().get('token')

# валидные данные для регистрации
class Exist:
# почта зарегистрированного пользователя
    email = User.user_registration_in_the_system_and_get_user_data()['email']
    exist = {
       "email": email
    }
