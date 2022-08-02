from pathlib import Path
import requests
import csv
import re 
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=XJ54Q43467ETNK7Y"
response = requests.get(url)
data = response.json()
conversion = data["Realtime Currency Exchange Rate"]
#print(conversion)
conversion_list = []
for rate in conversion:
        exchangerate = conversion ["5. Exchange Rate"]
exchangerate=float(exchangerate)
cwd= Path.cwd()
netprofit=[]
days=[]
profit_and_loss = cwd/"csv_reports"/"Profit_and_Loss.csv"
profit_and_loss.touch()
with profit_and_loss.open(mode="r",encoding="UTF-8",newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for value in reader:
        values = value[4]
        float1 = float(values)
        netprofit.append(float1)
        values1 = value[0]
        float2 = float(values1)
        days.append(float2)

if netprofit[0]>netprofit[1]:
    diff = netprofit[0]-netprofit[1]
    print (f"[PROFIT SURPLUS] DAY:{days[1]}, AMOUNT: SGD{exchangerate*diff}")
if netprofit[1]>netprofit[2]:
    diff1= netprofit[1]-netprofit[2]
    print (f"[PROFIT SURPLUS] DAY:{days[2]}, AMOUNT: SGD{exchangerate*diff1}")
if netprofit[2]>netprofit[3]:
    diff2 = netprofit[2]-netprofit[3]
    print (f"[PROFIT SURPLUS] DAY:{days[3]}, AMOUNT: SGD{exchangerate*diff2}")
if netprofit[3]>netprofit[4]:
    diff3 = netprofit[3]-netprofit[4]
    print (f"[PROFIT SURPLUS] DAY:{days[4]}, AMOUNT: SGD{exchangerate*diff3}")
if netprofit[4]>netprofit[5]:
    diff4 = netprofit[4]-netprofit[5]
    print (f"[PROFIT SURPLUS] DAY:{days[5]}, AMOUNT: SGD{exchangerate*diff4}")
if netprofit[5]>netprofit[6]:
    diff5 = netprofit[5]-netprofit[6]
    print (f"[PROFIT SURPLUS] DAY:{days[6]}, AMOUNT: SGD{exchangerate*diff5}")
if netprofit[6]>netprofit[7]:
    diff6 = netprofit[6]-netprofit[7]
    print (f"[PROFIT SURPLUS] DAY:{days[7]}, AMOUNT: SGD{exchangerate*diff6}")
if netprofit[7]>netprofit[8]:
    diff7 = netprofit[7]-netprofit[8]
    print (f"[PROFIT SURPLUS] DAY:{days[8]}, AMOUNT: SGD{exchangerate*diff7}")
if netprofit[8]>netprofit[9]:
    diff8 = netprofit[8]-netprofit[9]
    print (f"[PROFIT SURPLUS] DAY:{days[9]}, AMOUNT: SGD{exchangerate*diff8}")
if netprofit[9]>netprofit[10]:
    diff9 = netprofit[9]-netprofit[10]
    print (f"[PROFIT SURPLUS] DAY:{days[10]}, AMOUNT: SGD{exchangerate*diff9}")

