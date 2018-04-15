import requests
import exir

try:
	fi = open("token", "r")
	token = fi.read()
	fi.close()
except IOError:
	token = raw_input("Enter your token access> ")
	fi = open("token", "w")
	fi.write(token)
	fi.close()
re = requests.get("https://api.exir.tech/v0/user", headers = {"Authorization": "Bearer " +  token}).json()
print("Hello" + re["full_name"].encode("utf-8"))

print("Email: " + re["email"])
print("1 - Get balance")
print("2 - Get price")
print("3 - place order")
print("4 - Cancel order")
print("5 - Trade book")
x = raw_input("Enter would do you want> ")

price = requests.get("https://api.exir.tech/v0/ticker?symbol=btc").json()["ticker"]
if x == "1":
	z = requests.get("https://api.exir.tech/v0/user/balance", headers = {"Authorization": "Bearer " +  token}).json()
	print("Bitcoin Balance : " + str(z["btc_balance"]))
	print("Bitcoin avaliable : " + str(z["btc_available"]))
	print("Bitcoin pending : " + str(z["btc_pending"]))
	print("Money Balance : " + str(z["fiat_balance"]))
	print("Money avaliable : " + str(z["fiat_available"]))
	print("Your bitcoin in toman : " + str(z["btc_balance"] * price))
elif x == "2":
	price = requests.get("https://api.exir.tech/v0/ticker?symbol=btc").json()["ticker"]
	print(price)
elif x == "3":
	while "true":
		side = raw_input("Buy or Sell > ")
		side = side.lower()
		if side == "buy" or side == "sell":
			break
	size = raw_input("Amount of the order > ")
	pri = raw_input("Enter your price(" + price + ") > ")
	y = requests.post("https://api.exir.tech/v0/order", headers = {"Authorization": "Bearer " +  token}, data = {"symbol":"btc","side":side,"size":size,"type":"limit","price":pri}).json()
	print("Your order status : " + y["status"])
	print("Your order id : " + y["id"])
elif x == "4":
	sexy = raw_input("All or one >")
	sexy = sexy.lower()
	while "true":
		if sexy == "all":
			print("This object not complated!")
		elif sexy == "one":
			print("This object not complated!")
		else:
			print("This object not complated!")
elif x == "5":
	exir.tradebook()
else:
	print("Wrong number!")
