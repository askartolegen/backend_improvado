import os
from dotenv import load_dotenv

load_dotenv(dotenv_path='.env-dev')
VK_API_TOKEN = os.getenv('VK_API_TOKEN')
USER_ID = os.getenv('USER_ID')

