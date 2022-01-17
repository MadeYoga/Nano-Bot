from random import choice

from discord.ext import commands
from .core.subreddit import anime_subreddits
from listener.core.base import BaseImageCog


class AnimeImageCog(BaseImageCog):

    def __init__(self):
        super().__init__()
        self.name = "Anime Commands"
        self.load_pools(anime_subreddits)

    @commands.command(name="reload_anime_pool")
    @commands.is_owner()
    async def reload_anime_pool_command(self, ctx):
        self.load_pools(anime_subreddits)
        await ctx.send(":white_check_mark: | Reloaded, anime image pools!")
        return

    @commands.cooldown(1, 1, commands.BucketType.guild)
    @commands.command(name="moescape")
    async def moescape_command(self, ctx):
        """Get random post (anime wallpaper) from /r/Moescape

        **Usage**
        ```
        n>moescape
        ```
        """

        submission = choice(self.pools["MOESCAPE"])

        await self.reply_context(ctx=ctx, submission=submission)

    @commands.cooldown(1, 1, commands.BucketType.guild)
    @commands.command(name="tsun")
    async def tsun_command(self, ctx):
        """Get random post (anime wallpaper) from /r/Tsunderes

        **Usage**
        ```
        n>tsun
        ```
        """

        submission = choice(self.pools["TSUNDERES"])

        await self.reply_context(ctx=ctx, submission=submission)

    @commands.cooldown(1, 1, commands.BucketType.guild)
    @commands.command(name="aniwallp")
    async def aniwallp_command(self, ctx):
        """Get random anime wallpaper from /r/Animewallpaper

        **Usage**
        ```
        n>aniwallp
        ```
        """

        submission = choice(self.pools["ANIMEWALLPAPER"])

        await self.reply_context(ctx=ctx, submission=submission)

    @commands.cooldown(1, 1, commands.BucketType.guild)
    @commands.command(name="animeme", aliases=["animemes"])
    async def animeme_command(self, ctx):
        """Get random animeme from /r/Animemes

        **Usage**
        ```
        n>animeme
        n>animemes
        ```
        """

        submission = choice(self.pools["ANIMEMES"])

        await self.reply_context(ctx=ctx, submission=submission)

    @commands.cooldown(1, 1, commands.BucketType.guild)
    @commands.command(name="waifu")
    async def waifu_command(self, ctx):
        """Get random waifu from /r/Waifu

        **Usage**
        ```
        n>waifu
        ```
        """

        submission = choice(self.pools["WAIFU"])

        await self.reply_context(ctx=ctx, submission=submission)

    @commands.cooldown(1, 1, commands.BucketType.guild)
    @commands.command(name="awwnime", aliases=["awnime"])
    async def awwnime_command(self, ctx):
        """Get random awwnime from /r/awwnime

        **Usage**
        ```
        n>awwnime
        ```
        """

        submission = choice(self.pools["AWWNIME"])

        await self.reply_context(ctx=ctx, submission=submission)

    @commands.cooldown(1, 1, commands.BucketType.guild)
    @commands.command(name="hololive")
    async def hololive_command(self, ctx):
        """Get random awwnime from /r/Hololive

        **Usage**
        ```
        n>hololive
        ```
        """

        submission = choice(self.pools["HOLOLIVE"])

        await self.reply_context(ctx=ctx, submission=submission)

    @commands.cooldown(1, 1, commands.BucketType.guild)
    @commands.command(name="hololivememes")
    async def hololive_memes_command(self, ctx):
        """Get random awwnime from /r/hololivememes

        **Usage**
        ```
        n>hololivememes
        ```
        """

        submission = choice(self.pools["HOLOLIVEMEMES"])

        await self.reply_context(ctx=ctx, submission=submission)
