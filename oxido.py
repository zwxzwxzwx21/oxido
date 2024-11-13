import requests
import os 

url_test = "https://api.openai.com/v1/chat/completions"
# otworzenie pliku w folderze, pozniej trzeba bedzie var tekst dac do content by ai go przerobilo
with open("resc artykulu.txt",'r') as tresc:
    tekst = tresc.read()
key =  "Wpisz swój klucz" ### 
headers = \
{
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}

content =   [
                f"""przekształć poniższy artykuł w opisany sposób: \n \
                - użyj tagów html jak h1, p, by tekst był odpowiednio rozmieszczony na stronie \n \
                - określ pola w których możnaby usytuować grafiki, użyj img z atrybutem src = "image_placeholder.jpg" \n \
                - do każdego pola graficznego, dodaj artybut alt wraz z dokładnym promptem, który można użyć do wygenerowania grafiki, umieść również podpisy używając odpowieniego taki html \n \
                - nie uzywaj CSS ani JavaScript, wszystko musi zawierać się wyłącznie między <body> \n \
                oto artykuł: \n {tekst}""",
                f"""wygeneruj kod HTML, który zawiera style CSS i skrypt JavaScript, umożliwiające wyświetlanie oraz wizualizację tekstu w przeglądarce. Sekcja <body> powinna być całkowicie pusta (czyli nie zawierać żadnych elementów ani tekstu), a kod CSS i JavaScript muszą być wbudowane bezpośrednio w kod HTML, ale bez treści w <body>, ani nie powinny wyświetlać żadnego tekstu na stronie."""
            
            ]
# robimy petle by robic 2 prompty, lepsza czytelnosc

prompt_number = 1
# zapisujemy artykul w stringu zeby pozniej moc go latwo wkleic do pliku podglad.html
artykul = ''
for prompt in content:
    
    data = \
    {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": prompt}]
    }
    #zmiana na string 
    response = requests.post(url_test,headers=headers,json=data)

    # interesuje nas tylko content string,

    example_text = response.json()['choices'][0]['message']['content']

    if prompt_number == 1:
        with open("artykul.html",'w') as plik:
            plik.write(example_text)
            artykul = example_text
    else:
        with open("szablon.html",'w') as plik:
            plik.write(example_text)
        with open("podglad.html",'w') as plik_2:
            plik_2.write(example_text)
    prompt_number += 1 

# zmieniamy plik podglad.html gdyz jeszcze musimy do niego wkleic nasz artykul
from bs4 import BeautifulSoup
with open("podglad.html",'r',encoding='utf-8') as plik:
    parser = BeautifulSoup(plik,"html.parser")

body_part = parser.find("body")
if body_part:
    # nie jest potrzebne ale cuda sie zdarzają
    body_part.clear()

    body_part.append(BeautifulSoup(artykul,'html.parser'))

with open('podglad.html', "w", encoding="utf-8") as plik:
    plik.write(str(parser))