from discord.ext import commands
import discord
import requests
import json
from io import BytesIO
from PIL import Image


def get_image(red):
    if red == 'red':
        r = requests.get('https://sb2001nov.pythonanywhere.com/?red=1')
    else:
        r = requests.get('https://sb2001nov.pythonanywhere.com/')
    data = json.loads(r.text)

    images = [Image.open(BytesIO(requests.get(data['1']).content)),
              Image.open(BytesIO(requests.get(data['2']).content)),
              Image.open(BytesIO(requests.get(data['3']).content))]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
    return new_im


class Hazard(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["hazard", "story"])
    async def hazardous(self, ctx, *, red=''):
        with BytesIO() as image_binary:
            get_image(red).save(image_binary, 'PNG')
            image_binary.seek(0)
            await ctx.send(file=discord.File(fp=image_binary, filename='image.png'))


def setup(client):
    client.add_cog(Hazard(client))
