import telepot
from telepot.delegate import per_chat_id, create_open, pave_event_space, include_callback_query_chat_id
import jsonFormatter
import json
import Strike
import time

datasets = []
datasetsOld = []

print("Listening....")

while True:
    # load config files
    with open('config.json') as json_data_file:
        data = json.load(json_data_file)

    telegram_bot_token = data['bot']['private_key']

    bot = telepot.Bot(telegram_bot_token)

    updates = bot.getUpdates()
    #print(updates)
    messages = dict()

    groupIds = [update['message']['chat']['id'] for update in updates if 'text' in update['message']]

    for groupId in groupIds:
        messages[str(groupId)] = [update['message']['text'] for update in updates if 'text' in update['message'] and groupId == update['message']['chat']['id']]

    datasets = []
    i = 0
    for messageSet in messages.values():

        chatId = groupIds[i]
        title = ""
        description = ""
        dateTime = ""
        startingPoint = ""
        startingTime = "" # could be a time stamp
        endPoint = ""
        routeLength = ""

        jsonFeed = []

        for message in messageSet:
            # TODO Fix help message to only be displayed once
            if (message == "help"):
            #    bot.sendMessage(text="Jedes “Property in einer Zeile”\nWenn nicht bekannt NONE einfügen\n\nSchema:\nTitel\nBeschreibung\nDatum und Uhrzeit\nStartpunkt / Treffpunkt\nEndpunkt\nRoutenlänge\nWebsite Veranstalter (wenn nicht bekannt NONE schreiben)\n", chat_id=chatId)
                continue

            try:
                jsonFeed = message.split('\n')

                title = jsonFeed[0]
                description = jsonFeed[1]
                dateTime = jsonFeed[2]
                startingPoint = jsonFeed[3]
                endPoint = jsonFeed[4]
                routeLength = jsonFeed[5]
                website = jsonFeed[6]
                datasets.append(jsonFeed)
            except:
                continue

    #print(datasets)

    if datasets == datasetsOld:
        continue
    i = 1
    for dataset in datasets:
        model = Strike.StrikeModel()
        model.title = dataset[0]
        model.description = dataset[1]
        model.datetime = dataset[2]
        model.meetingPoint = dataset[3]
        model.endPoint = dataset[4]
        model.routeLength = dataset[5]
        model.latitude = 0
        model.longitude = 0
        model.strikeId = i
        model.url = dataset[6]
        model.searchTitle = dataset[0].lower()
        model.source = "Telegram chat group, collected bei FFF_Info Bot"

        model.save()

        i += 1

    datasetsOld = datasets

    print("Wrote data to server")