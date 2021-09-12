import discord
import asyncio
from discord.ext import commands

async def onCommandError(self, ctx: commands.Context, error: commands.CommandError):
    """A global error handler cog."""

    if isinstance(error, commands.CommandNotFound):
        return  # Return because we don't want to show an error for every command not found
    elif isinstance(error, commands.CommandOnCooldown):
        message = f"Detta kommandot är på cooldown. Försök igen efter {round(error.retry_after, 1)} sekunder."
    elif isinstance(error, commands.MissingPermissions):
        message = "Du saknar tillåtelse att använda detta kommandot!"
    elif isinstance(error, commands.UserInputError):
        message = "Någonting gick fel med din input, försök igen!"
    else:
        message = "Något gick fel. Försök igen!"

    await ctx.send(message, delete_after=5)
    await ctx.message.delete(delay=5)