import json
import os
import hashlib

async def anonymousMsg(message, client):
    DB_PATH = os.getenv('DB_PATH')

    content = message.content
    author_id = message.author.id

    f = open(DB_PATH + "/senders.json")
    data = json.load(f)
    f.close()

    f = open(DB_PATH + "/config.json")
    config = json.load(f)
    f.close()

    unique_id = 0
    try:
        unique_id = data[str(author_id)]
    except:
        unique_id = hashlib.sha256(str(author_id).encode('ASCII')).hexdigest()
        data.update({str(author_id): unique_id})

    channel = client.get_channel(int(config["channels"]["anonymous_messages"]))
    await channel.send("**Unique_ID: " + str(unique_id) + " **\n \n" + content)

    with open(DB_PATH + "/senders.json", 'w') as outfile:
        json.dump(data, outfile)


async def anonymousAnsw(message, client):
    if message.reference is None:
        return

    DB_PATH = os.getenv('DB_PATH')

    f = open(DB_PATH + "/config.json")
    config = json.load(f)
    f.close()

    message_sent = await client.get_channel(config["channels"]["anonymous_messages"]).fetch_message(message.reference.message_id)
    unique_id = message_sent.content.split(" ")[1]

    f = open(DB_PATH + "/senders.json")
    data = json.load(f)
    f.close()

    for key, value in data.items():
        if value == unique_id:
            member = client.get_user(int(key))
            channel = await member.create_dm()
            await channel.send("**DNS svarar:** " + message.content)
            return
