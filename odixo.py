import requests

url_test = "https://api.openai.com/v1/chat/completions"
API_key = "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"

headers = \
{
    "Authorization": f"Bearer {API_key}",
    "Content-Type": "application/json"
}
data = \
{
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "write something nice"}]
}
#need to change json to string so it prints out well
response = requests.post(url_test,headers=headers,json=data)

print(response.json())

#test