import requests

r = requests.get('https://192.168.253.40:7710', verify=False)
print(r.text)