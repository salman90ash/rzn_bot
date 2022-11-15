import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
if os.environ.get('TELEGRAM_ADMIN_ID') is not None:
    ADMIN_ID = int(os.environ.get('TELEGRAM_ADMIN_ID'))
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
URL = ''
if PORT != '':
    URL = f"{HOST}:{PORT}"
else:
    URL = HOST
RZN_TYPES_add = [(1, 'РУ'), (4, 'ВИРД'), (3, 'Обращения по вх.'),  (6, 'Обращения по исх.'), (5, 'Дубликат'), ]
# RZN_TYPES_list = [(1, 'РУ'), (2, 'Ввоз'), (3, 'Обращения по вх.'), (4, 'ВИРД'), (5, 'Дубликат'), (6, 'Обращения по исх.')]

