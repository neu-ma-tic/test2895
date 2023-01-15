
import os
import os.path
import file

# by Jakub Grzana

guilddir = ".database"

guild_envs = dict()

# im terribly sorry for ambiguous names

def NewUserData():
    output = dict()
    output['lvl_module'] = dict()
    output['lvl_module']['level'] = 0
    output['lvl_module']['exp'] = 0
    output['lvl_module']['messages'] = 0
    output['lvl_module']['sent_message_in_this_minute'] = False
    output['warnings'] = []
    return output

def NewGuildEnvironment():
    output = dict()
    
    output['debug_channel'] = None
    output['lvl_module_verbose'] = False
    output['users'] = dict()
    output['pic_post'] = dict()
    
    output['moderation'] = dict()
    output['moderation']['channel_unsolved_cases'] = None # Channel for hate speech detection reports
    output['moderation']['channel_autoreports'] = None # Channel for "nagging moderators" - reports about users who has too many warnings
    output['moderation']['channel_user_reports'] = None # Channel for user reports
    output['moderation']['channel_archive'] = None # Archive channel
    output['moderation']['unclosed_cases'] = []
    output['moderation']['verbose_warnings'] = True
    output['moderation']['warnings_length_in_days'] = 28
    output['moderation']['warnings_to_nag'] = 3
    output['moderation']['days_until_inactive'] = 999999
    
    output['reaction_roles'] = dict()
    output['reaction_roles']['main'] = dict()
    output['reaction_roles']['message'] = (None,None) # channel_id, message_id
    
    output['supported_languages'] = { '🇵🇱' : 'pl', 
     '🇬🇧' : 'en', 
     '🇺🇸' : 'en'
    }
    
    return output
    
def RecursiveDictUpdate(dict_data, dict_temp):
    for key in dict_temp:
        if type(dict_temp[key]) == type(dict()):
            if key not in dict_data:
                dict_data[key] = dict()
            RecursiveDictUpdate(dict_data[key], dict_temp[key])
        else:
            if key not in dict_data:
                dict_data[key] = dict_temp[key]

def LoadGuildEnvironment(guild):
    if not os.path.isdir(guilddir):
        os.mkdir(guilddir)
    filepath = guilddir + "/" + str(hash(guild.id)) + ".bse"
    if not os.path.isfile(filepath):
        guild_envs[guild.id] = NewGuildEnvironment()
    else:
        guild_envs[guild.id] = file.Load(filepath)
        RecursiveDictUpdate(guild_envs[guild.id], NewGuildEnvironment())
        
def SaveGuildEnvironment(guild):
    if not os.path.isdir(guilddir):
        os.mkdir(guilddir)
    filepath = guilddir + "/" + str(hash(guild.id)) + ".bse"
    file.Save(filepath,guild_envs[guild.id])

def GetGuildEnvironment(guild):
    if guild.id in guild_envs:
        return guild_envs[guild.id]
    else:
        LoadGuildEnvironment(guild)
        return guild_envs[guild.id]

def GetUserEnvironment(local_env, user):
    if hash(user.id) in local_env['users']:
        user_env = local_env['users'][hash(user.id)]
        RecursiveDictUpdate(user_env, NewUserData()) # Well actually it is required, cause LoadGuildEnvironment won't update user data :/ Looks like it is one of weakpoints of this bot
        return user_env
    else:
        local_env['users'][hash(user.id)] = NewUserData()
        return local_env['users'][hash(user.id)]

def StripUsersData(local_env, members):
    local_env['users'] = { hash(member.id) : GetUserEnvironment(local_env, member) for member in members }
    
def GuildInfo(guild):
    local_env = GetGuildEnvironment(guild)
    info = "**Informations about guild**: " + guild.name + "\n"
    for key in local_env:
        if key == 'users':
            continue
        info = info + key + " = " + str(local_env[key]) + "\n"
    return info