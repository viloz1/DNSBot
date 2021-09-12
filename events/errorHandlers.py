import discord

async def generalErrorHandler(client, config, event, *args, **kwargs):
    id = config["owner"]
    message = f"**Error**: \n \n Event: {event} \n Args: {args} \n Kwargs: {kwargs}"
    member = client.get_user(id)
    channel = await member.create_dm()
    await channel.send(message)

