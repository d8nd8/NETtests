# Задача №2 Автотест API Яндекса
#
# Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.
# Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой
#
# Пример положительных тестов:
#
# Код ответа соответствует 200.
# Результат создания папки - папка появилась в списке файлов.
import requests
from config import TOKEN


class TestYDCreateFolder:
    API_CREATE_FOLDER_URL = "https://cloud-api.yandex.net/v1/disk/resources"
    token = TOKEN

    def setup_method(self, token) -> None:
        self.headers = {
            "Authorization": f"OAuth {self.token}"
        }

    def test_delete_folder(self):
        params = {
            "path": "Test_Image",
            "permanently": True,
        }
        response = requests.delete(self.API_CREATE_FOLDER_URL, headers=self.headers, params=params)

        assert response.status_code == 204


    def test_create_folder(self):
        params = {
            "path": "Test_Image",
        }
        response = requests.put(self.API_CREATE_FOLDER_URL, headers=self.headers, params=params)

        assert response.status_code == 201

    def test_exist_folder(self):
        params = {
            "path": "Test_Image",
        }
        response = requests.get(self.API_CREATE_FOLDER_URL, headers=self.headers, params=params)

        assert response.status_code == 200






