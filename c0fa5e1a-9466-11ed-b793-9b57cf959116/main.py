from random import randint
import MyKov
def Define(Word):
  if Word == '+' or Word == '-' or Word == '*' or Word == '/':
    return 'p'
  elif Word.startswith('M'):
    return 'm'
  else:
    return 'n'

def Refine(Word, Ty):
  if Ty == 'p' and Word == '+':
    return '+'
  elif Ty == 'p' and Word == '-':
    return '-'
  elif Ty == 'p' and Word == '/':
    return '/'
  elif Ty == 'p' and Word == '*':
    return '*'
  elif Ty == 'm':
    try:
      NumbCat = int(Word.strip('M'))
      if NumbCat < 1:
        NumbCat = 1
      if NumbCat > 100:
        NumbCat = 100
    except:
      NumbCat = 1
    basicnames = 'A l d e n ~ A l e c ~ A n t o n ~ A r d e n ~ A r l e n ~ A r m a n d ~ A r r o n ~ A u g u s t u s ~ A v e r y ~ B e n e d i c t ~ B e n n e t t ~ B r a n d e n ~ B r e n d o n ~ B r i t t ~ B r o d e r i c k ~ C a r t e r ~ C h a d w i c k ~ C h a d ~ C h e t ~ C o l b y ~ C o l e ~ C o r d e l l ~ D a l t o n ~ D a m i e n ~ D a n t e ~ D a r e  l l ~ D a r i u s ~ D a r r o n ~ D a r w i n ~ D e w i t t ~ D i e g o ~ D i l l o n ~ D i r k ~ D o m e n i c ~ D o n o v a n ~ D o r i a n ~ D o r s e y ~ E d i s o n ~ E l d e n ~ E l v i n ~ E r i c h ~ G a l e n ~ G a r r e t ~ G a s t o n ~ G a v i n ~ G e r m a n ~ G r a h a m ~ H a l ~   H a n k ~ H a r l a n ~ H a y d e n ~ H e r s c h e l  ~ H o y t ~ H u n  t e ~   I s a i a s ~ I s s a c ~ J a c i n t o ~ J a r r e d ~ J o n a s ~ K e n d r i c k ~ K e n e t h ~ K e n n i t h ~ K e v e n ~ L e i f ~ L e n a r d ~ L i n c o l n ~ L i n w o o d ~ L u c i u s ~ L y n w o o d ~ M a l c  o l m ~ M a l i k ~ M a x w e l l ~ M c K i n l e y ~ M e r l i n ~ M e r r i l l ~ M i c h a l ~ M o n t y ~ N e w t o n ~ N o l a n ~ P o r t e r ~ Q u i n t o n ~ R a p h a e l ~ R e i d  ~ R  o  r y ~ S c o t t y ~ S h a d ~ S t a n t o n ~ S t e f  a n ~ T h a d d e u s ~ T o b  i a s~  T r  en t o n ~ V a n c e ~ W a l k e r ~ W a l t o n ~ W e l d o n ~ W e s ~ W e s t o n ~ W i l l i a n ~ W i n f o r d ~ W y a t t'
    Hatter = ', '
    for x in range(NumbCat):
      Cheshire = MyKov.Markov(basicnames).generate_markov_text()
      Cheshire = Cheshire.split('~')
      Cheshire = Cheshire[1]
      Cheshire = Cheshire.replace(" ", "")
      if len(Cheshire) > 10:
        NumbCat += 1
      else:
        Hatter += Cheshire
        Hatter += ', '
    return Hatter
  elif Ty == 'n' and Word.startswith('L'):
    Word = Word.strip('L')
    return len(Word)
  elif Ty == 'n' and 'd' in Word:
    Word = Word.split('d')
    Tans = 0
    for x in range(0, int(Word[0])):
      Tans += randint(1, float(Word[1]))
    return Tans
  else:
    return Word

def diceMaths(Inp):
  Total = 0
  Op = '+'
  Full = ''
  for x in range(0, len(Inp)):
    Type = Define(Inp[x])
    Answ = Refine(Inp[x], Type)
    if Type == 'p':
      Op = Answ
    elif Type == 'n':
      if Op == '+':
        Total += float(Answ)
      elif Op == '-':
        Total -= float(Answ)
      elif Op == '/':
        Total /= float(Answ)
      elif Op == '*':
        Total *= float(Answ)
    Full += str(Answ)
  return Full, Total

# Imp Dice
x = True
while x == True:
  message = input('> ')
  Input = message.split(' ')
  Full, Total = diceMaths(Input)
  print(Full + ', ' + str(Total))