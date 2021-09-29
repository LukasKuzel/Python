EARTH_GRAVITY = 9.8 #? normální pozemské tíhové zrychlení
MOON_GRAVITY = 1.62 #? měsíční gravitace
SPEED_OF_LIGHT = 300000000 #? rychlost světla ve vakuu
SPEED_OF_LIGHT_KM = 300000000*3.6
SPEED_OF_SOUND = 343 #? rychlost zvuku při teplotě 20 °C v suchém vzduchu
VENUSE_OD_ZEME = 41000000*1000 #km
RYCHLOST_STRELY_TANKU = 1800 #m/s

def EarthGravity():
    print("Výpočet gravitační síly na Zemi a Měsíci")
    m = input("Zadjete hmotnost tělesa:")
    vysledek1 = float(EARTH_GRAVITY)*float(m)
    vysledek2 = float(MOON_GRAVITY)*float(m)
    print("-------------------------------------------")
    print("Vysledek gravitační síly bude {:1.2f} N.".format(vysledek1))
    print("Gravitace na Měsíci bude {:1.2f} N.".format(vysledek2))


def SpeedOfLight():
    print("Výpočet cestovaní vesmírem na různá místa v rychlosti světla.")
    print("Jestli chcete počítat vzdálenost od Země, stiskněte 1")
    print("Jestli chcete počítat vzdálenost Země a Venuše, stiskněte 2")
    odpoved = input()
    print("-------------------------------------------")
    if odpoved == "1":
        s = input("Zadejte vzdálenost(v km):")
        t = float(s) / float(SPEED_OF_LIGHT_KM)
        print("Vaše cesta bude trvat {:1.10f} hodin".format(t))
    elif odpoved == "2":
        print("Dálka Země od Venuše")
        t = VENUSE_OD_ZEME / SPEED_OF_LIGHT_KM
        print("Vaše cesta bude trvat {:1.2f} hodin. ".format(t))
    else:
        print("Nezadali jste interval od 1 do 2.")
        exit()

def SpeedOfSound():
    print("Vypočítáme čas pomocí rychlosti zvuku.")
    s = input("Zadejte délku/neboli dráhu v metrech:")
    print("-------------------------------------------")
    vysledek1 = float(s)/float(SPEED_OF_SOUND)
    vysledek2 = (float(s) / float(SPEED_OF_SOUND))/60
    vysledek3 = ((float(s) / float(SPEED_OF_SOUND))/60)/60
    print("Váš čas bude {:.4f} sekund.".format(vysledek1))
    print("Váš čas bude {:.4f} minut.".format(vysledek2))
    print("Váš čas bude {:.4f} hodin.".format(vysledek3))

def SpeedOfTankBullet():
    print("Vypočítáme dobu letu střely z kanonu od tanku.")
    s = input("Zadejte délku/neboli dráhu v metrech:")
    print("-------------------------------------------")
    vysledek1 = float(s) / float(RYCHLOST_STRELY_TANKU)
    print("Doba letu střely bude {:.4f} sekund.".format(vysledek1))

def AllFour():
    while True:
        print("\n")
        print("Vyberte druh výpočtu:")
        print("Výpočet gravitační síly na Zemi a Měsíci. - 1")
        print("Výpočet cestovaní vesmírem na různá místa v rychlosti světla. - 2")
        print("Vypočítáme čas pomocí rychlosti zvuku. - 3")
        print("Vypočítáme dobu letu střely z kanonu od tanku. - 4")
        print("Zmáčkni 5 pro ukončení")
        print("-------------------------------------------")
        odpoved2 = input()
        if odpoved2 == "1":
            EarthGravity()
        elif odpoved2 == "2":
            SpeedOfLight()
        elif odpoved2 == "3":
            SpeedOfSound()
        elif odpoved2 == "4":
            SpeedOfTankBullet()
        elif odpoved2 == "5":
            exit()
        else:
            exit()