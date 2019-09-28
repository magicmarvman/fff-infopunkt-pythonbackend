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
    groupNames = [groupName['message']['chat']['title'] for groupName in updates if 'text' in groupName['message']]

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
                #print(jsonFeed)
                #print(len(jsonFeed))
                if len(jsonFeed) == 9:
                    print("EXEC 1")
                    if jsonFeed[0].lower().strip() == 'none': # Title
                        jsonFeed[0] = ""
                    print("EXEC 2")
                    if jsonFeed[1].lower().strip() == 'none': # Description
                        jsonFeed[1] == ''
                    if jsonFeed[8].lower().strip() == 'None': # organisation
                        jsonFeed[8] = ''
                    print("EXEC 3")
                    if jsonFeed[2].lower().strip() == 'None': # Date
                        jsonFeed[2] = ''
                    print("EXEC 4")
                    if jsonFeed[3].lower().strip() == 'None': # Time
                        jsonFeed[3] = ''
                    print("EXEC 5")
                    if jsonFeed[4].lower().strip() == 'None': # meetingPoint / StartPoint
                        jsonFeed[4] = ''
                    print("EXEC 6")
                    if jsonFeed[5].lower().strip() == 'None': # endPoint
                        jsonFeed[5] = ''
                    print("EXEC 7")
                    if jsonFeed[6].lower().strip() == 'None': # routing
                        jsonFeed[6] = ''
                    print("EXEC 8")
                    if jsonFeed[7].lower().strip() == 'None': # url
                        jsonFeed[7] = ''
                    print("EXEC 9")
                    #jsonFeed.append(bot.getChat(groupIds)['title'])
                    print(jsonFeed)
                    datasets.append(jsonFeed)

            except:
                #print("Error")
                continue

    #print(datasets)

    if datasets == datasetsOld:
        continue
    i = 1
    for dataset in datasets:
        model = Strike.StrikeModel()
        model.title = dataset[0]
        model.description = dataset[1]
        model.date = dataset[2]
        model.startTime = dataset[3]
        model.meetingPoint = dataset[4]
        model.endPoint = dataset[5]
        model.routeLength = dataset[6]
        model.latitude = 0
        model.longitude = 0
        model.strikeId = i
        model.url = dataset[7]
        model.searchTitle = dataset[0].lower()
        model.source = "Telegram chat group, collected bei FFF_Info Bot"
        #model.groupSource = dataset[8]
        model.groupSource = "FFF Info Test Group"
        model.organisation = dataset[8]

        model.save()
        print("Stored!")
        i += 1

    datasetsOld = datasets
    print(datasets)
    print("Wrote data to server")