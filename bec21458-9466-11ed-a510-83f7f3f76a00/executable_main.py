
import os 
import discord # Discord API
from discord.ext import tasks
from discord.ext import commands
from dotenv import load_dotenv # ENV vars
from discord.ext.commands import has_permissions, MissingPermissions
import traceback

# by Jakub Grzana

load_dotenv() # load environmental variables from file .env

import data
import log
import moderation
import translator
import levels
import pic_poster
import temp
import reaction_roles
from discord.ext.commands import CommandNotFound

version = "JG Zeke bot\n\
Version 0.0.1"

intents = discord.Intents.default()
intents.members = True
DiscordClient = commands.Bot(command_prefix='jg',intents=intents) # create client of discord-bot

################################### INTERNAL ###################################

@DiscordClient.event
async def on_error(event, *args, **kwargs):
    print("UNHANDLED EXCEPTION")
    print(event)
    print(traceback.format_exc())
    
@DiscordClient.event
async def on_command_error(ctx, error):
    await ctx.message.reply(str(error))
  
def cmd_error(reason):
    return f'Command error occured\n\
    Reason: {reason}'
    
async def cmd_results(ctx,result):
    if result[0]:
        await ctx.message.add_reaction('👍')
    else:
        await ctx.message.reply(cmd_error(result[1]))

################################################################################


#################################### TIMER #####################################

async def save_guild_data(bot, local_env, guild, minute):
    data.SaveGuildEnvironment(guild)

# ( minutes, func(bot, local_env, guild, minute) )
# minutes < 100000
Timers = []
Timers.append( (60, moderation.RemoveOutdatedWarnings) )
Timers.append( (1440, moderation.NagModerators) )
Timers.append( (60, save_guild_data) )
Timers.append( (1, levels.OneMinutePassed) )
Timers.append( (1, pic_poster.Pass) )
Timers.append( (1440, moderation.SearchForInactiveChannels) )

minute = -1
@tasks.loop(minutes=1)
async def each_minute():
    global minute
    # purge temporary dir, once per day
    if abs(minute) % 1440 == 180:
        print("Purging temporary directory")
        temp.PurgeTempDir()
    # Timers
    for (m,func) in Timers:            
        if abs(minute) % m == 0:
            for guild in DiscordClient.guilds:
                local_env = data.GetGuildEnvironment(guild)
                try:
                    await func(DiscordClient, local_env, guild, minute)
                except Exception as e:
                    await log.Error(DiscordClient, e, guild, local_env, { 'minute': minute } )
                    print("Exception in each_minute: " + str(e))
    minute = minute + 1 % 100000

################################################################################


################################## TRIGGERS ####################################

#@DiscordClient.event
#async def on_member_join(member):
#    local_env = data.GetGuildEnvironment(member.guild)
#    if hash(memeber.id) not in local_env['users']:
#        local_env['users'][hash(member.id)] = data.NewUserData()

@DiscordClient.event
async def on_message(message):
    if message.author.bot:
        return
    # enforce execution of commands
    await DiscordClient.process_commands(message)
    try: # guild message
        local_env = data.GetGuildEnvironment(message.guild)
        try:
            await levels.Pass(DiscordClient,local_env, message)
            await moderation.Pass(DiscordClient,local_env,message) # takes a lot of time, should be done last
        except Exception as e:
            await log.Error(DiscordClient, e, message.guild, local_env, { 'message' : message } )
    except: # private message
        pass 
    
@DiscordClient.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return 
    #print(reaction.emoji)
    local_env = data.GetGuildEnvironment(reaction.message.guild)
    try:
        await translator.Pass(DiscordClient, local_env, reaction, user)
        await reaction_roles.AddEmoji(DiscordClient, local_env, reaction, user)
    except Exception as e:
        await log.Error(DiscordClient, e, reaction.message.guild, local_env, { 'reaction' : reaction, 'user' : user } )

@DiscordClient.event        
async def on_reaction_remove(reaction, user):
    if user.bot:
        return 
    #print(reaction.emoji)
    local_env = data.GetGuildEnvironment(reaction.message.guild)
    try:
        await reaction_roles.RemoveEmoji(DiscordClient, local_env, reaction, user)
    except Exception as e:
        await log.Error(DiscordClient, e, reaction.message.guild, local_env, { 'reaction' : reaction, 'user' : user } )

###########################################################################


############################# REACTION ROLES ##############################

@DiscordClient.command(name='reaction_role_add', help="TODO")
@has_permissions(administrator=True)
async def cmd_reaction_role_add(ctx, emoji):
    local_env = data.GetGuildEnvironment(ctx.guild) 
    try:
        result = reaction_roles.AddRole(local_env, emoji, ctx.message.raw_role_mentions[0])
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {'context' : ctx} )

@DiscordClient.command(name='reaction_role_remove', help="TODO")
@has_permissions(administrator=True)
async def cmd_reaction_role_remove(ctx, emoji):
    local_env = data.GetGuildEnvironment(ctx.guild) 
    try:
        result = reaction_roles.RemoveRole(local_env, emoji)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {'context' : ctx} )
 
@DiscordClient.command(name='reaction_role_tmp_set', help="TODO")
@has_permissions(administrator=True)
async def cmd_raction_role_tmp(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild) 
    try:
        result = reaction_roles.SetMessage(local_env, ctx.message)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {'context' : ctx} )

###########################################################################


################################ GENERIC ##################################

@DiscordClient.command(name='save', help="Save data of this server (setup, userdata, warnings and so on)")
@has_permissions(administrator=True)
async def cmd_save(ctx):
    try:
        data.SaveGuildEnvironment(ctx.guild)
        result = (True,None)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, None, {'context' : ctx} )
        
@DiscordClient.command(name='strip_user_data', help="Remove all data of users who're no longer in this server")
@has_permissions(administrator=True)
async def cmd_strip(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild) 
    try:
        data.StripUsersData(local_env,ctx.guild.members)
        result = (True,None)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {'context' : ctx} )
        
@DiscordClient.command(name='version', help="Display version of bot")
async def cmd_version(ctx):
    try:
        await ctx.message.reply(version)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, None, {'context' : ctx} )
        
@DiscordClient.command(name='vars', help="Display variables of current guild")
async def cmd_vars(ctx):
    try:
        to_send = data.GuildInfo(ctx.guild)
        await ctx.message.reply(to_send)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, None, {'context' : ctx} )
        
###########################################################################


################################# LEVELS ##################################

@DiscordClient.command(name='level_leaderboard', help="Display level tierlist")
async def cmd_leaderboard(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        to_send = levels.RequestLevelList(local_env, ctx.guild.members)
        await ctx.message.reply(to_send)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {'context' : ctx} )

@DiscordClient.command(name='level_verbose', help="Display level tierlist")
@has_permissions(administrator=True)
async def cmd_verbose(ctx, verbose: bool):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = levels.SetVerbose(local_env, verbose)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {'context' : ctx} )

###########################################################################


############################### PIC POSTER ################################

@DiscordClient.command(name='pic_post_add', help="Add new pic_poster")
@has_permissions(administrator=True)
async def cmd_pic_post_add(ctx, internal_name, timer: int, keyword):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = pic_poster.AddPicPoster(DiscordClient, local_env, ctx.guild, internal_name, timer, ctx.channel.id, keyword.replace("_"," "))
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, { 'internal_name' : internal_name} )
        
@DiscordClient.command(name='pic_post_remove', help="Remove existing pic_poster")
@has_permissions(administrator=True)
async def cmd_pic_post_remove(ctx, internal_name):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = pic_poster.RemovePicPoster(DiscordClient, local_env, ctx.guild, internal_name)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, { 'internal_name' : internal_name} )
    
@DiscordClient.command(name='pic_post_keyword_add', help="Add to existing pic_poster keyword to search for")
@has_permissions(administrator=True)
async def cmd_pic_post_keyword_add(ctx, internal_name, keyword):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = pic_poster.AddSearchWord(DiscordClient, local_env, ctx.guild, internal_name, keyword.replace("_"," "))
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, { 'internal_name' : internal_name} )
        
@DiscordClient.command(name='pic_post_keyword_remove', help="Remove keyword from existing pic_poster")
@has_permissions(administrator=True)
async def cmd_pic_post_keyword_remove(ctx, internal_name, keyword):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = pic_poster.RemoveSearchWord(DiscordClient, local_env, ctx.guild, internal_name, keyword.replace("_"," "))
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, { 'internal_name' : internal_name} )
        
################################################################################


################################## MODERATION ##################################

@DiscordClient.command(name='mode_get', help="Get warnings of user")
@has_permissions(administrator=True)
async def cmd_mode_get(ctx, user):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = await moderation.GetUserWarnings(local_env, ctx.message.mentions[0], ctx.message)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )
    
@DiscordClient.command(name='mode_warn', help="Give warning to user")
@has_permissions(administrator=True)
async def cmd_mode_warn(ctx, user_id, reason):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = await moderation.AddWarning(local_env, ctx.message.mentions[0], reason.replace("_"," "))
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )
    
@DiscordClient.command(name='mode_channel', help="Set this channel as moderation channel")
@has_permissions(administrator=True)
async def cmd_mode_channel(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = moderation.SetModChannel(local_env, ctx.channel)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )

@DiscordClient.command(name='mode_ur_channel', help="Set this channel as channel for user report")
@has_permissions(administrator=True)
async def cmd_mode_ur_channel(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = moderation.SetUserReportsChannel(local_env, ctx.channel)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )

@DiscordClient.command(name='mode_nagging', help="Set this channel as channel to nag moderators")
@has_permissions(administrator=True)
async def cmd_mode_nagging(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = moderation.SetNaggingChannel(local_env, ctx.channel)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )
    
@DiscordClient.command(name='mode_archive', help="Set this channel as mod-archive channel")
@has_permissions(administrator=True)
async def cmd_mode_archive(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = moderation.SetArchiveChannel(local_env, ctx.channel)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )

@DiscordClient.command(name='mode_solve', help="Solve existing case")
@has_permissions(administrator=True)
async def cmd_mode_solve(ctx, case_id: int, confirmation: bool):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = await moderation.CaseSolve(DiscordClient,local_env, case_id, confirmation)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )
        
@DiscordClient.command(name='mode_purge', help="Remove all unclosed cases without solving them")
@has_permissions(administrator=True)
async def cmd_mode_purge(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = moderation.PurgeUnclosedCases(local_env)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )

@DiscordClient.command(name='mode_show_report', help="Show all users exceeding given number of warnings")
@has_permissions(administrator=True)
async def cmd_show_report(ctx, num: int):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        await ctx.channel.send( moderation.RequestWarnReport(local_env, ctx.guild, num)[0] )
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )

@DiscordClient.command(name='mode_disable', help="Purge uncloded cases and remove moderation channels")
@has_permissions(administrator=True)
async def cmd_mode_disable(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = moderation.DisableModeration(local_env)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )

@DiscordClient.command(name='mode_param_set', help="Set parameters for warning management")
@has_permissions(administrator=True)
async def cmd_mode_param_set(ctx, number_of_warning: int, length_in_days: int, verbose_warnings: bool):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = moderation.SetParameters(local_env, number_of_warning, length_in_days, verbose_warnings)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )
        
@DiscordClient.command(name='mode_inactive_days', help="TODO")
@has_permissions(administrator=True)
async def cmd_mode_inactive_days(ctx, days_until_inactive: int):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = moderation.SetDaysUntilInactive(local_env, days_until_inactive)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )

@DiscordClient.command(name='report', help="Report message to moderators")
async def cmd_mode_param_set(ctx, message_id: int):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        message = await ctx.channel.fetch_message(message_id)
        result = await moderation.ReportMessage(DiscordClient, local_env, ctx.message, message)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {} )

################################################################################


################################# DEBUG TOOLS ##################################

@DiscordClient.command(name='debug', help="Debug, will be removed")
@has_permissions(administrator=True)
async def cmd_debug(ctx):
    local_env = data.GetGuildEnvironment(ctx.guild)
    print("Minute: " + str(minute))
    print("Last error: " + str(traceback.format_exc()))
    print(local_env)
        
@DiscordClient.command(name='channel', help="Debug, will be removed")
@has_permissions(administrator=True)
async def cmd_channel(ctx, channel_internal_name):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        local_env[channel_internal_name] = ctx.channel.id
        #print(local_env)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, {'context' : ctx} )

################################################################################


################################# TRANSLATION ##################################

@DiscordClient.command(name='lang_add', help="Add emoji-to-translate")
@has_permissions(administrator=True)
async def cmd_lang_add(ctx,emoji,language):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = translator.AddEmojiTranslation(DiscordClient,local_env,emoji,language)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, { 'emoji' : emoji, 'language': language} )

@DiscordClient.command(name='lang_remove', help="Remove emoji-to-translate")
@has_permissions(administrator=True)
async def cmd_lang_remove(ctx,emoji):
    local_env = data.GetGuildEnvironment(ctx.guild)
    try:
        result = translator.RemoveEmojiTranslation(DiscordClient,local_env,emoji)
        await cmd_results(ctx,result)
    except Exception as e:
        await log.Error(DiscordClient, e, ctx.guild, local_env, { 'emoji' : emoji } )

################################################################################


################################ INITIALISATION ################################

@DiscordClient.event
async def on_ready():
    print("Connected. Loading data\n")
    for guild in DiscordClient.guilds:
        data.LoadGuildEnvironment(guild)
        local_env = data.GetGuildEnvironment(guild)
    log.PurgeLogDir()
    
    each_minute.start()
    print("Initialisation finished")
    print(f'{DiscordClient.user} has connected to Discord!')
    print("Number of servers (guilds) bot is connected to: "+str(len(DiscordClient.guilds)))


print("Startup finished. Connecting...")
DiscordClient.run("Nzg5Nzc2Njg1Njg3MTExNzAw.X92-2w.pODbXozIacE3ABdqDwUBOneqxrc")