import discord
import requests
import json
from discord.ext import commands

client = commands.Bot(command_prefix = "/", case_insensitive = True)

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel):
        return
    await client.process_commands(message)


@client.event
async def on_ready(): 
  print(f'[+] Yeaah, poze-bot connected!')

## START

@client.command()
async def start(ctx):
  await ctx.send(f'\n\nš šš¢š”š¦šØšš§šš¦: š\n> ā ā¢ šš£š:  /cpf 00000000000\n> ā ā¢ š§ššššš¢š”š:  /telefone 19996101067\n> ā ā¢ š”š¢š š:  /nome JAIR MESSIAS BOLSONARO\n> ā ā¢ š£šššš:  /placa ABC123\n> ā ā¢ šš”š£š:  /cnpj 00000000000000\n> ā ā¢ ššš”:  /bin 000000\n> ā ā¢ ššš£:  /cep 00000000\n> ā ā¢ š”š¢š š š£ ššš£:  /cep2 00000000\n> ā ā¢ šš£:  /ip 000000000\n> ā ā¢ šš¢š©šš š­šµ:  /covid SP\n\n')



## CPF

@client.command()
async def cpf(ctx, cpf):
  data = requests.get(f"http://ifind.chapada.com.br:7777/?token=20491c06-5675-4e06-b2ae-4e3fcda2abdd&cpf=").text

  await ctx.send(data)

 ## CNPJ

@client.command()
async def cnpj(ctx, cnpj):
  data = requests.get(f"https://www.receitaws.com.br/v1/cnpj/{cnpj}").json()
  text = "š šš¢š”š¦šØšš§š šš šš”š£š š„ššššš­ššš! š \n\n"

  try:
    error = data["error"]
    await ctx.send('ā ļø šš”š£š š”šš¢ šš”šš¢š”š§š„ššš¢!')
    return
  except Exception:
    pass

  text += f"> ā¢ šš”š£š: {data['CNPJ']}\n"
  text += f"> ā¢ š”š¢š š ššš”š§šš¦šš: {data['NOME FANTASIA']}\n"
  text += f"> ā¢ š„šš­šš¢ š¦š¢šššš: {data['RAZAO SOCIAL']}\n"
  text += f"> ā¢ š¦š§šš§šØš¦: {data['STATUS']}\n"
  text += f"> ā¢ šš”šš ššš¦šš„šššš¢: {data['CNAE PRINCIPAL DESCRICAO']}\n"
  text += f"> ā¢ šš”šš šš¢šššš¢: {data['CNAE PRINCIPAL CODIGO']}\n"
  text += f"> ā¢ ššš£: {data['CEP']}\n"
  text += f"> ā¢ ššš§š šššš„š§šØš„š: {data['DATA ABERTURA']}\n"
  text += f"> ā¢ ššš: {data['DDD']}\n"
  text += f"> ā¢ š§ššššš¢š”š: {data['TELEFONE']}\n"
  text += f"> ā¢ šš ššš: {data['EMAIL']}\n"
  text += f"> ā¢ š§šš£š¢ šš¢šš„ššš¢šØš„š¢: {data['TIPO LOGRADOURO']}\n"
  text += f"> ā¢ šš¢šš„ššš¢šØš„š¢: {data['LOGRADOURO']}\n"
  text += f"> ā¢ š”šØš šš„š¢: {data['NUMERO']}\n"
  text += f"> ā¢ šš¢š š£ššš šš”š§š¢: {data['COMPLEMENTO']}\n"
  text += f"> ā¢ šššš„š„š¢: {data['BAIRRO']}\n"
  text += f"> ā¢ š šØš”šššš£šš¢: {data['MUNICIPIO']}\n"
  text += f"> ā¢ šØš: {data['UF']}\n"
  text += f"> šØš¦šØšš„šš¢: {ctx.author}\n\n"

  await ctx.send(text)

## TELEFONE
@client.command()
async def telefone(ctx, tel):
  data = requests.get(f"https://www.dualitybuscas.org/privado/consultar_telefone_api.php?consulta={tel}").text

  await ctx.send(data)


## NOME

@client.command()
async def nome(ctx, nome1):
  nome1 = nome1.replace(" ","%20")
  data = requests.get(f"http://ifind.chapada.com.br:7777/?token=20491c06-5675-4e06-b2ae-4e3fcda2abdd&nome1=").text

  await ctx.send(data)

## NOMES POR CEP

@client.command()
async def cep2(ctx, cep2):
  data = requests.get(f"https://dualitybuscas.org/privado/cep.php?consulta={cep2}").text

  await ctx.send(data)

## PLACA

@client.command()
async def placa(ctx, placa):
  data = requests.get(f"https://dualitybuscas.xyz/privado/placa.php?consulta={placa}").text

  await ctx.send(data)
## CEP

@client.command()
async def cep(ctx, cep):
  data = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

  if data.status_code != 200:
    await ctx.send("ā ļø ššš£ š”šš¢ šš”šš¢š”š§š„ššš¢!")
    return

  data = data.json()

  text = "š šš¢š”š¦šØšš§š šš ššš£ š„ššššš­ššš! š \n\n"

  text += f"> ā¢ ššš£: {data['cep']}\n"
  text += f"> ā¢ šš¢šš„ššš¢šØš„š¢: {data['logradouro']}\n"
  text += f"> ā¢ šš¢š š£ššš šš”š§š¢: {data['complemento']}\n"
  text += f"> ā¢ šššš„š„š¢: {data['bairro']}\n"
  text += f"> ā¢ šššššš: {data['localidade']}\n"
  text += f"> ā¢ šš¦š§ššš¢: {data['uf']}\n"
  text += f"> ā¢ šššš: {data['ibge']}\n"
  text += f"> ā¢ š¦šššš: {data['siafi']}\n"
  text += f"> ā¢ ššš: {data['ddd']}\n"
  text += f"> šØš¦šØšš„šš¢: {ctx.author}\n\n"

  await ctx.send(text)

## BIN

@client.command()
async def bin(ctx, bin):
  data = requests.get(f"https://lookup.binlist.net/{bin}")

  if data.status_code != 200:
    await ctx.send("ā ļø ššš” š”šš¢ šš”šš¢š”š§š„ššš¢!")
    return

  data = data.json()
  
  text = "š šš¢š”š¦šØšš§š šš ššš” š„ššššš­ššš! š\n\n"

  text += f"> ā¢ ššš”: {bin}\n"
  text += f"> ā¢ ššš”šššš„š: {data['scheme']}\n"
  text += f"> ā¢ š§šš£š¢: {data['type']}\n"
  text += f"> ā¢ š”šš©šš: {data['brand']}\n"
  text += f"> ā¢ š£ššš¦: {data['country']['name']}\n"
  text += f"> ā¢ š¦šššš: {data['country']['alpha2']}\n"
  text += f"> ā¢ ššš”šššš„š š£ššš¦: {data['country']['emoji']}\n"
  text += f"> ā¢ š š¢ššš: {data['country']['currency']}\n"
  text += f"> šØš¦šØšš„šš¢: {ctx.author}\n\n"

  await ctx.send(text)

## IP

@client.command()
async def ip(ctx, ip):
  data = requests.get(f"http://ip-api.com/json/{ip}").json()
  text = "š šš¢š”š¦šØšš§š šš šš£ š„ššššš­ššš! š\n\n"

  if data["status"] != "success":
    await ctx.send('ā ļø šš£ š”šš¢ šš”šš¢š”š§š„ššš¢!')
    return

  text += f"> ā¢ š£ššš¦: {data['country']}\n"
  text += f"> ā¢ š¦šššš š£ššš¦: {data['countryCode']}\n"
  text += f"> ā¢ šš¦š§ššš¢: {data['regionName']}\n"
  text += f"> ā¢ š¦šššš šš¦š§ššš¢: {data['region']}\n"
  text += f"> ā¢ šššššš: {data['city']}\n"
  text += f"> ā¢ ššš£: {data['zip']}\n"
  text += f"> ā¢ ššš§šš§šØšš: {data['lat']}\n"
  text += f"> ā¢ šš¢š”ššš§šØšš: {data['lon']}\n"
  text += f"> ā¢ šš¢š„š”ššššš¢š„ šš šš”š§šš„š”šš§: {data['isp']}\n"
  text += f"> ā¢ šš š£š„šš¦š: {data['org']}\n"
  text += f"> ā¢ ššØš¦š¢ šš¢š„šš„šš¢: {data['timezone']}\n"
  text += f"> šØš¦šØšš„šš¢: {ctx.author}\n\n"
  await ctx.send(text)

## COVID

@client.command()
async def covid(ctx, covid):
  data = requests.get(f"https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{covid}").json()
  text = "š šš¢š©ššš­šµ šš„šš¦šš! š\n\n"

  try:
    error = data["error"]
    await ctx.send('ā ļø šš¦š§ššš¢ šš”š©ššššš¢!')
    return
  except Exception:
    pass

  text += f"> ā¢ šš¦š§ššš¢: {data['state']} - {data['uf']}\n"
  text += f"> ā¢ ššš¦š¢š¦: {data['cases']}\n"
  text += f"> ā¢ š š¢š„š§šš¦: {data['deaths']}\n"
  text += f"> ā¢ ššš¦š¢š¦ š¦šØš¦š£ššš§š¢š¦: {data['suspects']}\n"
  text += f"> ā¢ ššš¦š¢š¦ ššš¦ššš„š§ššš¢š¦: {data['refuses']}\n"
  text += f"> šØš¦šØšš„šš¢: {ctx.author}\n\n"

  await ctx.send(text)

## SIM OU NĆO

@client.command()
async def eu(ctx):
  data = requests.get(f"https://yesno.wtf/api/?ref=devresourc.es").json()

  text = f"{data['image']}\n"

  await ctx.send(text)

## WHATSAPP

@client.command()
async def wpp(ctx, tel):

  info = ('šÆ š¦ššØ ššš”š š£šš„š š¢ šŖššš§š¦šš£š£:\n\n')
  data = ('> https://api.whatsapp.com/send?phone=')
  text = info + data + (tel)

  await ctx.send(text)

## INSTA

@client.command()
async def insta(ctx, insta):

  info = ('š š¦ššØ ššš”š š£šš„š š¢ šš”š¦š§ššš„šš :\n\n')
  data = ('> https://www.instagram.com/')
  text = info + data + (insta)

  await ctx.send(text)

## GERADORES

## GERADOR DE CPF

@client.command()
async def gerarcpf(ctx):

    cpf = CPF()
    cpf = cpf.generate(True)

    text = ("ā¢ CPF GERADO:\n\n") + (cpf)
    await ctx.send(text)

client.run('ODg1MTgyNDgzNTk4MDIwNjI4.YTjUbQ.Sq8srAAHJnc6YlCo3UzfgECYIxw')
