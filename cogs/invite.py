from discord.ext import commands
import discord


class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self, ctx):
        e = discord.Embed(color=0xeba134, title='Bot Invite Link',
                          description='[Click Me](https://discord.com/api/oauth2/authorize?client_id'
                                      '=969899538141835274&permissions=515466718272&scope=bot) to invite this bot to '
                                      'your server')
        await ctx.send(embed=e)


def setup(client):
    client.add_cog(Invite(client))
