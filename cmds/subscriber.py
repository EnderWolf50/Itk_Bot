import discord
from discord.ext import commands
from core.classes import Cog_Ext
from core.rwFile import rFile, wFile

import redis

subscriberList = {}

r = redis.Redis(host="redis-17540.c56.east-us.azure.cloud.redislabs.com",
                port="17540",
                password="i7KZ0dEX4TP01e8HCM20vRkvNb7U2yUr")

for key in r.keys():
    subscriberList[key.decode("utf-8")] = r.get(key).decode("utf-8").split(", ")

class Subscribe(Cog_Ext):
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.channel == self.bot.get_channel(675956755112394753) and msg.author != self.bot.user:
            if len(msg.mentions) == 1 and str(msg.mentions[0].id) in subscriberList.keys():

                subscriptionInfo = f"<@{msg.mentions[0].id}>"
                for value in subscriberList[f"{msg.mentions[0].id}"]:
                    subscriptionInfo += f"\n{value}"

                await msg.channel.send(subscriptionInfo, delete_after= 180)

    @commands.group(aliases= ['s', 'sub'])
    async def subscriber():
        pass

    @subscriber.command()
    async def list(self, ctx):
        listMsg = ""
        for k, v in subscriberList.items():
            listMsg += f"<@{k}>\n"
            for line in v:
                listMsg += f"{line}\n"
        await ctx.channel.send(listMsg)

    @subscriber.command()
    async def set(self, ctx, user: discord.Member, *args):
        for newValue in len(args):
            print(newValue)
            print(args)


def setup(bot):
    bot.add_cog(Subscribe(bot))