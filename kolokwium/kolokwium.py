# -*- coding: utf-8 -*-
"""Kolokwium.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cObK9hxpbsIfKHhRWLKCCruFB3VhgFVW

# Zasady:
- W przypadku zadań otwartych proszę umieścić kod w odpowiednich komórkach pod zadaniem (taka sama nazwa funkcji i argumentów).
- W zadaniach otwartych robią Państwo to co jest wymagane w zadaniu, nie można używać printów ani dopisywać komórek, notebook pozostaje nienaruszony oprócz tych komórek, gdzie są Państwo proszeni o napisanie kodu. Aczkolwiek komentarze są mile widziane i mogą podnieść punktację rozwiązania konkretnego zadania.
- Można oczywiście po napisaniu jakieś funkcji testować swój kod, ale w momencie oddania muszą go Państwo oddać w formie takiej jakiej dostali, oczywiście po dopisaniu rozwiązań.
- Do rozwiązania zadań zamkniętych służą odpowiednie komórki znajdujące się pod zadaniem.
- W zadaniach zamkniętych wielokrotnego wyboru odpowiedź jest zawsze prawdziwa lub fałszywa, nie mogą tu Państwo rozpatrywać żadnych przypadków.
- W zadaniach nie wolno używać funkcji z biblioteki standardowej pythona, np. max(), min() czy sum()
- Oczywiście występuje całkowity zakaz ściągania, Państwa kod i odpowiedzi będą oceniane również pod kątem pracy indywidualnej.

# Zadania Otwarte

1) Zaimplementuj funkcję, która dla dwóch list L1, L2 zwraca listę L będącą produktem dwóch list, to znaczy element nazwijmy go $a$ ze zwróconej listy L jest produktem elementów z podanych dwóch list L1, L2, to znaczy $a = b \cdot c$, gdzie $b$ to element listy L1, a $c$ to element listy L2. W przypadku, gdy podane listy mają różne długości należy użyć 1 jako brakujący element (wyjaśnienie poniżej). <br>
Przykładowe wyniki: <br>
- Na przykład dla L1 = [2,2,3,2] oraz L2=[7,5,6,7] funkcja powinna zwrócić [14, 10, 18, 14]. <br>
- Na przykład dla L1 = [2,2,3] oraz L2=[7,5,6,7] funkcja pow
inna zwrócić [14, 10, 18, 7]. <br>


Wymagania: <br>
- Funkcja powinna działać w czasie $O(n + m)$, gdzie $n$ to rozmiar L1 oraz $m$ to rozmiar L2
- Funkcja nie może modyfikować danych wejściowych (L1 i L2 nie mogą zostać naruszone)
- Złożoność pamięciowa powinna wynosić $O(n + m)$, gdzie $n$ to rozmiar L1 oraz $m$ to rozmiar L2
"""

def f(L1, L2):
    pass

"""2) Napisz funkcję, której argumentem $t$ jest krotka lub lista i, która zwraca maksymalny element z $t$. Elementami $t$ może być liczba całkowita lub krotka lub lista. W przypadku krotki lub listy (krotka lub lista nigdy nie jest pusta) funkcja powinna odwoływać się rekurencyjnie do samej siebie w celu znalezienia maksymalnego elementu. <br>
Przykładowy wynik:
- Na przykład gdy t = [1, 2, [5, 0], [1,2,3], 8, [10, [12, 1], 5]] funkcja powinna zwrócić 12. <br>

Wymagania:
- Funkcja powinna być rekurencyjna, gdy elementem $t$ jest krotka lub lista
- Funkcja nie może modyfikować danych wejściowych (t pozostaje nienaruszone)
- Złożoność pamięciowa powinna wynosić $O(1)$
"""

def max_val(t):
    pass

"""3) Napisz funkcję, której argumentem jest lista, której pierwsza połowa i druga połowa są posortowane. Funkcja powinna zwracać posortowaną listę poprzez zastosowanie procedury Merge znanej z sortowania przez scalanie. <br>
Przykładowe wyniki: <br>
- Na przykład dla arr = [2, 3, 8, -1, 7, 10] funkcja powinna zwrócić [-1, 2, 3, 7, 8, 10].
- Na przykład dla arr = [-4, 6, 9, -1, 3] funkcja powinna zwrócić [-4, -1, 3, 6, 9].

Wymagania:
- W funkcji powinno zastosować się procedurę Merge znanej z sortowania przez scalanie, nie wolno używać normalnego sortowania.
- Procedura Merge powinna być zaimplementowana jako oddzielna funkcja
- Funkcja nie może modyfikować danych wejściowych (arr pozostaje nienaruszona)
"""

def Merge_Half(arr):
    pass
def Merge(arr):
    pass

"""# Zadania zamknięte

1) Wyjaśnij szczegółowo dlaczego poniższy kod, który z matematycznego punktu widzenia jest poprawny zwraca taki wynik
"""

import math
print(math.sqrt(2) * math.sqrt(2) == 2)

"""Wyjaśnienie:

2) Zaznacz poprawne odpowiedzi dotyczące poniższej funkcji f: <br>
A) Funkcja f jest rekurencyjna <br>
B) Wywołanie funkcji f dla liczb, które mają w zapisie dwójkowym taką samą liczbę jedynek i zer daje taki sam rezultat <br>
C) Funkcja f nie wykona się, gdy n jest stringiem <br>
D) Wywołanie f(1111) dokonuje 1111 wywołań rekurencyjnych <br>
E) Złożoność pamięciowa w tym algorytmie to $O(1)$
"""

def f(n):
    s = str(n)
    if len(s) <= 1:
        return s
    return s[-1] + f(int(s[:-1]))

"""Poprawne odpowiedzi:

3) Zaznacz poprawne odpowiedzi dotyczące poniższej funkcji comp: <br>
A) Funkcja comp zawsze zwraca liczbę niedodatnią <br>
B) Funkcja comp zawsze zwraca liczbę nieujemną <br>
C) Złożoność obliczeniowa funkcji comp to $O(n^{2})$ <br>
D) Funkcja comp działa poprawnie tylko dla stringów <br>
E) Wypełnij poniższy zakomentowany assert tak, aby działał zgodnie z zaimplementowaną funkcją comp (nie wolno tu się odwoływać do samej funkcji comp)
"""

def comp(s):
    res = 0
    for c1 in s:
        res += 2
        for c2 in s:
            res -= 1
    return res
s = 'INFORMATYKA'
assert type(s) == str
# assert comp(s) == ?

"""Poprawne odpowiedzi:

4) Opisz problem sortowania słownika w Pythonie. Jak podejdziesz do tego problemu i na co zwrócisz uwagę.

Wyjaśnienie:

5) Zaznacz poprawne odpowiedzi dotyczące poniższej funkcji sort_: <br>
A) Optymistyczny czas działania poniższego algorytmu wynosi $\Omega(n^{2})$ gdzie $n$ jest długością listy arr <br>
B) Wywołanie sort_([1, 2, 5, 0]) zwraca [0, 1, 2, 5] <br>
C) Średni czas działania poniższego algorytmu wynosi $\Theta(nlogn)$ gdzie $n$ jest długością listy arr <br>
D) Algorytm ten również będzie działał poprawnie w przypadku gdy arr jest krotką <br>
E) Złożoność pamięciowa w tym programie wynosi $O(1)$
"""

def sort_(arr):
    n = len(arr)
    for i in range(n):
        t = 1
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                t = 0
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        if t == 1:
            return

"""Poprawne odpowiedzi:"""