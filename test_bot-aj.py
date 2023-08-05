import coinbase
from coinbase.wallet.client import Client
from coinbase.wallet.client import OAuthClient


print("hello world")

# Client instatiation and Coinbase information
# To generate API key visit https://help.coinbase.com/en/exchange/managing-my-account/how-to-create-an-api-key
coinbase_API_key = '9xF36UsqaybNxP2M'
coinbase_API_secret = '6NXAzklQF2BwrlQivB0t6alFOmBXuqfW'
client = Client(coinbase_API_key, coinbase_API_secret)
# OAuth made user specific methods work
client = OAuthClient("28f70e7f2ea61ac9612c535eccd1a78277f02ac42e921729806e2e80bba63f40", "28f70e7f2ea61ac9612c535eccd1a78277f02ac42e921729806e2e80bba63f40") 
user = client.get_current_user()
# Get buy price
buy_price = client.get_buy_price(currency_pair = 'BTC-USD')
sell_price = client.get_sell_price(currency_pair = 'BTC-USD')
print(buy_price, sell_price)





#=====Random statements========#
# accounts = client.get_accounts()
# assert isinstance(accounts.data, list)
# assert accounts[0] is accounts.data[0]
# assert len(accounts[::]) == len(accounts.data)