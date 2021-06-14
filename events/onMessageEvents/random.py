async def random(message):
    if message.content.lower() == "sköj":
        await message.channel.send("***skôj***")
        return

    for word in message.content.lower().split(" "):
        if word == "dns":
            await message.channel.send("Datas Nämnd för ***skôj***")
            return
