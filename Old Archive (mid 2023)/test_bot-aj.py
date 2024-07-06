import coinbase
import requests
from coinbase.wallet.client import Client
from coinbase.wallet.client import OAuthClient

#===== A BITCOIN BOT ======#
#==========================#
print("BITCOIN BOT says 'Hello!' ")

# Client instatiation [one implementation] and Coinbase information
# To generate API key visit https://help.coinbase.com/en/exchange/managing-my-account/how-to-create-an-api-key
# Add api key and api secret environment variables
coinbase_API_key = '9xF36UsqaybNxP2M'
coinbase_API_secret = '6NXAzklQF2BwrlQivB0t6alFOmBXuqfW'
client = Client(coinbase_API_key, coinbase_API_secret)

# Get access and refresh tokens (for OAuth): https://docs.cloud.coinbase.com/sign-in-with-coinbase/docs/sign-in-with-coinbase-integration
# NEEDS-WORK
response_one =  requests.get('https://www.coinbase.com/oauth/authorize?response_type=code&client_id=b6fe079a71ac5f28ce21fa80b599dfa150989eeb0b8b36571baa635a2ebd7e36&scope=wallet:accounts:write')
print('Response One:', response_one)
# response_one_json_data = response_one.json()
# print(response_one_json_data)
request_one = requests.post('https://api.coinbase.com/oauth/token', 'grant_type=authorization_code&code=4c666b5c0c0d9d3140f2e0776cbe245f3143011d82b7a2c2a590cc7e20b79ae8&client_id=b6fe079a71ac5f28ce21fa80b599dfa150989eeb0b8b36571baa635a2ebd7e36&client_secret=ff71e2b8b9db724d57bd36b788e6bbcf1b22919d51d565aad2b45432ac1b170f')
print('Request One:',request_one.json())

# OAuth, Client instantiation [another client implementation]| made user specific methods work
client = OAuthClient("43f0449984c23099984925914e46ed8a3c594857fdca8dd186ce516a0f5a01ad", "43f0449984c23099984925914e46ed8a3c594857fdca8dd186ce516a0f5a01ad")

 
user = client.get_current_user()
print(user["name"])
# Get buy and sell price
buy_price = client.get_buy_price(currency_pair = 'BTC-USD')
sell_price = client.get_sell_price(currency_pair = 'BTC-USD')
# Get accounts for each wallet and print them out
# total = 0
# message = [ ]
# accounts = client.get_accounts()
# for wallet in accounts.data:
#     message.append( str(wallet['name']) + ' ' +   str(wallet['native_balance']) )
#     value = str( wallet['native_balance']).replace('USD','')
#     total += float(value)
# message.append( 'Total Balance: ' + 'USD ' + str(total) )
# print ('\n'.join( message ))







#=====Random statements========#
# accounts = client.get_accounts()
# assert isinstance(accounts.data, list)
# assert accounts[0] is accounts.data[0]
# assert len(accounts[::]) == len(accounts.data)