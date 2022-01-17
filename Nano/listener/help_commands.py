from discord.ext import commands

from listener.core.custom.embed import CustomEmbed


class HelpCog(commands.Cog):
    """Process commands for HelpCommand"""

    def __init__(self, client, server_prefixes: dict):
        self.client = client
        self.name = "Help"
        self.command_list_dict = self.load_command_strings()
        self.command_dict = {}
        self.load_command_dict()
        self.server_prefixes = server_prefixes

    @commands.command(name="help")
    async def help_command(self, ctx, *args):
        if args:
            args = ''.join(args)
            temp_command = self.command_dict.get(args)
            await ctx.send(embed=self.get_detail_command_embed(temp_command))
            return

        guild_id = str(ctx.guild.id)
        embed = self.get_default_help_embed()
        custom_prefix = self.server_prefixes.get(guild_id, 'None')

        if custom_prefix != 'None':
            custom_prefix = custom_prefix[0]

        embed.description += f"Custom prefix: `{custom_prefix}`"

        await ctx.send(embed=embed)

    def load_command_dict(self):
        for command in self.client.commands:
            if command.name.startswith("reload"):
                continue
            # Process command dict.
            self.command_dict[command.name] = command
            for alias in command.aliases:
                self.command_dict[alias] = command

    def load_command_strings(self) -> dict:
        temp_dictionary = {}
        for cog_name in self.client.cogs:
            command_cog = self.client.cogs[cog_name]
            cog_name = command_cog.name
            # cog_name = cog_name.replace('Cog', ' Commands')

            if cog_name == 'Owner':
                continue

            if cog_name not in temp_dictionary:
                temp_dictionary[cog_name] = ""

            for command in command_cog.get_commands():
                if command.name.startswith("reload"):
                    continue
                temp_dictionary[cog_name] += f"`{command.name}` "

        temp_dictionary['Audio Commands'] = "Audio commands can only be used using `slash command`, please use `/help` to get started."

        return temp_dictionary

    def get_default_help_embed(self) -> CustomEmbed:
        embed = CustomEmbed()

        embed.title = "Nano-Bot's Command List"

        # nano_bot = self.client.get_user(self.client.user.id)
        # embed.set_thumbnail(url=nano_bot.avatar_url)

        embed.description = "Prefix: `n>` | Alternative prefix: `@mention` the bot\n"

        for key in self.command_list_dict:
            if not self.command_list_dict[key]:
                continue
            embed.add_field(name=key, value=self.command_list_dict[key], inline=False)

        embed.add_field(name="Detail", value="For more detail, try `n>help <command-name>`", inline=False)
        # embed.add_field(name="Image Search Command", value="aliases: reddit r/ reddit_search")
        embed.add_field(name=":tools: Helpful Links",
                        value="[Invite](https://discord.com/api/oauth2/authorize?client_id=458298539517411328&permissions=8&scope=applications.commands%20bot) - "
                              "[Support Server](https://discord.gg/Y8sB4ay) - "
                              "[Vote](https://top.gg/bot/458298539517411328/vote)",
                        inline=False)

        embed.set_footer(text="For additional help, please contact Made Y#8195",
                         icon_url=self.client.user.avatar_url)
        return embed

    @staticmethod
    def get_detail_command_embed(command) -> CustomEmbed:
        embed = CustomEmbed()

        embed.title = ":bookmark: Help | " + command.name
        embed.description = "Aliases: " + ' '.join([f"`{alias}`" for alias in command.aliases])

        embed.description += "\n\n"
        if command.help:
            embed.description += command.help
        else:
            embed.description += "*No description*"

        embed.set_footer(text="Thanks for using Nano!")

        return embed
