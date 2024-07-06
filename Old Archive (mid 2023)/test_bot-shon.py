import coinbase
from coinbase.wallet.client import Client
#print("hello world")
#data = open('passphrase', r).read().splitlines()
#print("gb world")
#print(data)

# Add api key and api secret environment variables
coinbase_API_key = Environment_Variable
coinbase_API_secret = Environment_Variable
client = Client(coinbase_API_key, coinbase_API_secret)
print(client.get_current_user())

# accounts = client.get_accounts()
# assert isinstance(accounts.data, list)
# assert accounts[0] is accounts.data[0]
# assert len(accounts[::]) == len(accounts.data)