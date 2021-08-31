import discord

async def mainMessage(self):
    file = open("message.txt", encoding = 'utf-8')
    id = file.readline()
    line = file.read()
    file.close()

    channel = discord.utils.get(self.bot.get_all_channels(), id = int(id))


    messages = await channel.history(limit=1).flatten()
    if len(messages) == 0:
        await channel.send(line)
    else:
        message = messages[0]
        if message.content != line:
            await message.edit(content=line)