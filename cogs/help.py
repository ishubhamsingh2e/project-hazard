from discord.ext import commands
import discord


class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["HELP"])
    async def help(self, ctx):
        embed = discord.Embed(title='Bot prefix (*)', colour=discord.Colour.blue())
        embed.add_field(name="*hazard", value="Sends a randomly generated comic strip. alias: `*story`",
                        inline=False)

        embed.add_field(name="*invite", value="Add this bot to your server, get an invite link using this command",
                        inline=False)

        embed.add_field(name="*about", value="Get more info about the bot",
                        inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Help(client))
