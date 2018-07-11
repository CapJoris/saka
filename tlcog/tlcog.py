#default
import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help

#utilities
import random
from random import choice
from random import randint
import base64
import json
import aiohttp
import itertools
import requests

#math
import math
import decimal
from decimal import Decimal, ROUND_HALF_UP, DecimalException
from math import factorial as mfac

#statistic
from scipy import stats
import numpy

class tlcog:
    """tlcog"""
    
    def __init__(self, bot):
        self.bot = bot
        
    
    
    #UTILITIES
    def tlm(self):
        tlservermobile = self.bot.get_server('301578535175323658')
        return tlservermobile
    
    def isla(self):
        isla = self.tlm().get_member('199436790581559296')
        return isla
      
    @commands.command(pass_context = True, no_pm = True)
    async def owner(self, ctx):
        await self.bot.say('{} is the Owner of this Bot.'.format(self.isla().name))
    

    
    #MATHS
    def comb(self, x:int, y:int, rounding):
        xfac = mfac(x)
        yfac = mfac(y)
        nfac = mfac(x - y)
        op1 = yfac * nfac
        comb = Decimal(xfac / op1)
        return Decimal(comb.quantize(Decimal('{}'.format(rounding)), rounding = ROUND_HALF_UP))
    
    @commands.command(pass_context = True, no_om = False)
    async def combinatorials(self, ctx, x:int, y:int, rounding:int = None):
        """Calculate mathematical combinatorials
        
        
        Rounding default disabled, to change the value follow this method: for x.n rounding is 1, for x.nn rounding is 10, for x.nnn rounding is 100, etc."""
        if rounding is None:
            rounding = '0'
        else:
            rounding = '.{}'.format(rounding)
        try:
            await self.bot.say(self.comb(x, y, rounding))
        except ValueError:
            await self.bot.say('Cannot do factorial operation for a negative number.\n```py\n{} < 0```'.format(x - y))
        except DecimalException:
            await self.bot.say('Number too big.')
          
        
            
    #STATISTICS
    def chi(self, x:int, y:int, z:int, w:int):
        array = numpy.array([[x,y],[z,w]])
        chi2 = stats.chi2_contingency(array)
        chi2p = chi2[1]
        return chi2p

    
    @commands.command(pass_context = True, no_pm = False)
    async def chi2(self, ctx, x:int, y:int, z:int, w:int):
        try:
            if self.chi(x, y, z, w) <= 0.05:
                m = 'Those values statistically have a relevant difference.'
            elif self.chi(x, y, z, w) < 1:
                m = 'Those values statistically don\'t have a significant difference'
            elif self.chi(x, y, z, w) == 1:
                m = 'Those values statistically are the same' 
            await self.bot.say(str(self.chi(x, y, z, w)) + '\n{}'.format(m))
        except ValueError:
            await self.bot.say('Joris did something wrong')
        except DecimalException:
            await self.bot.say('Joris does not know what this part means')

                
                    
def setup(bot):
    n = tlcog(bot)
    bot.add_cog(n)
