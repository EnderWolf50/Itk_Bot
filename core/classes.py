import discord
from discord.ext import commands


class Cog_Ext(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
