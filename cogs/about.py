from discord.ext import commands
import discord


class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def about(self, ctx):
        e = discord.Embed(color=0xeba134, title='About the bot',
                          description='It fetches three random images from an inventory of 360 images,'
                                      ' merges them and sends as a comic')
        e.add_field(name="About the Creators",
                    value="Bot Developer: [Sarthak Goel](https://github.com/sarty-definite)\n"
                          "API Developer: [Shubham Singh](https://github.com/ishubhamsingh2e/project-hazard)",
                    inline=False)
        await ctx.send(embed=e)


def setup(client):
    client.add_cog(Invite(client))
