
#pobieranie n i m
n, m = input().split()

# n -> wymiary lotniska
# m -> ilosc pasow startowych (1 lub 2)

#pobranie opisu lotniska
dane_lotniska_POZIOMO = []
for el in range(int(n)):
    wolne_czy_puste = input()
    dane_lotniska_POZIOMO.append(wolne_czy_puste)

# grupowanie listy po 4 elementy
def grupowanie_po_4(lista):
    dane_lotniska_PIONOWO = []
    wyraz = ''
    i = 0
    for el in lista:
        wyraz += el
        i += 1
        if i == n:
            dane_lotniska_PIONOWO.append(wyraz)
            i = 0
            wyraz = ''
    return dane_lotniska_PIONOWO


# funkcja na znajdowanie jak najdluzszego ciagu wolnych miejsc
def znajwowanie_najdluzszego_ciagu_wolnych(lista):
    wolnych_miejsc = []
    maksymalny_ciag_wolnych_miejsc = []
    i = 0
    while i < int(n):
        wystepowanie = 0
        wolnych_miejsc = []

        for el in lista[i]:
            if el == '.':
                    wystepowanie += 1
                    wolnych_miejsc.append(wystepowanie)
            else:
                wolnych_miejsc.append(wystepowanie)
                wystepowanie = 0    
        
        wolnych_miejsc = sorted(wolnych_miejsc)
        maksymalny_ciag_wolnych_miejsc.append(wolnych_miejsc[-1]) 
        i+=1
    return maksymalny_ciag_wolnych_miejsc


# zmiana danych lotniska z POZIOMO na PIONOWO
def zmiana_na_PION(lista):
    dane_lotniska_PIONOWO = []
    d_l_osobno = []

    for el in lista:
        for x in el:
            d_l_osobno.append(x)

    indeks = 0
    pow = 0
    zwiekszanie = 1

    for el in range(0,n**2+n):
        
        if pow < n:
            dane_lotniska_PIONOWO.append(d_l_osobno[indeks])
            indeks += n
            pow += 1
        
        else:
            indeks = 0
            indeks += zwiekszanie
            zwiekszanie += 1
            pow = 0

    return dane_lotniska_PIONOWO

dane_lotniska_PIONOWO = zmiana_na_PION(dane_lotniska_POZIOMO)
dane_lotniska_PIONOWO = grupowanie_po_4(dane_lotniska_PIONOWO)


maksymalny_ciag_wolnych_pol_POZIOM = znajwowanie_najdluzszego_ciagu_wolnych(dane_lotniska_POZIOMO)
maksymalny_ciag_wolnych_pol_PION = znajwowanie_najdluzszego_ciagu_wolnych(dane_lotniska_PIONOWO)


# dla m = 1
if m == 1:
    k = 0
    for el in maksymalny_ciag_wolnych_pol_PION:
        if el > k:
            k = el
    for el in maksymalny_ciag_wolnych_pol_POZIOM:
        if el > k:
            k = el
print(k)

# dla m = 2 
if m == 2:
    pass






