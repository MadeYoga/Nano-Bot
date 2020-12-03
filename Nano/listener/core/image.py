import random

import praw

from . import config


class Subreddits:
    MEMES = "memes"
    DANKMEMES = "dankmemes"
    WTF = "wtf"
    GRANDORDER = "grandorder"
    WAIFU = "Waifu"
    SCATHACH = "scathach"
    FGOFANART = "FGOfanart"
    ANIME = "anime"
    ANIMEMES = "Animemes"
    AWWNIME = "awwnime"
    AZURELANE = "AzureLane"
    TSUNDERES = "Tsunderes"
    ANIMEWALLPAPER = "Animewallpaper"  # ANIME WALLPAPER ARTS
    MOESCAPE = "Moescape"  # ANIME WALLPAPER ARTS
    MAMARAIKOU = "MamaRaikou"
    SABER = "Saber"
    FGOCOMICS = "FGOcomics"
    FATEPRISMAILLYA = "FatePrismaIllya"
    ILLYASVIEL = "Illyasviel"


class Reddit:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=config.REDDIT_CLIENT_ID,
            client_secret=config.REDDIT_CLIENT_SECRET,
            user_agent=config.REDDIT_USER_AGENT
        )

    def get_submission(self, subreddit):
        submissions = list(self.reddit.subreddit(subreddit).hot())
        while True:
            submission = random.choice(submissions)
            if not submission.stickied and '.' in str(submission.url)[-5:]:
                break
        return submission

    def search_post(self, keyword):
        return self.reddit.subreddit('all').search(keyword)

    def search_get_post(self, keyword):
        # REGEX FOR IMAGE URL
        # (?:([^:/?#]+):)?(?://([^/?#]*))?([^?#]*\.(?:jpg|gif|png))(?:\?([^#]*))?(?:#(.*))?
        submissions = list(self.reddit.subreddit('all').search(keyword))
        while True:
            submission = random.choice(submissions)
            if not submission.stickied and '.' in str(submission.url)[-5:]:
                break
        return submission
