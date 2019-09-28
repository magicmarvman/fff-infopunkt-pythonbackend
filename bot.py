import telepot
from telepot.delegate import per_chat_id, create_open, pave_event_space, include_callback_query_chat_id
import jsonFormatter
import json

# load config files
with open('config.json') as json_data_file:
    data = json.load(json_data_file)

telegram_bot_token = data['bot']['private_key']

bot = telepot.Bot(telegram_bot_token)

# get the data from server
updates = bot.getUpdates()
print(updates)
# Filter the messages
messages = dict()

groupIds = [update['message']['chat']['id'] for update in updates if 'text' in update['message']]

for groupId in groupIds:
    messages[str(groupId)] = [update['message']['text'] for update in updates if 'text' in update['message'] and groupId == update['message']['chat']['id']]

#//print(messages)
datasets = [[]]

#//print(messages)

for messageSet in messages.values():

    title = ""
    description = ""
    meetingPoint = ""
    startingPoint = ""
    endPoint = ""
    routeLength = ""

    jsonFeed = []

    for message in messageSet:
        #print(message)
        jsonFeed = message.split('\n')

        title = jsonFeed[0]
        description = jsonFeed[1]
        meetingPoint = jsonFeed[2]
        startingPoint = jsonFeed[3]
        endPoint = jsonFeed[4]
        routeLength = jsonFeed[5]
        print(jsonFeed)
        datasets.append(jsonFeed)

print(datasets[1])







'''
datastock = json.dumps(message)

print(datastock)
'''