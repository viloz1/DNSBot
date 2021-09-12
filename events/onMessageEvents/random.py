async def random(message):
    messageSplit = message.content.lower().split(" ")

    for word in messageSplit:
        if word == "sköj":
            await message.channel.send("***skôj***")
            return
        if word == "dns":
            await message.channel.send("Datas Nämnd för ***skôj***")
            return
