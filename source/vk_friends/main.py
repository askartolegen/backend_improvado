import argparse
import vk_api


def main(token, user_id, output_format='csv', output_file='reports'):

    # авторизация в API VK
    vk_session = vk_api.VkApi(token=token)

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='VK friends list generator')
    parser.add_argument('-t', '--token', required=True, help='Authorization token')
    parser.add_argument('-u', '--user-id', required=True, help='User ID to generate report for')
    parser.add_argument('-f', '--format', default='csv', choices=['csv', 'tsv', 'json'], help='Output format')
    parser.add_argument('-o', '--output-file', default='report', help='Output file path')
    args = parser.parse_args()

    main(args.token, args.user_id, args.format, args.output_file)
