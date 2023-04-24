from telethon import TelegramClient, events, sync

# укажите данные вашего бота
api_id = 17199600
api_hash = 'd96d40fde445f4629c6c75d61f67dec2'
bot_token = '6293189472:AAGYvYa98gukaLE052SADcJUaoP2O-2N3bc'

# укажите список id пользователей, которым нужно отправить сообщение
user_ids = [383127157, 5109390503]

# создайте клиента Telethon
client = TelegramClient('my_session', api_id, api_hash).start(bot_token=bot_token)

# отправьте сообщение каждому пользователю из списка
for user_id in user_ids:
    try:
        # отправить сообщение пользователю
        client.send_message(user_id, 'TEST')
        print(f'Сообщение отправлено пользователю {user_id}')
    except Exception as e:
        print(f'Ошибка при отправке сообщения пользователю {user_id}: {e}')

# закрыть клиент Telethon
client.disconnect()
