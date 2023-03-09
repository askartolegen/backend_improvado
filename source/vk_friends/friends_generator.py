import argparse
import datetime
import html

import vk_api
import logging

import config
from report_generator import *


class Friends:
    def __init__(self, api, user_id):
        self.api = api
        self.user_id = user_id

    def get_friends(self):
        logging.info('Start getting friends...')
        # получение списка друзей пользователя
        response = self.api.friends.get(user_id=self.user_id, fields='sex,bdate,city,country,first_name', v='5.131')

        friends_list = []

        # обработка JSON-ответа
        for friend in response['items']:
            try:
                birthdate = friend.get('bdate', 'Не указана')
                if birthdate != 'Не указана':
                    # преобразование даты рождения в формат datetime
                    birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y')
                    # преобразование даты рождения в ISO формат и сохранение в словаре
                    birthdate = birthdate.date().isoformat()
            except Exception as e:
                birthdate = friend.get('bdate', 'Не указана')

            country = friend.get('country', {'title': 'Не указана'})['title']
            # декодирование Unicode-эскейп-последовательностей
            country = html.unescape(country)

            city = friend.get('city', {'title': 'Не указана'})['title']
            # декодирование Unicode-эскейп-последовательностей
            city = html.unescape(city)

            friends_list.append({'first_name': friend['first_name'],
                                 'last_name': friend['last_name'],
                                 'country': country,
                                 'city': city,
                                 'birthdate': birthdate,
                                 'gender': 'Женский' if friend['sex'] == 1 else 'Мужской'
                                 })

        # преобразование списка друзей в строку JSON
        friends_json = json.dumps(friends_list, ensure_ascii=False)

        logging.info(f'Finished getting {len(friends_list)} friends')
        friends_list = json.loads(friends_json)
        return friends_list


def main(token, user_id, output_format, output_file):
    logging.basicConfig(filename='../logs/example.log', level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')
    logging.info('Starting the script')

    report_generator = {'csv': CSVReportGenerator().generate_report, 'tsv': TSVReportGenerator().generate_report,
                        'json': JSONReportGenerator().generate_report}
    session = vk_api.VkApi(token=token)

    api = session.get_api()

    response = api.users.get(user_ids=user_id)

    # extract the first_name and last_name from the response
    first_name = response[0]['first_name']
    last_name = response[0]['last_name']

    logging.info(f'Get a list of friends for a user {user_id} {first_name} {last_name}')
    friend = Friends(api, user_id)

    if report_generator.get(output_format) is None:
        logging.info('Unsupported output format. Only CSV, TSV, and JSON formats are supported.')
        raise ValueError('Unsupported output format. Only CSV, TSV, and JSON formats are supported.')

    # сортируем список друзей
    sorted_friends = sorted(friend.get_friends(), key=lambda x: x['first_name'])

    # Pagination
    logging.info('Generate a report on 100 friends')
    start_index = 0
    index = 1
    while start_index <= len(sorted_friends):
        logging.info(f'Generate a report from {start_index} to {len(sorted_friends[start_index: start_index + 100])} '
                     f'items from the list of friends')
        report_generator[output_format](sorted_friends[start_index: start_index + 100], output_file+str(index))
        logging.info(f'The report is saved locally in a file {output_file+str(index)}.{output_format}')
        start_index += 100
        index += 1


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='VK friends list generator')
    # parser.add_argument('-t', '--token', required=True, help='Authorization token')
    # parser.add_argument('-u', '--user-id', required=True, type=int, help='User ID to generate report for')
    # parser.add_argument('-f', '--format', default='csv', choices=['csv', 'tsv', 'json'], help='Output format')
    # parser.add_argument('-o', '--output-file', default='report', help='Output file path')
    # args = parser.parse_args()
    #
    # main(args.token, args.user_id, args.format, args.output_file)
    main("vk1.a.jiVtk3rYzs6qwk1JEmMWmfQvAEn9-XZfJbsWw45bc44raveU0J-PoHXzLFGPDD0ilW9zraf17IVktc1fXg3kvrxpsz2c6pb230m1zLkM51dfP7sVtpy82usq3ZR7FdUDHB_KPwmxGdvyhY-PUDO-mwW2CQfEjwLxTUpaaMjaW5eScuvdVsu1L3fRyJTLjKY3aRRWMmz8u8NaKcHss6D4lg", 468144993, 'csv', 'report')

