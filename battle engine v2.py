# if you are looking for the rest of the steps, just run the game
import random

dmg = random.randint(4,7)
hp = 20
maxhp = 20
ehp = 30
edmg = random.randint(3,5)

cc = ''
name = ''
for i in range(6):
 cc = input(f'''
  NAME THE CHARACTER

 A  B  C  D  E  F  G
 H  I  J  K  L  M  N
 O  P  Q  R  S  T  U
 V  W  X  Y  Z
     {name}
''')
 name += cc.upper()
if len(name) > 6:
 input(f'''
 invalid name
 try again with a name thats less than 6 characters
 do you understand {name}?
 ''')
else:
 input(f'''
{name} WELCOME TO MY [[Game]]!!!!
PRESS [[Enter]] ON M0ST [[Text]]
''')
 input('''
* Theres a dummy standing there
 infront of you.
* Its quite menacing.
''')
 input('''
* Approach it?
Yes or Yes
''')

 while True:
  pc = input(f'''
[FIGHT][ACT][ITEM][MERCY]
 {name}  {hp}/{maxhp}
 ''')
 #fight
  if pc.lower() == 'fight':
   dmg = random.randint(4,7)
   pc2 = input('''
 * Dummy
 
 ''')
   if pc2.lower() == 'dummy':
    ehp -= dmg
    input(f'''
  * You did {dmg} damage!
  * They have {ehp} hp left!
  ''')
 #act
  elif pc.lower() == 'act':
   pc2 = input('''
 * Check
 * Talk
 ''')
   if pc2.lower() == 'check':
    input(f'''
  * Dummy ATK 0? DEF 12  
  * Its made of mostly cotton
  * Its alive too!
  ''')
   else:
    input('''
  * You tried talking to it...
  * ...
  * No response
  ''')
 #item
  elif pc.lower() == 'item':
   pc2 = input('''
 * Large cake
 
 ''')
   if pc2.lower() == 'cake':
    hp += 5 #you can change it easily
    input('''
  * You ate a tiny slice of cake
  * HP increased!
  ''')
   if hp > 20:
    hp = 20
 #mercy
  elif pc.lower() == 'mercy':
   pc2 = input('''
 * Spare
 
 ''')
   if pc2.lower() == 'spare':
    input('''
  * Nope  
  ''')
 #boss attack
  if pc.lower() == 'item':
   print()
  else:
   edmg = random.randint(3,5)
   hp -= edmg
   input(f'''
 * The dummy attacked!
 * {edmg} damage dealt!
 ''')
  if hp < 1:
   hp = 0
   input('''
 * You lost against a dummy
 * How pathetic
 ''')
 #win
  if ehp < 0:
   input('''
 * YOU WON!
 * You earned 10 XP 15 G
 ''')
 #loss
  if hp < 1:
   hp = 0
   input('''
 * You lost against a dummy
 * How pathetic
 ''')
