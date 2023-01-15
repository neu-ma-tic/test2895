from discord.ext import commands
import random


class _8ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["8ball", "8b"])
    async def _8ball(self, ctx, question):
        await ctx.send(f"{ctx.author.mention} {random.choice(responses)}")


def setup(bot):
    bot.add_cog(_8ball(bot))


responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "No and u gay",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]