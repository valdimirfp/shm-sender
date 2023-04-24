from telethon import TelegramClient, events, sync
from telethon.tl.types import MessageEntityUrl

# укажите данные вашего бота
api_id = 00000000
api_hash = '000000000'
bot_token = '0000000:00000000000000000'

# Set the path to the file containing the user IDs you want to send messages to
file_path = 'users.txt'

# Read the user IDs from the file and convert them to integers
with open(file_path, 'r') as f:
    user_ids = [int(line.strip()) for line in f]

# Create a Telethon client
client = TelegramClient('my_session', api_id, api_hash).start(bot_token=bot_token)

# Create a message entity for the hyperlink
url = 'https://t.me/+5Y1-M6eHsH5kNzMy'
entity = MessageEntityUrl(offset=56, length=4)
entity.url = url

# Set the message text with the hyperlink
message_text = "Привет 😎 \n\n🔥 Мы рады сообщить о добавлении новых пакетов подписки на наш VPN-сервис \n\nТеперь у вас есть возможность выбрать подписку на 3, 6 или 12 месяцев, чтобы защитить свое интернет-соединение на длительный период 📡 \n\n⚠️ Новые пакеты подписки на VPN-сервис имеют следующие цены ⚠️ \n\n3 месяца - 600₽ \n6 месяцев - 1135₽ \n12 месяцев - 2145₽ 🔥 \n\n⚡️ Не упустите возможность воспользоваться новыми тарифами по выгодным ценам. Закажи новую подписку в разделе 'Ключи' ➡ 'Новый ключ' ⚠️ \n\nТак же ты всегда можешь обратиться за помощью к нам через раздел Помощь ➡[Чат](https://t.me/+5Y1-M6eHsH5kNzMy) поддержки 🛠️ \n\nС уважением, \nКоманда SecretumVPN 😎"

# Send the message to each user in the list of IDs
for user_id in user_ids:
    try:
        # Send the message to the user with the entities included in the message text
        client.send_message(user_id, message_text, parse_mode='markdown')
        print(f'Message sent to user {user_id}')
    except Exception as e:
        print(f'Error sending message to user {user_id}: {e}')

# Disconnect the Telethon client
client.disconnect()