import discord
from discord.ext import commands
from __main__ import send_cmd_help

class poll:
    """Creates polls"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context = True, no_pm = True)
    async def createpoll(self, ctx, *, poll):
        """Creates a new poll"""
        await self.bot.say(poll)
        
def setup(bot):
    n = poll(bot)
    bot.add_cog(n)
