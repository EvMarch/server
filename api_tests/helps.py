from faker import Faker
import time
import random
import string
import json



class NewEmailCreate:
    # функция генерации незарегистрированной почты для проверки шоковости
    @staticmethod
    def get_email():
        fake = Faker()
    # Генерируем базовый email
        base_email = fake.email()
    # Получаем текущий timestamp для уникальности
        timestamp = int(time.time())
    # Или добавляем случайную строку для большей уникальности
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    # Формируем уникальный email
        email = f"{base_email.split('@')[0]}_{timestamp}_{random_suffix}@{base_email.split('@')[1]}"
        data = {
            "email": email

        }
        return data

class NewNameCreate:
    # функция генерации нового имени
    def __init__(self, locale='en_US'):
        self.faker = Faker(locale)
    
    def get_name(self):
        new_name = self.faker.name()
        data = {
            'name': new_name
        }
        return data



class DataCreate:
    # функция генерации фэйковых валидных данных для регистрации и последующего логина
    @staticmethod
    def generating_fake_valid_data_to_register_user():
        fake = Faker()
        base_email = fake.email()
        timestamp = int(time.time())
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
        local_part, domain = base_email.split('@')
        max_total_length = 50
        rest_length = len('_') + len(str(timestamp)) + len('_') + len(random_suffix) + 1 + len(domain)

        max_local_part_length = max_total_length - rest_length
        if len(local_part) > max_local_part_length:
            local_part = local_part[:max_local_part_length]

        email = f"{local_part}_{timestamp}_{random_suffix}@{domain}"
        length = random.randint(5, 20)
        characters = string.ascii_letters + string.digits  # латиница + цифры

        password = ''.join(random.choices(characters, k=length))
        
        age = random.randint(1, 99)
        data = {
            "email": email,
            "password": password,
            "age": age
        }

        return data
