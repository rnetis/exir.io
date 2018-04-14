import requests

r = requests.get("https://api.exir.tech/v0/trades?symbol=btc").json()
print("size\tprice\t\tside")

for x in range(0, 40):
  print(str(r['btc'][x]['size']) + '\t' + str(r['btc'][x]['price']) + '\t' + str(r['btc'][x]['side']))