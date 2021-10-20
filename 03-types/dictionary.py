'''
Slovníky (dictionaries) podobně jako seznamy v sobě obsahují další hodnoty.
Na rozdíl od seznamů, ve kterých jsou všechny prvky uspořádané do jedné sekvence, ve slovnících máme dva druhy prvků:
klíč (angl. key) a hodnotu (angl. value).
Každému klíči je přiřazena jedna hodnota.
'''

# Collection which is unordered, changeable and indexed.
# In Python dictionaries are written with curly brackets, and they have keys and values.
from turtledemo.chaos import f

car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}

point = {'x': 1, 'y': 10}

# Vytvoření slovníku pomocí konstruktoru dict()
point = dict(x=1, y=10)

# Změna hodnoty jednoho prvku slovníku
point['x'] = 2

# Vložení nového prvku do slovníku
point['z'] = 20

# Přístup k položkám slovníku
print(f'point["x"]: {point["x"]}')
print(f'point.get("x"): {point.get("x")}')

# Zjištění, zda existuje hodnota
if 'z' in point:
    print(f'point.get("z"): {point.get("z")}')

# Když hodnota neexistuje, vrací 0    
print(f'point.get("v", 0): {point.get("v", 0)}')

# Odstranění prvku ze slovníku  
del point['x']
print(f'point: {point}')

print(f'car.pop(): {car.pop("model")}')

# Odstraní poslední prvek ze slovníku
print(f'car.popitem(): {car.popitem()}')

# Procházení slovníkem - vypíše vždy pár klíč - hodnota
for key, value in point.items():
    print(f'{key} - {value}')

# Dictionary comprehension - zkráceně vytvoří slovník, jehož klíče tvoří čísla od 0 do 9 a hodnoty druhé mocniny 
values = {x: x ** 2 for x in range(10)}
print(f'values: {values}')

# Unpacking operator - pro slovníky se používají **
first = {'x': 1, 'y': 2}
second = {'x': 10, 'z': 5}
common = {**first, 'a': 15, **second}
print(f'common: {common}')

# Nested dictionary - vnořené slovníky
myfamily = {
  'child1' : {
    'name' : 'Emil',
    'year' : 2004
  },
  'child2' : {
    'name' : 'Tobias',
    'year' : 2007
  },
  'child3' : {
    'name' : 'Linus',
    'year' : 2011
  }
}
# print(f'Nested dictionary myfamily: {myfamily}')

# ??? 4. cvičení ???
# a) Navrhněte vlastní vnořený slovník tvořený 3 reálnými objekty s aspoň 6 klíči tak, abyste kromě jednoduchých
# datových typů (čísla, řetězce, boolean) ve slovníku vhodně využili i všechny v tomto bloku probrané strukturované
# typy - tedy set, tuple a list.
# Volte příklad vycházející z reality - např. slovník aut, slovník filmů, slovník historických postav atd.
# b) Pomocí vhodných metod přidejte do slovníku nový prvek a nějaký starý naopak odstraňte
# c) Proveďte výpis obsahu slovníku tak, aby i v konzoli vytvořil hezky naformátovanou tabulku i s mezerami
# viz níže uvedený vzor.
'''
Slovník myfamily
---------------------------------------------
child           name                year
---------------------------------------------
child1          Emil                2004
child2          Tobias              2007
child3          Linus               2011
---------------------------------------------
Počet záznamů: 3
'''

denikKnizek = {
  'Projekt Kronos' : {
    'nazevk' : 'Projekt Kronos', 'autor' : 'Pavel Bareš',
    'zanr' : 'Romány, Literatura česká, Sci-fi',
    'rok' : '2017',
    'hodnoceni' : '86%',
    'info' : 'Být hrdinou není ve skutečnosti ani zdaleka takové, jak se o tom píše v komiksech… Píše se rok 2052 a to málo, co po válce ze světa zbylo, halí šero nukleární zimy. Attiona City, jednu z posledních výsep lidské civilizace, zevnitř požírá záhadná epidemie a společenské rozkoly. Zatímco prominentní občané v horní části města se vzpamatovávají z válečných hrůz, méně šťastní obyvatelé spodního Downtownu je stále prožívají. Drogový byznys jen kvete, ulicím vládnou konkurenční gangy a zoufalí Downtowneři se ocitají v čím dál větší izolaci. To vše jsou ale jen první výstřely do tmy předznamenávající občanskou válku. Mladý Downtowner Jason Blake vždycky toužil být hrdinou. A teď se mu — k jeho smůle — tohle přání beze zbytku vyplní. Naproti tomu Luco Scarpa nikdy nechtěl nic jiného než prožít svůj život v klidu a míru. Přesto má pod taktovkou nejmocnější organizace světa lovit právě takové lidi, jako je Jason. A ačkoli o tom ani jeden z nich nemá nejmenší tušení, brzy se z nich mají stát pouhé figurky šachové partie, ve které se hraje o osud celého města.'
  },
  'Jméno větru' : {
    'nazevk' : 'Jméno Větru',
    'autor' : 'Patrick Rothfuss',
    'zanr' : 'Literatura světová, Romány, Fantasy',
    'rok' : '2017',
    'hodnoceni' : '92%',
    'info' : 'Jmenuji se Kvothe. Unášel jsem spícím mohylovým králům ukradené princezny. Spálil jsem město Trebon. Strávil jsem noc s Felurian a odešel živý a při smyslech. Byl jsem vyloučen z Univerzity ve věku mladším, než na ni lidé obvykle vstupují. Mluvil jsem s bohy, miloval ženy a skládal písně, při kterých minstrelové vzlykali. Možná jste o mně slyšeli.Tak začíná Kvothův příběh - od jeho dětství strávené ve skupině potulných herců, přes léta prožitá jako polodivoký sirotek na ulicích zločinem prolezlého města až po drzý a nepřehlédnutelný vstup do obtížného a nebezpečného studia magie na slavné Univerzitě. Na samém počátku však Kvotha potkáváme již jako zkušeného mága, zručného zloděje, suverénního muzikanta a neblaze proslulého vraha.Ale ve Jménu větru se toho o něm skrývá mnohem víc, vždyť jde o pravdivé zobrazení událostí skrývajících se za legendou o Kvothovi Královrahovi.'
  },
  'Píseň krve' : {
    'nazevk' : 'Píseň Krve',
    'autor' : 'Anthony Ryan',
    'zanr' : 'Literatura světová, Romány, Fantasy',
    'rok' : '2014',
    'hodnoceni': '92%',
    'info' : 'Vélin Al Sorna, zasvěcený Šestému řádu, byl od dětství cvičen k boji a zabíjení ve službách Víry. Řád se stal jeho jedinou rodinou. Vélinův otec sloužil jako rytíř králi Janusovi, panovníkovi Sjednoceného království, rozhodl se však Vélina zbavit jeho práv a v pouhých deseti letech ho zanechal na prahu Šestého řádu. Chlapec ho za to nenávidí. Během pobytu v řádu se Vélin dozvídá zatím netušené podrobnosti o své matce, která zemřela, když byl ještě dítě. Postupně také odhaluje důvody, jež jeho otce vedly k tomu, že ho řádu svěřil. Jedna pravda je však důležitější než všechny ostatní: Vélina Al Sornu čeká budoucnost, kterou má teprve pochopit. Budoucnost, jež změní nejen království, ale také celý svět.'
  },
  'Vlčí krev' : {
    'nazevk' : 'Vlčí krev',
    'autor' : 'Michaela Burdová',
    'zanr' : 'Literatura česká, Fantasy, Pro děti a mládež',
    'rok' : '2013',
    'hodnoceni' : '81%',
    'info' : 'Vydejme se do Velwetie, tajemné země obývané Temnovlky – nesmrtelnými bytostmi, ze kterých jde strach a lidé jsou pro ně pouhou kořistí. Minulost vlkodlaka Nerana, nazývaného Syn pekel, je s Temnovlky pevně svázaná. Pouze čarovný nektar Étarlininy slzy by mu mohl pomoci se odpoutat a zvrátit svůj osud. Musí uzavřít spojenectví s elfkou Liadel, kterou ze srdce nenávidí. Podaří se mu odhalit její tajemství? Bude Neranovi odpuštěna dávná zrada? Ve Velwetii mezitím propuká boj temných sil – třinácti démonů. Neran je vtažen do bitvy o moc. Kdo zvítězí, rozhodne o osudu celé země.'
  }
}



# value_one = denikKnizek['Projekt Kronos']
# value_two = denikKnizek['Jméno větru']
# value_three = denikKnizek['Píseň krve']
# value_four = denikKnizek['Vlčí krev']
# new_denik_knizek = {}
# for key, value in denikKnizek.items():
#   new_denik_knizek[key] = value
#   print(new_denik_knizek[key])
#
# for value_one in new_denik_knizek[key].values():
#   print(value_one)

#print(f'Nested dictionary denikKnizek: {denikKnizek["Projekt Kronos"]}')
import sys
print(f'Knihy:')
print(f'-------------------------------------------------------------------------------------------------------------------------------')
print(f'|Název knihy           autor                      žánr                        rok      hodnocení                          info|')
print(f'-------------------------------------------------------------------------------------------------------------------------------')
def get_all():
  pocet_zaznamu=0
  for value_one in denikKnizek.values():
    for value_two in value_one.values():
      print(value_two,'   |  ', end='')
    print('\n')
    pocet_zaznamu = pocet_zaznamu + 1
  print(f'-------------------------------------------------------------------------------------------------------------------------------')
  print(f'Počet knih v seznamu je: {pocet_zaznamu}')
  print('\n')
get_all()

# for value_one in denikKnizek['Projekt Kronos'].values():
#   print(value_one ,'   |  ',end='')
# print('\n')

#
del denikKnizek['Vlčí krev']
denikKnizek['Rod země a krve'] = {'nazevk' : 'Rod země a krve', 'autor' : 'Sarah J. Maas', 'zanr' : 'Literatura světová, Romány, Fantasy','rok' : '2020', 'hodnoceni' : '93%', 'info' : 'Bryce je 25 a žije už dva roky sama po záhadné vraždě svých přátel. Případ byl uzavřen a považován za ukončený dokud o dva roky později vrah neudeří znovu a nezabije další lidi naprosto stejným způsobem. Bryce se stane hlavní podezdřelou neboť každou z obětí viděla jako poslední. Aby dokázala svou nevinu musí případ vyřešit a tak dostane tvz. ochránce a pomocníka Hunta Athalara. Společně pátrají a pravda, která vyjde najevo by je ani v nejdivočejších snech nenapadla.'}
print(f'Knihy:')
print(f'-------------------------------------------------------------------------------------------------------------------------------')
print(f'|Název knihy           autor                      žánr                        rok      hodnocení                          info|')
print(f'-------------------------------------------------------------------------------------------------------------------------------')
def get_all_two():
  pocet_zaznamu = 0
  for value_one in denikKnizek.values():
    for value_two in value_one.values():
      print(value_two,'   |  ', end='')
    print('\n')
    pocet_zaznamu = pocet_zaznamu + 1
  print(f'-------------------------------------------------------------------------------------------------------------------------------')
  print(f'Počet knih v seznamu je: {pocet_zaznamu}')
  print('\n')
get_all_two()

