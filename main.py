import discord

from discord.ext import commands

import music

cogs = [music]

client=commands.Bot(command_prefix='?', intents = discord.Intents.all())


for i in range(len(cogs)):
  cogs[i].setup(client)




client.run("ODk1NTE0NjE3NjIxNjU5NzA4.YV5q-g.67qHi2oTuPJBdLez7YOHQoVzOO8")