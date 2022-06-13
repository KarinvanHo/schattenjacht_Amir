import time
from teksten import *

inventaris = []


def keuzemenu(actie1, actie2, resultaat1, resultaat2, resultaat_a, resultaat_b, vervolg1=None, vervolg2=None):
	print(actie1 + '\n' + actie2)
	keuze = input('Kies actie 1 of actie 2: ')
	if keuze == str(1) and vervolg1 == 'ja':
		vervolg = input(resultaat1)
	elif keuze == str(1):
		print(resultaat1)
		vervolg = None
	elif keuze == str(2) and vervolg2 == 'ja':
		vervolg = input(resultaat2)
	elif keuze == str(2):
		print(resultaat2)
		vervolg = None
	if vervolg == 'j':
		print(resultaat_a)
	elif vervolg == 'n':
		print(resultaat_b)


def uitvoeren(kamer):
	if kamer == 'inventaris':
		return inventaris
	# acties keuken
	if kamer == 'keuken':
		while True:
			keuzemenu(keuken_actie1, keuken_actie2, keuken_resultaat1, keuken_resultaat2, keuken_resultaat_a,
					  keuken_resultaat_b)
	# 			keuze = input('''
	# 1. inspecteer het plankje onder de koelkast
	# 2. inspecteer de deur naar de ketelruimte
	# Kies actie 1 of 2 of typ 'terug'\n
	# actie: ''')
	# 			if keuze == str(1):
	# 				print('''
	# Zou het? Niet echt een originele plek voor een cadeau. Je verwijdert het plankje
	# en voor je het weet schiet Misha onder de koelkast. POOOEEESSSS. Je kijkt in de
	# ruimte maar ziet geen cadeau. Wel een stoffige kat die je er weer onderuit vist.''')
	# 				time.sleep(2)
	# 			elif keuze == str(2):
	# 				print('''
	# Doe die deur toch eens dicht! Zo kan ik de klok toch niet lezen??? En het licht uit graag.''')
	# 				time.sleep(2)
	# 			elif keuze == 'terug':
	# 				break
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
	# acties woonkamer
	elif kamer == 'woonkamer':
		while True:
			keuze = input('''
1. inspecteer bankkussen
2. actie 2
Kies actie 1 of 2 of typ 'terug'\n
actie: ''')
			if keuze == str(1):
				if 'stofzuiger' not in inventaris and 'papiertje' not in inventaris:
					print('''
Ik zou dit niet zonder stofzuiger doen...''')
				elif 'papiertje' not in inventaris:
					stofzuiger = input("Stofzuiger uit je inventaris gebruiken? Typ 'j' of 'n': ").lower()
					if stofzuiger == 'j':
						print('''
STOFZUIGER GEBRUIKT
Terwijl je de kruimels stofzuigt, ontdek je een papiertje. Je kan deze nog net onderscheppen 
voordat deze in de stofzuigerslang verdwijnt. Het volgende staat erop geschreven: 

--------------------------
| a needle in a HAYstack |
--------------------------

Ok.....''')
						inventaris.remove('stofzuiger')
						inventaris.append('papiertje')
					else:
						print('Dan toch lekker niet?')
				else:
					print(
						"(Hier heb je het papiertje gevonden met daarop de dubieuze tekst: 'a needle in a HAYstack'.)")
				time.sleep(2)
			elif keuze == str(2):
				print('''
actie 2 gedaan''')
				time.sleep(2)
			elif keuze == 'terug':
				break
	############# hier volgt nog slaapkamer! ############
	# acties studio
	elif kamer == 'studio':
		while True:
			keuze = input('''
1. luister aandachtig naar de piano.
2. actie 2
Kies actie 1 of 2 of typ 'terug'\n
actie: ''')
			if keuze == str(1):
				print('''
Er valt geen touw aan vast te knopen. Het is zeker geen deuntje. (Of is dit
experimentele black metal?) Het valt je op dat korte en lange tonen worden
afgewisseld, met pauzes tussendoor. Morse code! Het klinkt als volgt:

... ___ ...  HIER LOCATIE IN MORSE CODE TYPEN''')
				time.sleep(2)
			elif keuze == str(2):
				print('''
actie 2 gedaan''')
				time.sleep(2)
			elif keuze == 'terug':
				break

# acties KAMER
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
