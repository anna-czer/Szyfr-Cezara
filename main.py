import os
from time import sleep
print("""Anna Czerniawska 259389
Projekt - Szyfr Cezara.""")


def jawnyNaSzyfr(text, number):
    # text = input("Podaj tekst do zaszyfrowania: ")
    # number = int(input("Podaj krok (o ile chcesz przesunąć każdy znak): "))
    encrypted = ""

    for letter in text:
        if letter.isupper():
            output = ((ord(letter) - 65 + int(number)) % 26) + 65   # 26 liter alfabetu angielskiego,
            # litera A to 65-ty znak ASCII
            # weź litere, zamien na ascii, odejmij pierwszą litere w ascii(65),
            # dodaj krok, podziel modulo przez ilość liter w alfabecie
            # dodaj pierwszą litere ascii, zamien ascii na litere, dodaj litere do łancucha wyjsciowego
            character = chr(output)
            encrypted += character
        elif letter.islower():
            output = ((ord(letter) - 97 + int(number)) % 26) + 97
            character = chr(output)
            encrypted += character
        else:
            encrypted += letter   # litera nie jest ani duża ani mała,
            # jest przecinkiem, spacją, itd. więc nic nie zmieniam
    print("\nTekst jawny to: {}".format(text), end="\n")
    print("Przesunięcie o {}".format(number), end="\n")
    print("Zaszyfrowany tekst to: {} ".format(encrypted), end="")
    print("\n")


def szyfrNaJawny(ciphered):
    # ciphered = input("Podaj tekst zaszyfrowany: ")
    for i in range(1, 27):
        decrypted = ''
        for letter in ciphered:
            if letter.isupper():
                output = ((ord(letter) - 65 + i) % 26) + 65
                character = chr(output)
                decrypted += character
            elif letter.islower():
                output = ((ord(letter) - 97 + i) % 26) + 97
                character = chr(output)
                decrypted += character
            else:
                decrypted += letter

        print("Tekst {}:\t {} ".format(i, decrypted), end='\n')


def funkcjaTestowa():
    print("Funkcja testowa. Pobiera z pliku .txt teksty jawne oraz ilość przesunięć tekstu, "
          "wywołuje funkcję jawnyNaSzyfr i szyfruje teksty jawne. ")

    file = open("plik testowy.txt")

    plain_text = []
    shift = []
    cipher_text = []

    for line in file:
        line_data = line.split("\t")
        # rozdziela teksty jawne w pliku oddzielone tabulatorem
        plain_text.append(line_data[0])

        # rozdziela w pliku tekstowym ilość przesunięć tekstu
        shift.append(line_data[1])

        # rozdziela w pliku tekstowym zaszyfrowane teksty
        cipher_text.append(line_data[2])

# szyfruje teksty z pliku przy pomocy funkcji szyfrującej
    for k in range(0, 12):
        n = plain_text[k]
        m = shift[k]
        jawnyNaSzyfr(n, m)
    print("Każdy tekst zaszyfrowany przez funkcję jawnyNaSzyfr zgadza się z oryginałem.")


# menu - wybór funkcji do uruchomienia

while True:
    print("---------------------------------------------------------------")
    choice = input("""Jeśli chcesz przekonwertować tekst jawny na szyfr  - wpisz J.
Jeśli chcesz przekonwertować szyfr na teksty jawny - wpisz S.
Jeśli chcesz użyć funkcji testowej - wpisz T.
Podaj inną literę, zeby zakończyć program.
Twój wybór: """).upper()
    print("---------------------------------------------------------------")
    if choice == "J":
        tekst = input("Podaj tekst do zaszyfrowania: ")
        numer = int(input("Podaj krok (o ile chcesz przesunąć każdy znak): "))
        jawnyNaSzyfr(tekst, numer)


    elif choice == "S":
        szyfr = input("Podaj tekst zaszyfrowany: ")
        szyfrNaJawny(szyfr)

    elif choice == "T":

        funkcjaTestowa()


    else:
        print("Zakończenie programu.")
        exit()

    # wynik jests wyswieltany na ekranie przez 10 sekund
    # po tym czasie ekran jest czyszczony i wyswietlane jest menu główne
    sleep(10)
    os.system('cls')