from teksten import *
# import acties


kamers = {'keuken': keuken_alg, 'loggia': loggia_alg, 'slaapkamer': slaapkamer,
		  'studio': studio, 'toilet': toilet, 'washok': washok, 'woonkamer': woonkamer_alg}

# inventaris = acties.uitvoeren('inventaris')
inventaris = []

def print_overzicht(lijst):
	if lijst == {} or lijst == []:
		print('\nOverzicht is leeg')
	elif type(lijst) == dict:
		for key in lijst.keys():
			print(f'- {key}')
	else:
		for item in lijst:
			print(f'- {item}')


def print_omgeving(kamer):
	print(kamers[kamer])


def keuzemenu(actie1, actie2, resultaat1, resultaat2, resultaat_a=None, resultaat_b=None, vervolg1=None, vervolg2=None):
	print(actie1 + '\n' + actie2)
	keuze = input("Kies actie 1 of actie 2 of typ 'terug': ")
	if keuze == 'terug':
		return
	elif keuze == str(1) and vervolg1 == 'ja':
		vervolg = input(resultaat1)
		print(f'TEST TEST TEST: {vervolg}')
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

if __name__ == '__main__':
	print(start)
	while True:
		instructie = input('\nGa naar: ').lower()
		if instructie == 'uitgang':
			break
		elif instructie == 'i':
			print_overzicht(inventaris)
		elif instructie == 'k':
			print_overzicht(kamers)
		elif instructie == 'help':
			print(spelregels)
		elif instructie in kamers:
			print_omgeving(instructie)
			if instructie == 'keuken':
				keuzemenu(keuken_actie1, keuken_actie2, keuken_resultaat1, keuken_resultaat2)
			elif instructie == 'loggia':
				if 'stofzuiger' not in inventaris:
					keuzemenu(loggia1_actie1, loggia_actie2, loggia_resultaat1, loggia_resultaat2)
					inventaris.append('stofzuiger')
				else:
					keuzemenu(loggia2_actie1, loggia_actie2, loggia_resultaat1, loggia_resultaat2)
			elif instructie == 'woonkamer':
				if 'stofzuiger' not in inventaris and 'papiertje' not in inventaris:
					keuzemenu(woonkamer1_actie1, woonkamer_actie2, woonkamer1_resultaat1, woonkamer_resultaat2)
				elif 'papiertje' not in inventaris:
					keuzemenu(woonkamer2_actie1, woonkamer_actie2, woonkamer2_resultaat1, woonkamer_resultaat2)
					inventaris.remove('stofzuiger')
					inventaris.append('papiertje')
				else:
					keuzemenu(woonkamer1_actie1, woonkamer_actie2, woonkamer3_resultaat1, woonkamer_resultaat2)
		else:
			print("Controleer je spelling. Bij twijfel raadpleeg de spelregels door 'help' te typen.")