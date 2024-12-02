R = 13.6
h = 4.135667696e-15
c = 3.0e8
def czy_foton_pochloniety(energia_fotonu):
    for n1 in range(1, 20):  # sprawdzam poziomy od 1 do 21, bo pozniejsze przejscia maja energie mniejsza niz 0,01 a program ma liczyc z ta dokadnoscia
        for n2 in range(n1 + 1, 21):
            delta_E = R * (1 / n1**2 - 1 / n2**2)
            if round(delta_E, 2)==energia_fotonu:
                return True
    return False

def emisja_fali(dlugosc_fali):
    energia = round((h * c) / (dlugosc_fali * 1e-9),2)
    if czy_foton_pochloniety(energia) == True:
        return True
    return False

#masymalna energia (miedzy n=1 a n=21) i minimalna energia (miedzy n=20 a n=21)
maksi = round(13.6*(1 / 1**2 - 1 / 21**2),2)
mini = round(13.6*(1 / 20**2 - 1 / 21**2),2)


mini_dl = 91.2


print("Zadanie 1")
print("Wprowadz energie fotonu w Ev z dokładnością do 2 miejsc po przecinku, w przeciwnym razie program zaokrągli ją do 2 miejsc:")
while True:
    try:
        e_u = round(float(input()), 2)
        if e_u>0 and e_u>=mini and e_u<=maksi:
            if czy_foton_pochloniety(e_u)==True:
                print("Ten foton może zostać pochłonięty")
            else:
                print("Tego fotonu nie można pochłonąć")
            break
        elif e_u<mini or e_u>maksi:
            print("Wartość musi zawierać się w przedziale od ", mini, " Ev do ", maksi, " Ev")
        else:
            print("Energia musi być liczbą dodatnią")
    except ValueError:
        print("Podano niepoprawną wartość energii. Wprowadź liczbę zmiennoprzecinkową większą od 0")

print("Zadanie 2")
print("Wprowadz dlugosc fali elektormagnetycznej w nanometrach z dokładnością do 2 miejsc po przecinku, w przeciwnym razie program zaokrągli ją do 2 miejsc:")
while True:
    try:
        dlugosc = round(float(input()),2)
        if dlugosc>mini_dl:
            if emisja_fali(dlugosc) == True:
                print("Atom wodoru może wyemitować falę o tej długości")
            else:
                print("Atom wodoru nie może wyemitować fali o tej długości")
            break
        else:
            print("Dlugosc fali musi byc liczbą większą od teoretycznej minimalnej długości fali (91.2 nm)")
    except ValueError:
        print("Podano niepoprawną wartość dlugości fali. Wprowadź liczbę zmiennoprzecinkową większą od teoretycznej minimalnej długości fali (91.2 nm)")

print("Zadanie 3")
print("Wprowadz kolejno w dwoch wierszach numery orbit poczatkowej i koncowej")
while True:
    try:
        n1 = int(input())
        n2 = int(input())
        if n1==n2:
            print("Atom nie wyemituje żadnej fali, ponieważ różnica poziomów energetycznych wynosi 0")
            break
        elif n1 >= 0 and n2 >= 0:
            dl = abs(round((h * c) / (R * (1 / n1 ** 2 - 1 / n2 ** 2) * 1e-9), 2))
            print("Długość fali wynosi: ", dl, " nm", end="")
            if n1 < n2:
                print(", nastąpiła absorbcja")
            else:
                print(", nastąpiła emisja")
            break
        else:
            print("Numery orbit muszą być liczbami całkowitymi nieujemnymi")
    except ValueError:
        print("Podano niepoprawną wartośc numeru jednej lub obu orbit. Wprowadz liczby całkowite nieujemne")
