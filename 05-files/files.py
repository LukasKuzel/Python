 def fileRead(path):
    try:
        with open(path, encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        return f'Soubor nebyl nalezen'
    except Exception as error:
        return f'Chyba načtení souboru: {error} {type(error)}'
    finally:
        file.close()
    return data


def fileWrite(path, data=""):
    try:
        with open(path, mode='w', encoding='utf-8') as file:
            file.write(data)
    except FileNotFoundError:
        return f'Soubor nebyl nalezen'
    except Exception as error:
        return f'Chyba zápisu do souboru: {error} {type(error)}'
    finally:
        file.close()
    return True


obsah = fileRead('./python.txt')
print(obsah)
print(fileWrite('./kopie.txt', data=obsah))