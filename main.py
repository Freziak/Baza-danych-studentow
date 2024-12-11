import json

studenci = {}

def add(student,studenci,indeks):
    studenci[indeks] = student

try:
    file = open("dane.json","r")
    try:
        studenci = json.load(file)
    except json.decoder.JSONDecodeError:
        pass
    
    file.close()
except FileNotFoundError:
    pass

while True:

    print("\n")
    print("1. Dodaj nowego studenta")
    print("2. Edytuj dane studenta")
    print("3. Usun studenta")
    print("4. Wyswietl studenta")
    print("5. Wyjscie")
    
    choice = input("Co chcesz zrobic: ")
    print("\n")
    if choice == "1":

        indeks = input("Numer indeksu: ")
        if indeks == "":
            print("Nieprawidlowy numer indeksu.")
            continue
        if indeks in studenci:
            print("\n")
            print("Taki indeks istnieje w bazie")
            print("\n")
            continue
        name = input("Imie studenta: ")
        surname = input("Nazwisko studenta: ")
        pesel = input("Podaj pesel: ")
        location = input("Miejscowosc zamieszkania: ")
        student = {
        "imie": name,
        "nazwisko": surname,
        "pesel": pesel,
        "miejsce zamieszkania": location
        }
        add(student,studenci,indeks)

    elif choice == "2":

        indeks = input("Edytowanie danych. Podaj indeks studenta: ")

        if indeks not in studenci:
            print("W bazie danych nie ma takiego studenta.")
        else:
            for dane in studenci[indeks]:
                choice = input(f"Czy chcesz edytowac {dane}? T/N: ").lower()
                if choice == "t":
                    dana = input(f"Podaj {dane}: ")
                    studenci[indeks][dane] = dana


    elif choice == "3":

        student = input("Usuwanie studenta. Podaj indeks studenta: ")
        if student in studenci:
            del studenci[student]
            print("Student zostal usuniety.")
        else:
            print("W bazie danych nie ma takiego studenta.")
            print("\n")

    elif choice == "4":
        student = input("Wyswietlanie danych. Podaj indeks studenta: ")
        if student in studenci:
            print("\n")
            print(f"Imie: {studenci[student]["imie"]}")
            print(f"Nazwisko: {studenci[student]["nazwisko"]}")
            print(f"Pesel: {studenci[student]["pesel"]}")
            print(f"Miejsce zamieszkania: {studenci[student]["miejsce zamieszkania"]}")
            print("\n")
        else:
            print("W bazie danych nie ma takiego studenta.")
    elif choice == "5":

        try:
            file = open("dane.json","w")
            json.dump(studenci, file, indent=4)
            file.close()
        except FileNotFoundError:
            pass

        break

