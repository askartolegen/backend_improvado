import argparse

def main(token, user_id, output_format, output_file):
    # Здесь должен быть код для получения списка друзей из VK и записи в файл с указанным форматом
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='VK friends list generator')
    parser.add_argument('-t', '--token', required=True, help='Authorization token')
    parser.add_argument('-u', '--user-id', required=True, help='User ID to generate report for')
    parser.add_argument('-f', '--format', default='csv', choices=['csv', 'tsv', 'json'], help='Output format')
    parser.add_argument('-o', '--output-file', default='report', help='Output file path')
    args = parser.parse_args()

    main(args.token, args.user_id, args.format, args.output_file)
