from pathlib import Path
import csv
import requests
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=XJ54Q43467ETNK7Y"
response = requests.get(url)
data = response.json()
conversion = data["Realtime Currency Exchange Rate"]
#print(conversion)
conversion_list = []
for rate in conversion:
        exchangerate = conversion ["5. Exchange Rate"]
exchangerate=float(exchangerate)
#print(exchangerate)
cwd= Path.cwd()
days=[]
cash=[]
cash_on_hand = cwd/"csv_reports"/"Cash_on_Hand.csv"
cash_on_hand.touch()
with cash_on_hand.open(mode="r",encoding="UTF-8",newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for value in reader:
        values = value[0]
        float1 = float(values)
        days.append(float1)
        values1 = value[1]
        float2 = float(values1)
        cash.append(float2)
#print(cash)
#print(days)
if cash[0]>cash[1]:
    diff = cash[0]-cash[1]
    print (f"[CASH SURPLUS] DAY:{days[1]}, AMOUNT: SGD{exchangerate*diff}")
if cash[1]>cash[2]:
    diff1 = cash[1]-cash[2]
    print (f"[CASH SURPLUS] DAY:{days[2]}, AMOUNT: SGD{exchangerate*diff1}")
if cash[2]>cash[3]:
    diff2 = cash[2]-cash[3]
    print (f"[CASH SURPLUS] DAY:{days[3]}, AMOUNT: SGD{exchangerate*diff2}")
if cash[3]>cash[4]:
    diff3 = cash[3]-cash[4]
    print (f"[CASH SURPLUS] DAY:{days[4]}, AMOUNT: SGD{exchangerate*diff3}")
if cash[4]>cash[5]:
    diff4 = cash[4]-cash[5]
    print (f"[CASH SURPLUS] DAY:{days[5]}, AMOUNT: SGD{exchangerate*diff4}")
if cash[5]>cash[6]:
    diff5 = cash[5]-cash[6]
    print (f"[CASH SURPLUS] DAY:{days[6]}, AMOUNT: SGD{exchangerate*diff5}")
if cash[6]>cash[7]:
    diff6 = cash[6]-cash[7]
    print (f"[CASH SURPLUS] DAY:{days[7]}, AMOUNT: SGD{exchangerate*diff6}")
if cash[7]>cash[8]:
    diff7 = cash[7]-cash[8]
    print (f"[CASH SURPLUS] DAY:{days[8]}, AMOUNT: SGD{exchangerate*diff7}")
if cash[8]>cash[9]:
    diff8 = cash[8]-cash[9]
    print (f"[CASH SURPLUS] DAY:{days[9]}, AMOUNT: SGD{exchangerate*diff8}")
if cash[9]>cash[10]:
    diff9 = cash[9]-cash[10]
    print (f"[CASH SURPLUS] DAY:{days[10]}, AMOUNT: SGD{exchangerate*diff9}")

coh = cwd/"summary_report.txt"
coh.touch()
with coh.open(mode="w", encoding="UTF-8",newline="")as file:
        writer=csv.writer(file)
        writer.writerow([exchangerate])