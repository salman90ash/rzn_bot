### 1. Создаем виртуальное окружение
```
python -m venv venv
```
### 2. Настраиваем зависимости
```
pip install -r requirements.txt
```
### 3. Настраиваем переменные окружения
```
vim .env
```
Прописываем<br>
TELEGRAM_BOT_TOKEN=<br>
TELEGRAM_ADMIN_ID=

### 4. Создание службы
```
sudo vim /etc/systemd/system/rzn_bot.service

```

Указываем следующее содержимое
```
[Unit]
Description=rzn bot
After=multi-user.target
 
[Service]
User=<user>

Restart=always
ExecStart=/home/<user>/apps/rzn_bot/venv/bin/python /home/<user>/apps/rzn_bot/main.py
 
[Install]
WantedBy=multi-user.target
```

Перезугражем systemctl
```
sudo systemctl daemon-reload
```

Pапуск службы
```
sudo systemctl start rzn_bot.service
```

Посмотреть статус службы
```
sudo systemctl status rzn_bot.service
```

Добавляем службу в автозагрузку системы
```
sudo systemctl enable rzn_bot.service
```
