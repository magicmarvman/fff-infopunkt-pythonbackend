import telepot
from telepot.delegate import per_chat_id, create_open, pave_event_space, include_callback_query_chat_id
import jsonFormatter
import json

telegram_bot_token = "938606091:AAG8fQx3u7oCRup4jY_pQBvpIsRrliCt28A"

bot = telepot.Bot(telegram_bot_token)

# get the data from server
updates = bot.getUpdates()

# Filter the messages
message = {"": []}

groupIds = [update['message']['chat']['id'] for update in updates if 'text' in update['message']]

for groupId in groupIds:
    message[String(groupId)] = messageText = [update['message']['text'] for update in updates if 'text' in update['message'] and groupId == update['message']['chat']['id']]

datastock = json.dumps(message)

print(datastock)