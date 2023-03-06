import vk_api

# авторизация в API VK
vk_session = vk_api.VkApi(token='vk1.a.B7FGihQfvP8YenF07D1gps0ZOY-szFH8zVN4AAA0gNOfX_LUbJQm0fDRf17dG-ac-6rVYvwGT0k'
                                '4qXe97vXxcGjoJ1fjCtiFq30tTKJ8AUfQrOMEdGDViseAfX_EbW0O-jNpRp4vHgqwT78Viz6fpJZXBx1i'
                                'WitmvxaQxr25mug3ZyF7gsxIhMRv7qrU8YX4')

user_id = 123456

# получение списка друзей пользователя
response = vk_session.method('friends.get', {'user_id': f'{user_id}', 'fields': 'sex,bdate,city,country'})

# обработка JSON-ответа
for friend in response['items']:
    print(f"ID: {friend['id']}")
    print(f"Имя: {friend['first_name']}")
    print(f"Фамилия: {friend['last_name']}")
    print(f"Пол: {'Женский' if friend['sex'] == 1 else 'Мужской'}")
    print(f"Дата рождения: {friend.get('bdate', 'Не указана')}")
    print(f"Город: {friend['city']['title'] if 'city' in friend else 'Не указан'}")
    print(f"Страна: {friend['country']['title'] if 'country' in friend else 'Не указана'}")
    print("-" * 50)
