import requests
import matplotlib.pyplot as plt

x = requests.get("https://www.google.com/")

print(dict(x.headers)['Date']) if x.status_code == 200 else print("Sem acesso")

y = requests.get("https://www.sapo.pt")

z = requests.get("https://data.binance.com/api/v3/ticker/24hr")

a = z.json()

low_price = []

for i in a:
    low_price.append(i['lowPrice'])

plt.figure()
plt.scatter()
plt.show()

