async def on_member_join(self, member):
    channel_id = '390056984650579980'
    recruitment = '<#408205979805548545>'
    m = f' Welcome {member.mention} to Royal Smash League.\n**First off lets get you're roles registered.**\n- To get a Captain role (only for team captains), please type: `+selfrole Captain`\n- To get any of the Region roles, please type: `+selfrole Region_NA` or `+selfrole Region_APAC` or `+selfrole Region_EU`\n- To get a Graphics Designer role, please type: `+selfrole GFX Designer`\n**Once you have done all that you're now onto getting your team registered for the next season.**\n- To register for the next season, please type: `+rsl signup`\n- You will get a form sent to your DMs you don't need to instantly fill out the form straight away, it will not disappear or close until one of the Directors make an announcement, and even then they will be sure to give 1-2 weeks advance on the dead line.\n**Now if you're looking for a team.**\n- There is an easy to access\n{recruitment} channel in our server, it in under the category of "Clash Royale", and there you can find all the current teams that are recruiting for members at that time.\nGood Luck with your time in RSL we hope to hear from you again.'
    await self.bot.send_message(self.bot.get_channel(channel_id), m)
