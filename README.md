# VK Friends List Generator
Приложение, которое позволяет получить список друзей пользователя VK и сохранить его в формате CSV, TSV или JSON.

# Установка и настройка
1. Установите Python 3.8 или более позднюю версию.
2. Склонируйте репозиторий с помощью команды ```git clone https://github.com/askartolegen/vk-friends-generator.git```.
3. Установите необходимые зависимости с помощью команды ```pip install -r requirements.txt```.
4 .Получите ключ доступа VK API и укажите его в качестве значения параметра --token при запуске скрипта.
# Запуск
Для запуска скрипта используйте команду ```python friends_generator.py --token <ваш_ключ_API> --user-id <ID_пользователя> --format <формат_вывода> --output-file <путь_к_файлу>```.

# Описание приложения
Приложение получает список друзей пользователя VK API и сохраняет его в формате CSV, TSV или JSON.

# API-эндпоинты
Приложение использует следующие API-эндпоинты VK API:

* friends.get - для получения списка друзей пользователя.
# Авторизация
Для работы приложения необходимо получить ключ доступа VK API. Ключ можно получить, создав приложение на сайте VK и запросив его с помощью метода ```oauth.vk.com/access_token```. Ключ доступа должен быть передан в качестве параметра ```--token``` при запуске скрипта.