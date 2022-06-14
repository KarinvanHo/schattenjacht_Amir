from teksten import *


kamers = {'keuken': keuken_alg, 'loggia': loggia_alg, 'slaapkamer': slaapkamer,
		  'studio': studio_alg, 'toilet': toilet_alg, 'washok': washok, 'woonkamer': woonkamer_alg}


inventaris = []
hints = set()


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


def vervolgactie(vervolg, resultaat_a, resultaat_b):
	print(vervolg)
	actie = input("Kies 'j' of 'n': ")
	if actie == 'j':
		return resultaat_a
	elif actie == 'n':
		return resultaat_b


def keuzemenu(actie1, actie2, resultaat1, resultaat2, resultaat_a=None, resultaat_b=None, vervolg1=None, vervolg2=None):
	print(actie1 + '\n' + actie2)
	keuze = input("Kies actie 1 of actie 2 of typ 'terug': ").lower()
	if keuze == 'terug':
		return
	elif keuze == str(1) and vervolg1 == 'ja':
		return vervolgactie(resultaat1, resultaat_a, resultaat_b)
	elif keuze == str(1):
		return resultaat1
	elif keuze == str(2) and vervolg2 == 'ja':
		return vervolgactie(resultaat1, resultaat_a, resultaat_b)
	elif keuze == str(2):
		return resultaat2


if __name__ == '__main__':
	print(start)
	while True:
		if len(hints) == 3:
			print(einde)
			break
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
				print(keuzemenu(keuken_actie1, keuken_actie2, keuken_resultaat1, keuken_resultaat2))
			elif instructie == 'loggia':
				if 'stofzuiger' not in inventaris:
					meenemen = keuzemenu(loggia1_actie1, loggia_actie2, loggia1_resultaat1, loggia_resultaat2)
					print(meenemen)
					if meenemen == loggia1_resultaat1:
						inventaris.append('stofzuiger')
				else:
					print(keuzemenu(loggia2_actie1, loggia_actie2, loggia2_resultaat1, loggia_resultaat2))
			elif instructie == 'woonkamer':
				if 'papiertje' not in inventaris and 'stofzuiger' not in inventaris:
					print(keuzemenu(woonkamer_actie1, woonkamer_actie2, woonkamer1_resultaat1, woonkamer_resultaat2))
				elif 'stofzuiger' in inventaris:
					stofzuigen = keuzemenu(woonkamer_actie1, woonkamer_actie2, woonkamer2_resultaat1,
										   woonkamer_resultaat2, resultaat_a=woonkamer_resultaat_a,
										   resultaat_b=woonkamer_resultaat_b, vervolg1='ja')
					print(stofzuigen)
					if stofzuigen == woonkamer_resultaat_a:
						inventaris.remove('stofzuiger')
						inventaris.append('papiertje')
						hints.add(1)
				else:
					print(keuzemenu(woonkamer_actie1, woonkamer_actie2, woonkamer3_resultaat1, woonkamer_resultaat2))
			elif instructie == 'toilet':
				if 'dood zilvervisje' not in inventaris and 'papiertje' not in inventaris:
					print(keuzemenu(toilet1_actie1, toilet_actie2, toilet1_resultaat1, toilet_resultaat2))
				elif 'papiertje' in inventaris:
					doden = keuzemenu(toilet1_actie1, toilet_actie2, toilet3_resultaat1, toilet_resultaat2,
									  resultaat_a=toilet_resultaat_a, resultaat_b=toilet_resultaat_b, vervolg1='ja')
					print(doden)
					if doden == toilet_resultaat_a:
						inventaris.remove('papiertje')
						inventaris.append('dood zilvervisje')
				else:
					print(keuzemenu(toilet2_actie1, toilet_actie2, toilet2_resultaat1, toilet_resultaat2))

		else:
			print("Controleer je spelling. Bij twijfel raadpleeg de spelregels door 'help' te typen.")
