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

										                                ,"  ".
										             _      .---.    _ /#     |
										           ,' `.  ,'     `.." ".      ,--.
										          |#   `/ #      (#    )    /    )
 										          `.    |         )   (`.__/    /
 										             `. \        (     )/'/    /
  										               `.\       /)   (( /    /
   										                  `.   .'(     )y    /
 										                    >_<\  `._.'(    /
 										                    /   ) /'-`.->,-'
   										                   (   ( (   (
   										                    )     )   ) 
   										                         (
I8,        8        ,8I 88888888888 88          88      a8P  ,ad8888ba,   88b           d88  
`8b       d8b       d8' 88          88          88    ,88'  d8"'    `"8b  888b         d888  
 "8,     ,8"8,     ,8"  88          88          88  ,88"   d8'        `8b 88`8b       d8'88  
  Y8     8P Y8     8P   88aaaaa     88          88,d88'    88          88 88 `8b     d8' 88  
  `8b   d8' `8b   d8'   88"""""     88          8888"88,   88          88 88  `8b   d8'  88  
   `8a a8'   `8a a8'    88          88          88P   Y8b  Y8,        ,8P 88   `8b d8'   88  
    `8a8'     `8a8'     88          88          88     "88, Y8a.    .a8P  88    `888'    88  
     `8'       `8'      88888888888 88888888888 88       Y8b `"Y8888Y"'   88     `8'     88              

Welkom bij de jaarlijkse schattenjacht ter ere van je verjaardag! 
Omdat je een hekel hebt aan wandelen, is het dit jaar een luie editie geworden.
{spelregels}
Succes! '''

einde = '''
                                       .
              . .                     -:-             .  .  .
            .'.:,'.        .  .  .     ' .           . \ | / .
            .'.;.`.       ._. ! ._.       \          .__\:/__.
             `,:.'         ._\!/_.                     .';`.      . ' .
             ,'             . ! .        ,.,      ..======..       .:.
            ,                 .         ._!_.     ||::: : | .        ',
     .====.,                  .           ;  .~.===: : : :|   ..===.
     |.::'||      .=====.,    ..=======.~,   |"|: :|::::::|   ||:::|=====|
  ___| :::|!__.,  |:::::|!_,   |: :: ::|"|l_l|"|:: |:;;:::|___!| ::|: : :|
 |: :|::: |:: |!__|; :: |: |===::: :: :|"||_||"| : |: :: :|: : |:: |:::::|
 |:::| _::|: :|:::|:===:|::|:::|:===F=:|"!/|\!"|::F|:====:|::_:|: :|::__:|
 !_[]![_]_!_[]![]_!_[__]![]![_]![_][I_]!//_:_\\![]I![_][_]!_[_]![]_!_[__]!
 ----------------------------------EINDE----------------------------------
 
Je hebt alle hints gevonden om je cadeau's te kunnen vinden! 
Hierbij nogmaals de hints:
 
hint 1:
Een papiertje met daarop geschreven: 'a needle in a HAYstack'
 
hint 2:
Het keyboard wat de volgende noten speelt:
kort lang lang lang lang pauze
lang lang kort kort kort pauze
lang lang kort kort kort pauze

hint 3:
een schilderij van Julius Caesar die een bordje vasthoudt. Op het bordje staat de letter 'V'. 

hint 4:
Bierviltjes met daarop de woorden 'mjy', 'fhmyjw', en 'ltwinos'.


Aanvullende hints zijn te koop. Succes!
'''


keuken_alg = f'''
Je begeeft je nu in de keuken. Het plankje onder de koelkast lijkt 
scheef te zitten. Verder staat de deur naar de ketel op een kier.
'''
keuken_actie1 = '1. inspecteer het plankje onder de koelkast'
keuken_actie2 = '2. inspecteer de deur naar de ketelruimte'
keuken_resultaat1 = '''
Zou het? Niet echt een originele plek voor een cadeau. Je verwijdert het plankje
en voor je het weet schiet Misha onder de koelkast. POOOEEESSSS. Je kijkt in de
ruimte maar ziet geen cadeau. Wel een stoffige kat die je er weer onderuit vist.'''
keuken_resultaat2 = '\nDoe die deur toch eens dicht! Zo kan ik de klok toch niet lezen??? En het licht uit graag.'


loggia_alg = f'''
Je bent nu in de loggia. Niks opvallend te zien.
'''
loggia1_actie1 = '1. Stofzuiger meenemen'
loggia2_actie1 = '(Je hebt de stofzuiger al meegenomen)'
loggia_actie2 = '2. Doe het licht uit zodat Karin weer rustig kan ademen op de bank.'
loggia1_resultaat1 = "\nDe stofzuiger zit nu in je inventaris."
loggia2_resultaat1 = '\nWat zeg ik nu? Je hebt de stofzuiger al meegenomen.'
loggia_resultaat2 = "\nDankjewel!"


slaapkamer_alg = f'''
In de slaapkamer is het redelijk opgeruimd. Geen hoopjes kleding waaronder iets verscholen kan zitten.
Misha snuffelt aan een vieze onderbroek die op bed ligt. Huh? Het schilderij is vervangen!
'''
slaapkamer_actie1 = '1. Bekijk het schilderij.'
slaapkamer_actie2 = '2. Geef Misha een aai.'
slaapkamer_resultaat1 = '''
Het is een schilderij van Julius Caesar die een bordje vasthoudt. Op het bordje staat de letter 'V'.
Volgens mij staat deze aanwijzing niet op zichzelf.'''
slaapkamer_resultaat2 = '''
MISHA GEAAID.
En weer door met het spel graag. Misha is er straks ook nog.'''

studio_alg = f'''
Ok, dit is freaky. In de studio speelt het keyboard uit zichzelf.
'''
studio_actie1 = '1. Actie 1'
studio_actie2 = '2. Luister aandachtig naar het keyboard'
studio_resultaat1 = '\nResultaat1'
studio_resultaat2 = '''
Er valt geen touw aan vast te knopen. Het is zeker geen deuntje. (Of is dit
experimentele black metal?) Het valt je op dat korte en lange tonen worden
afgewisseld, met pauzes tussendoor. Het klinkt als volgt:

kort lang lang lang lang pauze
lang lang kort kort kort pauze
lang lang kort kort kort pauze'''


toilet_alg = f'''
Er zit een dik zilvervisje over de toiletbril. Had je nu maar een papiertje om em te weg te halen.
'''
toilet1_actie1 = '1. Maak zilvervisje dood.'
toilet2_actie1 = '(Het zilvervisje heb je verwijderd. Wat je nu ziet is een resterend vlekje van je moordpartij)'
toilet_actie2 = '2. Scheur velletje toiletpapier af.'
toilet1_resultaat1 = '\nNiet met je blote handen viezerik! Zorg maar eerst dat je een papiertje vindt.'
toilet2_resultaat1 = '\nWat zeg ik nu? Je hebt het zilvervisje al verwijderd.'
toilet3_resultaat1 = "\nPapiertje uit inventaris gebruiken? Typ 'j' of 'n': "
toilet_resultaat2 = '\nHet is lastig zien in een tekstueel avontuur, maar het toiletpapier is OP. Jammer joh!'
toilet_resultaat_a = '''
PAPIERTJE GEBRUIKT.
Zilvervisje gedood. Maar dacht je nu echt dat je hier een hint mee kon vinden? Helaas.
Je kan wel weer lekker op de toiletbril zitten. Jammer dat het toiletpapier op is.'''
toilet_resultaat_b = '\nZolang dat zilvervisje er zit kan je geen draak uitlaten hè.'

washok_alg = f'''
Het deurtje van de wasmachine is gesloten, maar je kan je niet herinneren dat je 
een was gedraaid hebt.
'''
washok_actie1 = '1. Actie 1.'
washok_actie2 = '2. Wasmachine openen.'
washok_resultaat1 = '\nResultaat 1'
washok1_resultaat2 = "\nInhoud verwijderen? Typ 'j' of 'n': "
washok2_resultaat2 = "\n(Je hebt hier de bierviltjes gevonden met daarop de woorden 'mjy', 'fhmyjw', en 'ltwinos')"
washok_resultaat_a = '''
Geen idee waarom, maar de trommel is gevuld met bierviltjes. Je vindt 3 viltjes met daarop wat geschreven:
'mjy', 'fhmyjw', en 'ltwinos'.
'''
washok_resultaat_b = 'Maar hoe denk je dan verder te kunnen komen met dit spel?'

woonkamer_alg = f'''
De woonkamer! Genoeg te zien hier, maar valt er iets op? 
Hmmm, Misha probeert iets tussen de bank vandaan te halen.
'''
woonkamer_actie1 = '1. Inspecteer bankkussen'
woonkamer_actie2 = '2. Actie 2'
woonkamer1_resultaat1 = '\nIk zou dit niet zonder stofzuiger doen...'
woonkamer2_resultaat1 = "\nStofzuiger gebruiken? Typ 'j' of 'n'"
woonkamer3_resultaat1 = "\n(Hier heb je het papiertje gevonden met daarop de dubieuze tekst: 'a needle in a HAYstack'.)"
woonkamer_resultaat2 = '\nResultaat 2'
woonkamer_resultaat_a = '''
STOFZUIGER GEBRUIKT
Terwijl je de kruimels stofzuigt, ontdek je een papiertje. Je kan deze nog net onderscheppen 
voordat deze in de stofzuigerslang verdwijnt. Het volgende staat erop geschreven: 

--------------------------
| a needle in a HAYstack |
--------------------------

Ok.....'''
woonkamer_resultaat_b = "\nDan toch lekker niet?"

