recnik1 = open('recnik1.txt', encoding="utf-8")                   # Otvaram recnik1 sa listom reci(sva slova su mala)
inverserecnik = open('inverserecnik.txt', "w", encoding="utf-8")  # Kreiram inverserecnik fajl za upis rezultata

pomocnaLista1 = list()                                            # Kreiranje prve pomocne liste za reci
pomocnaLista2 = list()                                            # Kreiranje druge pomocne liste za reci

for rec in recnik1:                                               # Idem kroz reci u fajlu. Tacnije linija po linija
    del pomocnaLista1[:]                                          # Ovde praznim pomocnu listu pre inverzovanje redosleda slova sledece reci
    for slovo in rec:                                             # Idem kroz slova u reci.
        if slovo != '\n':                                         # Iskljucujem '\n' newline karakter
            pomocnaLista1.append(slovo)                           # Dodavanje elementa listi

    pomocnaLista2 = list(reversed(pomocnaLista1))                 # Okrecem pomocnuListu1 i upisujem u pomocnuListu2
    inverserecnik.write(''.join(pomocnaLista2) + '\n')            # Pretvaram pomocnuListu2 u string i upisujem u fajl. Bez gluposti  ] [ ,

# Zadnje dve linije mogu da budu jedna
# TODO Sortirati inverserecnik po pocetnom slovu(zadnjim slovom reci u njenom izgovoru) u 1 ili vise fajlova
# TODO Resiti dilemu da li cemo kreirati stablo od reci.
# TODO Koriscenje date strukture podataka za ispis liste reci koje se rimuju sa unetom recju
