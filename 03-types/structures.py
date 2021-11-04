import sys
from string import ascii_letters

with open("Veta.txt", mode='w', encoding='utf-8') as newfile:
    dinosaurus = 'Dinosauři jsou rozmanitou skupinou obratlovců řazenou mezi plazy, která dominovala fauně na pevninách této planety přes 134 milionů let v období druhohor. Dle současné systematiky patří mezi dinosaury také ptáci, kteří jsou jejich jedinou dosud žijící skupinou.'
    newfile.write(dinosaurus)

def fileRead():
    try:
        with open("Veta.txt", mode='r', encoding='utf-8') as file:
            veta = file.read()
    except FileNotFoundError:
        return f'Soubor nebyl nalezen'
    except Exception as error:
        return f'Chyba načtení souboru:{error}'
    finally:
        file.close()
    return veta

veta_vystup = fileRead()

from collections import Counter
def charFrequency():
    veta_vystup = fileRead()
    print(veta_vystup)
    veta_list = list(veta_vystup)
    counts_ascii = {}
    print(f'Počet písmenek je:')
    for item in veta_list:
        counts_ascii[item] = (counts_ascii[item] + 1) if (item in counts_ascii) else 1
    sort_orders = dict(sorted(counts_ascii.items(), key=lambda x: x[1], reverse=True))
    for i in sort_orders.items():
        print(i)
charFrequency()
