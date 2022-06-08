import time

inventaris = []

def uitvoeren(kamer):
  if kamer == 'inventaris':
    return inventaris
  # acties keuken
  if kamer == 'keuken':
    while True:
      keuze = input('''
1. inspecteer het plankje onder de koelkast
2. inspecteer de deur naar de ketelruimte
Kies actie 1 of 2 of typ 'terug'\n
actie: ''')
      if keuze == str(1):
        print('''
Zou het? Niet echt een originele plek voor een cadeau. Je verwijdert het plankje
en voor je het weet schiet Misha onder de koelkast. POOOEEESSSS. Je kijkt in de
ruimte maar ziet geen cadeau. Wel een stoffige kat die jer weer onderuit vist.''')
        time.sleep(2)
      elif keuze == str(2):
        print('''
Doe die deur toch eens dicht! Zo kan ik de klok toch niet lezen??? En het licht uit graag.''')
        time.sleep(2)
      elif keuze == 'terug':
        break
  # acties loggia
  if kamer == 'loggia':
    while True:
      if 'stofzuiger' not in inventaris:
        keuze = input('''
  1. Neem de stofzuiger mee
  2. actie 2
  Kies actie 1 of 2 of typ 'terug'\n
  actie: ''')
        if keuze == str(1):
          inventaris.append('stofzuiger')
          print('''
  Stofzuiger aan inventaris toegevoegd''')
          time.sleep(2)
        elif keuze == str(2):
          print('''
  actie 2 gedaan''')
          time.sleep(2)
        elif keuze == 'terug':
          break
      else:
        keuze = input('''
1. (Stofzuiger heb je al meegenomen)
2. actie 2
Kies actie 1 of 2 of typ 'terug'\n
actie: ''')
        if keuze == str(2):
          print('''
actie 2 gedaan ''')
          time.sleep(2)
        elif keuze == 'terug':
          break
#   # acties KAMER
#   elif kamer == 'KAMER':
#     while True:
#       keuze = input('''
# 1. actie 1
# 2. actie 2
# Kies actie 1 of 2 of typ 'terug'\n
# actie: ''')
#       if keuze == str(1):
#         print('''
# actie 1 gedaan''')
#         time.sleep(2)
#       elif keuze == str(2):
#         print('''
# actie 2 gedaan''')
#         time.sleep(2)
#       elif keuze == 'terug':
#         break