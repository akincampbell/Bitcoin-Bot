import coinbase
#from coinbase.wallet.client import Client
#print("hello world")
#data = open('passphrase', r).read().splitlines()
#print("gb world")
#print(data)

coinbase_API_key = "9xF36UsqaybNxP2M"
coinbase_API_secret = "6NXAzklQF2BwrlQivB0t6alFOmBXuqfW"
client = Client(coinbase_API_key, coinbase_API_secret)
print(client.get_sell_price(currency_pair = 'BTC-USD'))

# accounts = client.get_accounts()
# assert isinstance(accounts.data, list)
# assert accounts[0] is accounts.data[0]
# assert len(accounts[::]) == len(accounts.data)