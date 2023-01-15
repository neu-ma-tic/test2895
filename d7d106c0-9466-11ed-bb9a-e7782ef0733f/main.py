from replit import db
import os
import discord
from discord.ext import commands
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument
from webserver import keep_alive

# do bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!pp ', intents=intents)

# de comando
liberarResetEconomy = False
liberado = False

# de cargo
testeBot = 942196943961075753
moderador = 941896155606949889
membroAtivo = 941895729243361290

# de usuario
dono = 650025458884411423

# de canal
canalNomeTeste = 'teste-bot'
logBot = int(db['log'])

# de server
testBot = 939500700747046972
invited = 941112607467778068

# funções ----------------------------------------------------------------------------------------

async def canal(message): # para saber se o canal de resposta é o de teste
  return True if message.channel.name == canalNomeTeste or message.channel.name == 'comandos' else False

async def guild(message): # verifica se o servidor é valido
  if message.guild.id == testBot or message.guild.id == invited:
    return True
  else:
    return False

async def cargos(message): #retorna uma lista dos cargos do author da mensagem
  lista = [] 
  for cargo in message.author.roles:
    lista.append(cargo.id)
  return lista

async def pegaid(mensao): # pega o id do membro mensionado
  return f'{mensao[3:-1]}'

# eventos ----------------------------------------------------------

@bot.event # para saber quando o bot está pronto
async def on_ready():
  if not 'loja' in db.keys():
    db['loja'] = {}
  print(f'estou logado no {bot.user.name}')

@bot.event # para adicionar uma carteira a um usuario que entrou
async def on_member_join(membro):
  db[str(membro.id)] = {'pp':0,'itens':{}}
  await membro.guild.get_channel(logBot).send(f'carteira criada para {membro.mention}')

@bot.event # para deletar a carteira do usuario que saiu
async def on_member_remove(membro):
  del db[str(membro.id)]
  await membro.guild.get_channel(logBot).send(f'carteira deletada para {membro.mention}')

@bot.event
async def on_command_error(message, error):
  if isinstance(error, MissingRequiredArgument):
    await message.channel.send(f'faltando argumentos no comando, use (!pp help comando) para ver os dados do comando')
  elif isinstance(error, CommandNotFound):
     await message.channel.send('comando não encontrado, use !pp help para ver todos os comandos')
  else:
    raise error

@bot.event # para o bot n responder a ele mesmo
async def on_message(message):
  global logBot
  if message.author == bot.user:
    pass
  elif await guild(message):
    if await canal(message) and await guild(message):
      logBot = int(db['log'])
      await bot.process_commands(message)
  else:
    await message.channel.send(f'o bot {bot.user.name} não está disponivel para o seu servidor, contate Purple-Senpai#2860 para libera-lo')

# comandos livres -------------------------------------------------------------------------

@bot.command() # comando de teste
async def teste(message):
  '''testa conexão com o bot
  se a mensagem for respondida, então o bot esta online
  caso contrario o bot não esta online'''
  await message.channel.send(f'mensagem recebida de {message.author.name}.')

@bot.command() # mostra a carteira do author ou do usuario da mensão
async def carteira(message, mensao=None):
  '''vê dinheiro e itens da carteira
  usado para poder ver a sua carteira ou a carteira de algum outro membro
  pode ser usado !pp carteira para ver sua carteira
  ou !pp carteira @membro para ver a carteira de outra pessoa.'''
  if mensao == None:
    if str(message.author.id) in db.keys():
      await message.channel.send(f'você tem {db[str(message.author.id)]["pp"]}PP na sua carteira.')
      if len(db[str(message.author.id)]['itens']) == 0:
        await message.channel.send('você ainda não comprou nenhum item.')
      else:
        itens = ''
        if len(db[str(message.author.id)]['itens'].keys()) == 1:
          for item in db[str(message.author.id)]['itens'].keys():
            itens += f'{item}'
          await message.channel.send(f'você já comprou o iten: {itens}')
        else:
          for item in db[str(message.author.id)]['itens'].keys():
            itens += f'{item}, '
          await message.channel.send(f'você já comprou os itens: {itens[:-2]}')
    else:
      await message.channel.send('você não tem uma carteira.')
  else:
    idMensao = await pegaid(mensao)
    if idMensao in db.keys():
      await message.channel.send(f'{mensao} tem {db[str(idMensao)]["pp"]}PP na carteira')
      if len(db[str(idMensao)]['itens']) == 0:
        await message.channel.send(f'{mensao} ainda não comprou nenhum item.')
      else:
        itens = ''
        for item in db[str(idMensao)]['itens'].keys():
          itens += f'{item}, '
        await message.channel.send(f'{mensao} ja comprou os itens: {itens[:-2]}')
    else: # melhorar posteriormente a forma de detecção de usuario inesistente !!!!
      await message.channel.send(f'usuario {mensao} inesistente')

@bot.command() # mostra os itens a venda na loja
async def loja(message):
  '''visualizar os itens da loja
  mostra os itens dos mais antigos até os mais novos
  mostra um contador, nome do item e preço'''
  if not 'loja' in db.keys():
    db['loja'] = {}
  else:
    if len(db['loja']) == 0:
      await message.channel.send('nenhum item esta a venda na loja.')
    else:
      n = 1
      for item in db['loja']:
        await message.channel.send(f'{n}# {item}, {db["loja"][item]["preco"]}PP')
        n += 1

@bot.command() # mostra as informações de um tiem
async def iteminfo(message, nomeitem):
  '''mostra as informações de um item
  item da loja ou iventario
  !pp iteminfo nomedoitem'''
  if nomeitem in db['loja'].keys():
    await message.channel.send(f'item {nomeitem}: preco {db["loja"][nomeitem]["preco"]}PP, cargo {message.guild.get_role(db["loja"][nomeitem]["cargo"]).mention}')
  elif nomeitem in db[str(message.author.id)]["itens"].keys():
    await message.channel.send(f'item {nomeitem}: preco {db[str(message.author.id)]["itens"][nomeitem]["preco"]}PP, cargo {message.guild.get_role(db[str(message.author.id)]["itens"][nomeitem]["cargo"]).mention}')
  else:
    await message.channel.send(f'item {nomeitem} não existe')

@bot.command()
async def compraritem(message, nomeitem):
  '''compra um item da loja
  usado para comprar um item da loja, para sua carteira
  !pp compraritem nomedoitem
  seu dinheiro sera diminuido conforme o preço do item
  se não tiver dinheiro suficiente, não sera comprado
  nome do item obrigatório'''
  if not nomeitem in db['loja'].keys():
    await message.channel.send('item não encontrado.')
  elif db[str(message.author.id)]['pp'] < db['loja'][nomeitem]['preco']:
    await message.channel.send('você não tem dinheiro suficiente')
  elif db['loja'][nomeitem]['cargo'] in await cargos(message):
    await message.channel.send('você ja possue o cargo desse item')
  else:
    db[str(message.author.id)]['pp'] -= db['loja'][nomeitem]['preco']
    db[str(message.author.id)]['itens'][nomeitem] = db['loja'][nomeitem]
    await message.channel.send('item comprado')

@bot.command()
async def usaritem(message, nomeitem):
  '''usa um item do iventario
  comando para usar um item do seu iventario
  o item sera deletado do seu iventario depois o uso
  !pp usaritem nomedoitem
  nome do item obrigatório'''
  if not nomeitem in db[str(message.author.id)]['itens'].keys():
    await message.channel.send('item não encontrado na sua carteira.')
  else:
    try:
      membro = message.guild.get_member(message.author.id)
      role = message.guild.get_role(db[str(message.author.id)]['itens'][nomeitem]['cargo'])
      await membro.add_roles(role)
      del db[str(message.author.id)]['itens'][nomeitem]
      await message.channel.send('item usado.')
    except:
      await message.channel.send('cargo inesistente ou excluido.')
      db[str(message.author.id)]['pp'] =+ db[str(message.author.id)]['itens'][nomeitem]['preco']
      del db[str(message.author.id)]['itens'][nomeitem]
      await message.channel.send('dinheiro devolvido e item excluido')
      del db['loja'][nomeitem]
      await message.guild.get_channel(logBot).send(f'item {nomeitem} excluido por cargo inesistente')

@bot.command()
async def rankingpp(message):
  '''top 10 dos usuarios com mais pp
  os usuarios com 0pp não serão mensionados
  !pp rankingpp'''
  dictpp = {}
  listpp = []
  rank = ''
  for chave in db.keys():
    if chave == 'loja' or chave == 'log':
      continue
    else:
      if db[chave]['pp'] == 0:
        pass
      else:
        dictpp[int(db[chave]['pp'])] = str(chave)
  if len(dictpp) == 0:
    await message.channel.send('todos tem 0PP')
  else:
    for chave in dictpp.keys():
      listpp.append(int(chave))
    listpp.sort()
    for i in range(10):
      try:
        rank += f'{i+1}# {message.guild.get_member(int(dictpp[int(listpp[-1])])).mention} com {listpp[-1]}PP\n'
        listpp.pop()
      except:
        break
  await message.channel.send(f'{rank}')

# comandos membros ativos -----------------------------------------------------

@bot.command()
async def givepp(message, quantia, mensao):
  '''dá dinheiro a outro membro
  !pp givepp quantia @membro
  o dinheiro é retirado da sua carteira e enviado para o membro mensionado'''
  if testeBot in await cargos(message) or moderador in await cargos(message) or dono == message.author.id:
    if not str(message.author.id) in db.keys():
      await message.channel.send('você não possue uma carteira')
    else:
      if db[str(message.author.id)]['pp'] < int(quantia):
        await message.channel.send('você não tem dinheiro suficiente.')
      else:
        quantia = int(quantia)
        db[str(message.author.id)]['pp'] -= quantia
        db[await pegaid(mensao)]['pp'] += quantia
        await message.channel.send('quantia transferida')
  else:
    await message.channel.send('você não tem cargo suficiente.')

# comandos moderadores -------------------------------------------------------

@bot.command() # cria um item para colocar na loja
async def criaritem(message, nome, preco, cargo):
  '''cria um item pra loja
  cria um item para ser colocado a venda na loja
  !pp criaritem nomedoitem precodoitem @cargo
  todos parametros obrigatórios'''
  if testeBot in await cargos(message) or moderador in await cargos(message) or dono == message.author.id:
    if nome in db['loja'].keys():
      await message.channel.send('esse item já existe na loja.')
    else:
      db['loja'][nome] = {'preco':int(preco), 'cargo':int(f'{cargo[3:-1]}')}
      await message.channel.send(f'item {nome} criado.')
  else:
    await message.channel.send('você não tem cargo suficiente.')

@bot.command() # edita um item da loja
async def edititem(message, nome, novonome='none', preco='none', cargo='none'):
  '''edita um item dentro da loja
  !pp edititem nomedoitem novonome novopreco @novocargo
  se caso não quiser mudar uma das opções é só usar none
  !pp edititem nomedoitem none 50 none por exemplo
  nome do item obrigatório'''
  if moderador in await cargos(message) or testeBot in await cargos(message) or dono == message.author.id:
    if not nome in db['loja'].keys():
      await message.channel.send('esse item não existe na loja, use !pp criaritem para criar esse item')
    else:
      if novonome == 'none' and preco == 'none' and cargo == 'none':
        await message.channel.send('você escolheu mudar nada.')
      else:
        if novonome != 'none':
          db['loja'][novonome] = db['loja'][nome]
          del db['loja'][nome]
        if preco != 'none':
          db['loja'][nome]['preco'] = int(preco)
        if cargo != 'none':
          cargo = await pegaid(cargo)
          db['loja'][nome]['cargo'] = int(cargo)
        await message.channel.send('item modificado')         
  else:
    await message.channel.send('você não tem cargo suficiente.')

@bot.command() # tira um item da loja
async def delitem(message, nome):
  '''deleta um item dentro do mercado
  !pp delitem nomedoitem'''
  if moderador in await cargos(message) or testeBot in await cargos(message) or dono == message.author.id:
    if not nome in db['loja'].keys():
      await message.channel.send('esse item não existe na loja.')
    else:
      del db['loja'][nome]
      await message.channel.send('item removido.')
  else:
    await message.channel.send('você não tem cargo suficiente.')

@bot.command()
async def addpp(message, quantia, mensao=None):
  '''adiciona dinheiro a carteira
  adiciona dinheiro a sua ou na carteira de alguem
  pode ser usado !pp addpp 100 por exemplo, para adicionar 100pp na sua carteira
  ou por exemplo !pp addpp 100 @mensao para adicionar 100pp na carteira de alguem
  quantia obrigatória'''
  if moderador in await cargos(message) or testeBot in await cargos(message) or dono == message.author.id:
    quantia = int(quantia)
    if mensao == None:
      if not str(message.author.id) in db.keys():
        await message.channel.send('você não tem uma carteira.')
      elif quantia == 0:
        await message.channel.send('nada foi adicionado.')
      else:
        db[str(message.author.id)]['pp'] += quantia
        await message.channel.send(f'{quantia}pp adicionado na sua carteira')
    else:
      idmensao = await pegaid(mensao)
      if not str(idmensao) in db.keys():
        await message.channel.send(f'usuario {mensao} não encontrado.')
      elif quantia == 0:
        await message.channel.send('nada foi adicionado.')
      else:
        db[str(idmensao)]['pp'] += quantia
        await message.channel.send(f'{quantia}pp adicionado a carteira de {mensao}')
  else:
    await message.channel.send('você não tem cargo suficiente.')

@bot.command()
async def delpp(message, quantia, mensao=None):
  '''remove dinheiro a carteira
  remove dinheiro da sua ou na carteira de alguem
  pode ser usado !pp delpp 100 por exemplo, para remover 100pp na sua carteira
  ou por exemplo !pp delpp 100 @mensao para remover 100pp na carteira de alguem
  é impossivel alguem ficar com pp negativo
  quantia obrigatória'''
  if moderador in await cargos(message) or testeBot in await cargos(message) or dono == message.author.id:
    quantia = int(quantia)
    if mensao == None:
      if not str(message.author.id) in db.keys():
        await message.channel.send('você não tem uma carteira.')
      elif quantia == 0:
        await message.channel.send('nada foi retirado.')
      else:
        if db[str(message.author.id)]['pp'] >= quantia:
          db[str(message.author.id)]['pp'] -= quantia
          await message.channel.send(f'{quantia}pp retirado da sua carteira')
        else:
          await message.channel.send('pp não retirado, quantidade alta de mais, você não pode ficar com pp negativo')
    else:
      idmensao = await pegaid(mensao)
      if not str(idmensao) in db.keys():
        await message.channel.send(f'usuario {mensao} não encontrado.')
      elif quantia == 0:
        await message.channel.send('nada foi removido.')
      else:
        if db[str(idmensao)]['pp'] >= quantia:
          db[str(idmensao)]['pp'] -= quantia
          await message.channel.send(f'{quantia}pp removido da carteira de {mensao}')
        else:
          await message.channel.send(f'quantia alta demais para ser removida, o usuario {mensao} não pode ficar com pp negativo')
  else:
    await message.channel.send('você não tem cargo suficiente.')

@bot.command()
async def resetpp(message, mensao=None):
  '''reseta o dinheiro da carteira
  reseta o dinheiro da sua ou da carteira de alguem
  pode ser usado !pp resetpp para resetar o dinheiro da sua carteira
  ou por exemplo !pp resetpp @mensao para resetear o dinheiro da carteira de alguem
  quando resetado, o dinheiro da pessoa vai pra 0'''
  if moderador in await cargos(message) or testeBot in await cargos(message) or dono == message.author.id:
    if mensao == None:
      if not str(message.author.id) in db.keys():
        await message.channel.send('você não possue uma carteira.')
      else:
        db[str(message.author.id)]['pp'] = 0
        await message.channel.send('seu dinheiro foi resetado.')
    else:
      idmensao = await pegaid(mensao)
      if not idmensao in db.keys():
        await message.channel.send(f'{mensao} não possue uma carteira.')
      else:
        db[idmensao]['pp'] = 0
        await message.channel.send(f'o dinheiro de {mensao} foi resetado.')
  else:
    await message.channel.send('você não tem cargo suficiente.')

@bot.command()
async def auditpp(message, novolog=None):
  '''muda o log de mudança do bot
  !pp auditpp #novocanal
  o log são mensagens de criação e remoção de carteiras'''
  if testeBot in await cargos(message) or moderador in await cargos(message) or dono == message.author.id:
    if novolog == None:
      try:
        await message.channel.send(f'grupo usado para log é: {message.guild.get_channel(logBot).mention}')
      except:
        await message.channel.send('chat não encontrado, use !pp auditpp #chat para mudar')
    else:
      db['log'] = int(f'{novolog[2:-1]}')
      await message.channel.send('log redefinido')
      await message.guild.get_channel(db['log']).send('log redefinido')
  else:
    await message.channel.send('você não tem cargo suficiente.')

@bot.command()
async def daritem(message, nomeitem, mensao):
  '''dá um item a um membro
  !pp daritem nomedoitem @membro
  pode transferir um item do seu iventario para um membro
  o item ira sumir do seu iventario'''
  if testeBot in await cargos(message) or moderador in await cargos(message) or dono == message.author.id:
    if not str(message.author.id) in db.keys():
      await message.channel.send('você não tem uma carteira')
    else:
      if nomeitem in db[str(message.author.id)]['itens'].keys():
        db[str(await pegaid(mensao))]['itens'][nomeitem] = db[str(message.author.id)]['itens'][nomeitem]
        del db[str(message.author.id)]['itens'][nomeitem]
        await message.channel.send(f'item enviado para {mensao}')
      else:
        await message.channel.send('item não encontrado')
  else:
    await message.channel.send('você não tem cargo suficiente.')

# comandos dono ---------------------------------------------------------------

@bot.command(name='resetallwalletsforeveyone')
async def resetEconomy(message):
  '''reinicia a economia
  só pode ser usado pelo dono
  para usar o comando, é necessario usa-lo
  usar o comando de confirmação (!pp confirm)
  e usa-lo novamente'''
  if testeBot in await cargos(message) or dono == message.author.id:
    global liberarResetEconomy
    global liberado
    if liberarResetEconomy == False:
      await message.channel.send('use o comando !pp confirm para confirmar\nuse o comando !pp resetallwalletsforeveyone em seguida para efetuar a exclusão')
      liberado = True
    else:
      for chave in db.keys():
        if chave == 'loja' or chave == 'log':
          continue
        del db[chave]
      for membro in message.guild.members:
        if not membro.bot:
          db[str(membro.id)] = {'pp':0,'itens':{}}
      await message.channel.send(f'{len(db.keys())} carteiras recriadas')
      liberarResetEconomy = False
      liberado = False
  else:
    await message.channel.send('você não tem cargo suficiente.')

@bot.command()
async def confirm(message):
  '''comando de confirmação'''
  if testeBot in await cargos(message) or dono == message.author.id:
    global liberarResetEconomy
    global liberado
    if liberarResetEconomy == True:
      await message.channel.send('o comando !pp resetallwalletsforeveyone já foi liberado')
    else:
      if liberado == False:
        await message.channel.send('use o comando !pp resetallwalletsforeveyone para liberar esse comando')
      else:
        liberarResetEconomy = True
        await message.channel.send('o comando !pp resetallwalletsforeveyone foi liberado')
  else:
    await message.channel.send('você não tem cargo suficiente.')

keep_alive()
bot.run(os.environ["TOKEN"])

# arrumar os comentarios das funções para ficarem um pouco padronizadas
# arrumar para vc n comprar dar ou receber itens que vc já tem
# colocar uma função para criar a carteira quando o usuario não tiver carteira para toda função que usa ou o dinheiro do usuario ou os itens dele
# arrumar os possiveis erros de conversão de tipo de variavel
# colocar os enbeds em todas as funções
#   fazer uma função para mensagens basicos
# criar o meu próprio help usando embed
# dar uma ultima vasculhada pra ver se pode dar algum erro