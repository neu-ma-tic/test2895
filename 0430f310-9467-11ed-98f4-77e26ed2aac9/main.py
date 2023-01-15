import discord
import os
from keep_alive import keep_alive

import random
import pandas as pd

import smtplib, ssl 
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart



# Built-in data storage
newcomers_id = set() # Set of newcomers'id
personal_code = dict() # Dict of users'verification_code

df_mailsis = pd.read_csv(os.getenv('EXCEL_URL') + '/export?gid=0&format=csv')['Email']
lst_mailsis = df_mailsis.values.tolist()
print(df_mailsis)

# Sub functions and variables
def send_mail(sender, receiver, bodySend):
  msg = MIMEText(bodySend, 'html')
  msg['Subject'] = 'Hi! I am Qiqi'
  msg['From'] = sender
  msg['To'] = receiver
  s = smtplib.SMTP_SSL(host = 'smtp.gmail.com', port = 465)
  s.login(user = sender, password = os.getenv('GMAILPASS'))
  s.sendmail(sender, receiver, msg.as_string())
  s.quit()

def generate_code():
  return random.randint(10000, 99999)

class EmailAddressNotIncluded(Exception):
  '''Mail user fill is not one of mails SIS of IT-E10 students'''
  pass

signing_guide_msg = f'Welcome to the server **HUST IT-E10 K65**. Now if you are a **K65 student in IT-E10 at HUST, VIE**, please type `!sign your_mailSIS` to get `verification_code` by **your mail SIS**. Otherwise, just type `!guest`'



# Bot features
class MyClient(discord.Client):
  # Check whether bot is ready
  async def on_ready(self):
    print('Logged in as')
    print(self.user.name)
    print(self.user.id)
    print('------')

  # Bot welcome and guide newcomers
  async def on_member_join(self, member):
    ch_thegreathall = self.get_channel(int(os.getenv('CHANNEL00_ID')))
    await ch_thegreathall.send(f'Greetings to you, {member.mention}! Please check your DM for instruction.')
    await member.send(signing_guide_msg)
    print(member.id)
    newcomers_id.add(member.id)

  # Bot goodbye to leavers
  async def on_member_remove(self, member):
    ch_thegreathall = self.get_channel(int(os.getenv('CHANNEL00_ID')))
    await ch_thegreathall.send(f'Farewell, {member.mention}. Best wishes!')
    try:
      del personal_code[member.id]
    except:
      pass
    else:
      newcomers_id.remove(member.id)
    
  # Bot reacts to users' messages
  async def on_message(self, msg):
    # If the msg is bot's, bot replies none
    if msg.author == self.user:
      return
    
    # Bot sends verification mail for newcomers
    elif msg.author.id in newcomers_id and msg.author.dm_channel.id == msg.channel.id:
      if msg.content.startswith('!sign'):
        try:
          verification_code = generate_code()
          receiver = msg.content.split()[1]
          if receiver not in lst_mailsis:
            raise EmailAddressNotIncluded
          sender = 'discordbothust10@gmail.com'
          bodySend = f'Dear, your verification code is {verification_code}. Regards, !steve.'
          send_mail(sender, receiver, bodySend)
          personal_code[msg.author.id] = verification_code
          await msg.author.send('Type your verification code below:')
        except IndexError:
          await msg.author.send('You may forget to type your mail SIS!')
        except EmailAddressNotIncluded:
          await msg.author.send('Your mail maybe wrong or not one of the mails of IT-E10 K65 HUST student')
        except:
          await msg.author.send('Your mail maybe wrong!')
      elif msg.content == str(personal_code.get(msg.author.id, None)):
        main_server = self.get_guild(int(os.getenv('SERVER_ID')))
        role_ITE10 = discord.utils.get(main_server.roles, name='IT-E10')
        member = main_server.get_member(msg.author.id)
        await member.add_roles(role_ITE10)
        await msg.author.send('Your role has been given. Welcome home!')
        del personal_code[msg.author.id]
        newcomers_id.remove(msg.author.id)
      elif msg.content == '!guest':
        main_server = self.get_guild(int(os.getenv('SERVER_ID')))
        role_visitor = discord.utils.get(main_server.roles, name='Visitor')
        member = main_server.get_member(msg.author.id)
        await member.add_roles(role_visitor)
        await msg.author.send('Your role has been given. Now you can visit our sever!')
        try:
          del personal_code[msg.author.id]
        except:
          pass
        newcomers_id.remove(msg.author.id)
      else:
        await msg.author.send('Something is wrong!')
      

# Main
intents = discord.Intents.default()
intents.members = True

client = MyClient(intents=intents)
keep_alive()
client.run(os.getenv('TOKEN'))