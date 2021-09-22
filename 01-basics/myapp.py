vysledek = 0
print("Tohle je znalostní quiz!!")

print("Co je to Python?")
print("a: Vejce na tvrdo")
print("b: Had")
print("c: Programovací jazyk")
print("d: Nemoc vlasů")

print("Jaká je vaše odpověď: ?")
odpoved = input()
if odpoved == "c":
    print("Správne")
    vysledek=vysledek+1
else:
    print("Špatně")

print("Co je to YAML?")
print("a: Druh lamy")
print("b: Pocit radosti")
print("c: Zvuk při žvýkání")
print("d: Formát")

print("Jaká je vaše odpověď: ?")
odpoved = input()
if odpoved == "d":
    print("Správne")
    vysledek=vysledek+1
else:
    print("Špatně")

print("Co je to JavaScript?")
print("a: Multiplatformní, objektově orientovaný, událostmi řízený skriptovací jazyk.")
print("b: Interpretovaný skriptovací programovací jazyk")
print("c: Služba s předplaceným obsahem")
print("d: Internetová sociální síť")

print("Jaká je vaše odpověď: ?")
odpoved = input()
if odpoved == "a":
    print("Správne")
    vysledek=vysledek+1
else:
    print("Špatně")

print("Co je to XML?")
print("a: Video přehrávač")
print("b: Obecný značkovací jazyk")
print("c: Značková obuv")
print("d: Lék proti rakovině")

print("Jaká je vaše odpověď: ?")
odpoved = input()
if odpoved == "b":
    print("Správne")
    vysledek=vysledek+1
else:
    print("Špatně")

from playsound import playsound
print("Tvuj vysledek spravnych odpovedi je: {}".format(vysledek))
if vysledek == 4:
    print("VÝBORNĚĚ!!!! MÁŠ PLNÝ POČET BODŮ!")
    playsound('victory.mp3')
elif vysledek == 3:
    print("Pěkně. Máš skoro plný počet podů.")
    playsound('victory.mp3')
elif vysledek == 2:
    print("Máš se hodně co učit")
    playsound('nice.mp3')
else:
    print("Zklamal jsi tuto třídu a svého učitele. Mazej se učit.")
    playsound('stupid.mp3')

