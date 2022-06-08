import teksten
import acties


kamers = {'keuken': teksten.keuken, 'loggia': teksten.loggia, 'slaapkamer': teksten.slaapkamer,
		  'studio': teksten.studio, 'toilet': teksten.toilet, 'washok': teksten.washok, 'woonkamer': teksten.woonkamer}

inventaris = acties.uitvoeren('inventaris')


def print_overzicht(lijst):
	if lijst == {} or lijst == []:
		print(f'Overzicht is leeg')
	elif type(lijst) == dict:
		for key in lijst.keys():
			print(key)
	else:
		for item in lijst:
			print(item)


def print_omgeving(kamer):
	print(kamers[kamer])


if __name__ == '__main__':
	print(teksten.start)
	while True:
		instructie = input('\nGa naar: ').lower()
		if instructie == 'exit':
			break
		elif instructie == 'i':
			print_overzicht(inventaris)
		elif instructie == 'k':
			print_overzicht(kamers)
		elif instructie == 'help':
			print(teksten.spelregels)
		elif instructie in kamers:
			print_omgeving(instructie)
			acties.uitvoeren(instructie)
		else:
			print("Controleer je spelling. Bij twijfel raadpleeg de spelregels door 'help' te typen.")
