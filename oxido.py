import requests
import os 
# it does conenct and works just fine
url_test = "https://api.openai.com/v1/chat/completions"
# otworzenie pliku w folderze, pozniej trzeba bedzie var tekst dac do content by ai go przerobilo
with open("resc artykulu.txt",'r') as tresc:
    tekst = tresc.read()
key =  "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"
headers = \
{
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
content = f"""przekształć poniższy artykuł w woniższy sposób: \n \
            - użyj tagów html jak h1, p, by tekst był odpowiednio rozmieszczony na stronie \n \
            - określ pola w których możnaby usytuować grafiki, użyj img z atrybutem src = "image_placeholder.jpg" \n \
            - do każdego pola graficznego, dodaj artybut alt wraz z dokładnym promptem, który można użyć do wygenerowania grafiki, umieść również podpisy używając odpowieniego taki html \n \
            - nie uzywaj CSS ani JavaScript, wszystko musi zawierać się wyłącznie między <body> \n \
            oto artykuł: \n {tekst}"""
data = \
{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": content}]
}
#need to change json to string so it prints out well
response = requests.post(url_test,headers=headers,json=data)

# in the response we look for first response and we take the content of the reply, so it looks readable!

#print(response.json()['choices'][0]['message']['content']) 
# this one should check for choices in content,
if response.status_code == 200:
    response_text = response.json()
    if 'choices' in response_text and len(response_text['choices'] > 0):


        #print(tekst)
        # i dont really want to use my tokens that often so its a testcase first too see if writing to html file works just fine
        example_text = response.json()['choices'][0]['message']['content']

        with open("artykul.html",'w') as plik:
            plik.write(example_text)
    else:
        print('there is no choices somehow')
else: print('something went wrong')