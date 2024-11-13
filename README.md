### Instrukcja uruchomienia

1. *Wystarczy otworzyć kod w interpreterze i uruchomić go*.
- Można również otworzyć go za pomocą terminala wpisując "cmd" w lokalizacji plików a następnie wpisując "python oxido.py".
- W przypadku braku bibliotek należy zainstalować "requests" i "bs4" nie umieszczam ich w osobnym pliku gdyż zostałem o to poproszony.

### Sposób działania

1. Na początku skrypt łączy się z OpenAI poprzez mój klucz API.
2. Tworzony jest placeholder, który będzie przetrzymywać wynik naszej odpowiedzi od AI, można zrezygnować z jego użytku, ale żeby lepiej opisać co się dzieje, postanowiłem, że go zostawię.
3. Otrzymany tekst wpisujemy w plik artykul.html
4. Importujemy bs4 i szukamy części <body> w naszym pliku szablon.html i czyścimy go (co nie jest konieczne, ale jeśli podmieni sie plik, wszystko i tak zadziała) i wpisujemy do niego nasz artykuł

#### Stary sposób działania (wraz z generowaniem plików szablon.html i podglad.html)

1. Na początku skrypt łączy się z OpenAI poprzez mój klucz API.
2. Utworzona jest flaga, która sprawdza do którego pliku powinien być wpisany wynik naszych promptów.
3. Tworzony jest placeholder, który będzie przetrzymywać wynik jednego z promptów, gdyż jest on potrzebny później, a nie chcemy by został on nadpisany.
4. Następnie iterujemy przez każdy prompt w pętli, pierwszy wytwarza nam treść przekształconego artykułu, po czym zmienia flage, by z następną iteracją, ta wpisała wartość drugiego prompta w inne pliki.
5. Po wyjściu z pętli mamy już utworzone nasze 3 pliki, ale podglad.html jest wybrakowany, ponieważ nie ma jeszcze wpisanego artykułu, robimy więc to po pętli:
- Otwieramy plik i szukamy części <body> w kodzie HTML
- Czyścimy wszystko co jest w części body (kod generowany jest przez AI, więc jest szansa, że treść polecenia w którym zakazane jest wpisywanie jakiegokolwiek kodu, mogłabyć po prostu ominięta, urok pracy z AI :) )
- Dopisujemy do części <body> nasz artykuł i wpisujemy do w podglad.html

#### Uwagi

GitHub blokuje klucze jeśli te zostaną załączone z kodem, więc postanowiłem swojego klucza API nie dołączać, by wszystko dobrze działało, wystarczy w variable "key" wpisać swój własny klucz (linia 8)