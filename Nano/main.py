import asyncio
import os
import json

import aiohttp
import discord
from discord.ext import commands

from listener.core.client import NanoClient
from listener.general_commands import GeneralCog
from listener.help_commands import HelpCog
from listener.image_commands import ImageCog
from listener.musicv2_commands import MusicV2Cog

prefixes = ["n>"]
default_prefix = "n>"
server_prefixes = {}


def load_server_prefixes():
    global server_prefixes

    with open("prefixes.json") as f:
        server_prefixes = json.load(f)

    print(server_prefixes)


def save_server_prefixes():
    global server_prefixes

    with open('prefixes.json', 'w') as fp:
        json.dump(server_prefixes, fp)


def get_memory_config():
    intents = discord.Intents(messages=True, guilds=True)

    intents.voice_states = True
    intents.typing = False
    intents.presences = False
    intents.members = False
    intents.bans = False
    intents.integrations = False
    intents.invites = False
    intents.dm_messages = False
    intents.guild_reactions = False

    return intents


def get_prefix(bot, message):
    guild_id = str(message.guild.id)

    if guild_id in server_prefixes:
        return commands.when_mentioned_or(*server_prefixes[guild_id])(bot, message)

    return commands.when_mentioned_or(*prefixes)(bot, message)


async def main():
    global loop

    # ENVIRONMENTS
    nano_token = os.environ['NR_TOKEN']

    # Load Dependency for DI
    session = aiohttp.ClientSession()

    # Load server settings
    load_server_prefixes()

    # Configure client
    intents = get_memory_config()
    client = NanoClient(command_prefix=get_prefix, intents=intents)
    client.remove_command('help')

    # Load Cogs
    cogs = [
        GeneralCog(client=client),
        ImageCog(client=client),
        MusicV2Cog(client=client)
    ]

    # Add Cogs
    for command_cog in cogs:
        client.add_cog(command_cog)
        print(command_cog.name, "is Loaded")

    client.add_cog(HelpCog(client=client, server_prefixes=server_prefixes))

    @client.command()
    @commands.is_owner()
    async def shutdown(ctx):
        save_server_prefixes()
        await ctx.bot.logout()

    # Run Bot
    try:
        loop.run_until_complete(await client.start(nano_token))
    except Exception as e:
        await session.close()
        print('Session closed.')
        print(e)


loop = asyncio.get_event_loop()

loop.run_until_complete(main())
