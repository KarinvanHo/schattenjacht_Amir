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
				print("helemaal opnieuw schrijven")
			elif instructie == 'woonkamer':
				print("helemaal opnieuw schrijven")

		else:
			print("Controleer je spelling. Bij twijfel raadpleeg de spelregels door 'help' te typen.")