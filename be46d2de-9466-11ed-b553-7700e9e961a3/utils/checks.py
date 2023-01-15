from discord.ext import commands

from utils.manager import main_data

class NoProfile(commands.CheckFailure):
    """ Exception raise when Player doesn't have a profile yet. """
    pass

class HasProfile(commands.CheckFailure):
    """ Exception raise when Player have profile. """
    pass


def has_profile():
    async def predicate(ctx: commands.Context):
        if str(ctx.author.id) in main_data:
            return True
        raise NoProfile()
    
    return commands.check(predicate)

def has_no_profile():

    async def predicate(ctx: commands.Context):
        if str(ctx.author.id) not in main_data:
            return True
        raise HasProfile()
    
    return commands.check(predicate)