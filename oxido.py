import requests
import os 
url_test = "https://api.openai.com/v1/chat/completions"

key =  "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"
headers = \
{
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json"
}
data = \
{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "write something nice"}]
}
#need to change json to string so it prints out well
response = requests.post(url_test,headers=headers,json=data)

# in the response we look for first response and we take the content of the reply, so it looks readable!

print(response.json()['choices'][0]['message']['content']) 

# test