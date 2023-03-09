import tempfile
import os
import config

from source.vk_friends.friends_generator import main


def test_main():
    # Создаем временный файл и передаем его в функцию main()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_file_path = f.name
        main(token=config.VK_API_TOKEN, user_id=config.USER_ID, output_format = 'csv', output_file = temp_file_path)

        # Проверяем, что файл содержит ожидаемые данные
        with open(temp_file_path, 'r') as temp_file:
            with open('expected_report1.csv', 'r') as expected_file:
                assert temp_file.read() == expected_file.read()

    # Создаем еще один временный файл и передаем его в функцию main()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_file_path = f.name
        main(token=config.VK_API_TOKEN, user_id=config.USER_ID, output_format = 'tsv', output_file = temp_file_path)

        # Проверяем, что файл содержит ожидаемые данные
        with open(temp_file_path, 'r') as temp_file:
            with open('expected_report2.tsv', 'r') as expected_file:
                assert temp_file.read() == expected_file.read()

    # Создаем еще один временный файл и передаем его в функцию main()
    with tempfile.NamedTemporaryFile(delete=False) as f:
        temp_file_path = f.name
        main(token=config.VK_API_TOKEN, user_id=config.USER_ID, output_format = 'json', output_file = temp_file_path)

        # Проверяем, что файл содержит ожидаемые данные
        with open(temp_file_path, 'r') as temp_file:
            with open('expected_report3.json', 'r') as expected_file:
                assert temp_file.read() == expected_file.read()

    # Удаляем временные файлы
    os.remove(temp_file_path)
