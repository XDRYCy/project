from argparse import ArgumentParser
import sqlite3


def pobierz_ocene():
    while True:
        grade = input('Podaj ocenę: ')
        try:
            grade = int(grade)
            if grade >= 1 and grade <= 5:
                break
            else:
                print('Wprowadź ocenę z zakresu od 1 do 5')
        except ValueError:
            print('Wprowadź liczbę całkowitą')
    return grade


def pobierz_nazwisko():
    while True:
        nazwisko = input('Podaj nazwisko: ')
        try:
            if isinstance(nazwisko, str):
                if len(nazwisko) >= 2 and nazwisko.isalpha():
                    return nazwisko
                else:
                    print('Podaj prawidłowe dane (nazwisko ma mniej niż 2 znaki)')
            else:
                print('Nazwisko musi być łańcuchem znaków. Popraw dane:')
        except ValueError:
            print('Nazwisko zawiera nieprawidłowe dane. Popraw:')

def pobierz_imie():
    while True:
        imie = input('Podaj imię: ')
        try:
            if isinstance(imie, str):
                if len(imie) >= 2 and imie.isalpha():
                    return imie
                else:
                    print('Podaj prawidłowe dane (Imie ma mniej niż 2 znaki)')
            else:
                print('Imię musi być łańcuchem znaków. Popraw dane:')
        except ValueError:
            print('Imię zawiera nieprawidłowe dane. Popraw:')


def podaj_wiek():
    while True:
        wiek = input('Podaj wiek: ')
        try:
            wiek = int(wiek)
            if wiek > 0 and wiek < 150:
                return wiek
            else:
                print('Podałeś wiek mniejszy niż 0 lub większy od 150. Popraw dane: ')
        except ValueError:
            print('Podałeś błędne dane.')


def zainteresowania():
    hobby = {1: 'sport', 2: 'motoryzacja', 3: 'psychologia', 4: 'medycyna', 5: 'informatyka', 6: 'matematyka',
             7: 'książki', 8: 'film', 9: 'muzyka'}
    for key, value in hobby.items():
        print(key, value)
    while True:
        choice = input('Wybierz jedno zainteresowanie, które najlepiej Cię opisuje (podaj numer):')
        try:
            choice = int(choice)
            if choice in hobby:
                return hobby[choice]
            else:
                print("Podaj cyfrę z przedziału 1-9")
        except ValueError:
            print('Podałeś błędne dane')


def miejsce_zamieszkania():
    miejsce = {"miasto", "wieś"}
    while True:
        print(miejsce)
        choice = input('Wybierz czy mieszkasz na wsi czy mieście: ')
        if choice in miejsce:
            return choice
        else:
            print('Twój wybór musi być podany jako "wieś" lub "miasto".')


parser = ArgumentParser(description="Aplikacja do dodawania opinii")

parser.add_argument('--install', help='Instalacja. Uwaga usunie bazę danych', action='store_true')
parser.add_argument('--add', help='Dodaj nową osobę.')
parser.add_argument('--list', help='Wypisz osoby', action='store_true')
args = parser.parse_args()

connection = sqlite3.connect('opinie.db')
cursor = connection.cursor()

if args.install:
    print('Instalacja')
    cursor.execute('DROP TABLE IF EXISTS opinie')
    cursor.execute('CREATE TABLE IF NOT EXISTS opinie(id INTEGER PRIMARY KEY AUTOINCREMENT, imie TEXT, nazwisko TEXT, opinia INTEGER, miejsce_zamieszkania TEXT, zainteresowanie TEXT)')


if args.add:
    print('Dodajemy')
    imie = pobierz_imie()
    nazwisko = pobierz_nazwisko()
    ocena = pobierz_ocene()
    a = zainteresowania()
    b = miejsce_zamieszkania()
    cursor.execute(
        "INSERT INTO opinie (imie, nazwisko, opinia, miejsce_zamieszkania, zainteresowanie) VALUES (?, ?, ?, ?, ?)",
        (imie, nazwisko, ocena, b, a))
    connection.commit()


if args.list:
    print('Wyświetlamy')
    print('ID \t Imię \t Nazwisko \t Ocena \t Miejsce zamieszkania \t Zainteresowanie')
    for id_opinii, imie, nazwisko, opinia, miejsce_zamieszkania, zainteresowanie in cursor.execute(
            'SELECT id, imie, nazwisko, opinia, miejsce_zamieszkania, zainteresowanie FROM opinie'):
        print(f'{id_opinii} \t {imie} \t {nazwisko} \t {opinia} \t {miejsce_zamieszkania} \t {zainteresowanie}')


