import requests
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=XJ54Q43467ETNK7Y"
response = requests.get(url)
data = response.json()
conversion = data["Realtime Currency Exchange Rate"]
#print(conversion)
conversion_list = []
for rate in conversion:
        exchangerate = conversion ["5. Exchange Rate"]
print(exchangerate)
    
    

    