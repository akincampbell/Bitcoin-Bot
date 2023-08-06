import coinbase
from coinbase.wallet.client import Client
from coinbase.wallet.client import OAuthClient


print("hello")

# Client instatiation and Coinbase information
# To generate API key visit https://help.coinbase.com/en/exchange/managing-my-account/how-to-create-an-api-key
coinbase_API_key = '9xF36UsqaybNxP2M'
coinbase_API_secret = '6NXAzklQF2BwrlQivB0t6alFOmBXuqfW'
client = Client(coinbase_API_key, coinbase_API_secret)
# OAuth made user specific methods work
client = OAuthClient("08e141e2ab09c8ddaa7275db0f126e0875c1bc4a5fa0784f53a69378cf0cebff", "08e141e2ab09c8ddaa7275db0f126e0875c1bc4a5fa0784f53a69378cf0cebff") 
user = client.get_current_user()
print(user["name"])
# Get buy and sell price
buy_price = client.get_buy_price(currency_pair = 'BTC-USD')
sell_price = client.get_sell_price(currency_pair = 'BTC-USD')
# Get accounts for each wallet and print them out
total = 0
message = [ ]
accounts = client.get_accounts()
for wallet in accounts.data:
    message.append( str(wallet['name']) + ' ' +   str(wallet['native_balance']) )
    value = str( wallet['native_balance']).replace('USD','')
    total += float(value)
message.append( 'Total Balance: ' + 'USD ' + str(total) )
print ('\n'.join( message ))







#=====Random statements========#
# accounts = client.get_accounts()
# assert isinstance(accounts.data, list)
# assert accounts[0] is accounts.data[0]
# assert len(accounts[::]) == len(accounts.data)