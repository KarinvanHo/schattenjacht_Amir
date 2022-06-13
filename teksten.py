spelregels = '''
*****************
* De spelregels *
*****************
- Je kan de ruimtes in je huis bezoeken door de naam van de kamer in te voeren.
- Voor een overzicht van alle kamers, typ in het 'ga naar'-veld 'k'.
- Zodra je een kamer bezoekt kan je twee acties uitvoeren. Dit kan iets inspecteren 
  zijn, of iets in je inventaris stoppen.
- Je inventaris open je door in het 'ga naar'-veld 'i' te typen. 
- Wil je de spelregels opnieuw inzien? Typ 'help'.
- Wil je het spel verlaten? Typ 'uitgang'
'''

start = f'''
Welkom bij de jaarlijkse schattenjacht ter ere van je verjaardag! 
Omdat je een hekel hebt aan wandelen, is het dit jaar een luie editie geworden.
{spelregels}
Succes! '''


keuken_alg = f'''
Je begeeft je nu in de keuken. Het plankje onder de koelkast lijkt 
scheef te zitten. Verder staat de deur naar de ketel op een kier.'''
keuken_actie1 = '1. inspecteer het plankje onder de koelkast'
keuken_actie2 = '2. inspecteer de deur naar de ketelruimte'
keuken_resultaat1 = '''
Zou het? Niet echt een originele plek voor een cadeau. Je verwijdert het plankje
en voor je het weet schiet Misha onder de koelkast. POOOEEESSSS. Je kijkt in de
ruimte maar ziet geen cadeau. Wel een stoffige kat die je er weer onderuit vist.'''
keuken_resultaat2 = 'Doe die deur toch eens dicht! Zo kan ik de klok toch niet lezen??? En het licht uit graag.'


loggia_alg = f'''
Je bent nu in de loggia. Niks opvallend te zien.'''
loggia1_actie1 = '1. Stofzuiger meenemen'
loggia2_actie1 = '(Je hebt de stofzuiger al meegenomen)'
loggia_actie2 = '2. Doe het licht uit zodat Karin weer rustig kan ademen op de bank.'
loggia_resultaat1 = "De stofzuiger zit nu in je inventaris."
loggia_resultaat2 = "Dankjewel!"


slaapkamer = f'''
Je begeeft je nu in de slaapkamer.
'''

studio = f'''
Ok, dit is freaky. In de studio speelt het keyboard uit zichzelf.
'''

toilet = f'''
Je begeeft je nu in het toilet.
'''

washok = f'''
Je begeeft je nu in het washok.
'''

woonkamer_alg = f'''
De woonkamer! Genoeg te zien hier, maar valt er iets op? 
Hmmm, Misha probeert iets tussen de bank vandaan te halen.
'''
woonkamer_actie1 = '1. Inspecteer bankkussen'
woonkamer_actie2 = '2. Actie 2'
woonkamer1_resultaat1 = 'Ik zou dit niet zonder stofzuiger doen...'
woonkamer2_resultaat1 = "Stofzuiger gebruiken? Typ 'j' of 'n'"
woonkamer3_resultaat1 = "(Hier heb je het papiertje gevonden met daarop de dubieuze tekst: 'a needle in a HAYstack'.)"
woonkamer_resultaat2 = 'Resultaat 2'
woonkamer_resultaat_a = '''
STOFZUIGER GEBRUIKT
Terwijl je de kruimels stofzuigt, ontdek je een papiertje. Je kan deze nog net onderscheppen 
voordat deze in de stofzuigerslang verdwijnt. Het volgende staat erop geschreven: 

--------------------------
| a needle in a HAYstack |
--------------------------

Ok.....'''
woonkamer_resultaat_b = "Dan toch lekker niet?"

