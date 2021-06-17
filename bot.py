import os
import discord
import random

from dotenv import load_dotenv
from discord_slash import SlashCommand
from discord.ext import commands
from discord_slash.utils.manage_commands import create_option

from app.Quote import Quote
from app.Guild import Guild

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
slash = SlashCommand(client, sync_commands=True)


for guild in client.guilds:
    guild_record = Guild.where("guild_number", guild.id).get()
    if not guild_record:
        Guild.create({
            "guild_number": guild.id
        })


def guild_ids():
    guild_ids = []
    for guild in Guild.all():
        guild_ids.append(guild.guild_number)
    return guild_ids


@client.event
async def on_ready():
    """When the bot connects to the servers"""
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    """When a message gets sent"""
    if message.author == client.user:
        """Skips if the sender is the bot"""
        return

    if "pizza" in message.content.lower():
        if random.randint(1, 10) == 1:
            await message.channel.send("They didn't cut my pizza O_O")


@slash.slash(name="quotes", guild_ids=guild_ids(), options=[
    create_option(
        name="id",
        description="Specific quote ID: There are %s quotes" % len(Quote.all()),
        option_type=4,
        required=False
    )
])
async def _quotes(ctx, id=None):
    if id:
        quote = Quote.find(int(id))
        response = quote.quote if quote else f"quote: {id} does not exist"
        hidden = bool(not quote)
        await ctx.send(response, hidden=hidden)
    else:
        choices = []
        for quote in Quote.all():
            choices.append(quote.quote)
        response = random.choice(choices)
        await ctx.send(response)


@slash.slash(name="magic-ashball", guild_ids=guild_ids())
async def _magic_ashball(ctx):
    choices = [
        "Uhhhh so like Yeah! You got this!",
        "Nope the end is near",
        "That's definitely a possibility",
        "Dont get your hopes up",
        "Oof, yeah that's not happening",
        "I'll get back to you",
        "For sure",
        "Absolutely"
    ]
    response = random.choice(choices)
    await ctx.send(response)


@slash.slash(name="help", guild_ids=guild_ids(), description="Shows information on how to use AshBot")
async def _help(ctx):
    response = (
        "Commands:\n"
        "`/help`: displays this message!\n"
        "`/magic-ashball`: Ask a question, get a mystical answer\n"
        "`/quotes`: Things only ash would say!"
    )
    await ctx.send(response, hidden=True)


client.run(TOKEN)

