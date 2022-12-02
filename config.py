import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
ADMIN_ID = int(os.environ.get('TELEGRAM_ADMIN_ID'))
# if os.environ.get('TELEGRAM_ADMIN_ID') is not None:
#     ADMIN_ID = int(os.environ.get('TELEGRAM_ADMIN_ID'))
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
API_TG_TOKEN = os.environ.get('API_TG_TOKEN')
URL = ''
API = f'/tg/api/v1/{API_TG_TOKEN}'

if PORT != '':
    URL = f"{HOST}:{PORT}{API}"
else:
    URL = HOST + API

print(URL)
RZN_TYPES_add = [(1, 'РУ'), (4, 'ВИРД'), (3, 'Обращения по вх.'),  (6, 'Обращения по исх.'), (5, 'Дубликат'), ]
# RZN_TYPES_list = [(1, 'РУ'), (2, 'Ввоз'), (3, 'Обращения по вх.'), (4, 'ВИРД'), (5, 'Дубликат'), (6, 'Обращения по исх.')]

