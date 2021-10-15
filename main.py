import discord
from discord.ext import commands
from keep_alive import keep_alive
import music

cogs = [music]

client = commands.Bot(command_prefix="-", intents = discord.Intents.all())

@client.command(name='credits')
async def credits(ctx):
    await ctx.send('Created since Rhythm got deleted -- Made in October 2021')
    await ctx.send('Thanks to Emily and Olivia for supporting me during the countless code errors I fixed')

for i in range(len(cogs)):
  cogs[i].setup(client)

keep_alive()

client.run("token")
