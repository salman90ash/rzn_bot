import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
ADMIN_ID = int(os.environ['TELEGRAM_ADMIN_ID'])
RZN_TYPES_add = [(1, 'РУ'), (4, 'ВИРД'), (3, 'Обращения по вх.'),  (6, 'Обращения по исх.'), (5, 'Дубликат'), ]
# RZN_TYPES_list = [(1, 'РУ'), (2, 'Ввоз'), (3, 'Обращения по вх.'), (4, 'ВИРД'), (5, 'Дубликат'), (6, 'Обращения по исх.')]

