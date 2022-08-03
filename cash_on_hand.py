from pathlib import Path
import csv
import requests
def cash():
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=XJ54Q43467ETNK7Y"
    response = requests.get(url)
    data = response.json()
    conversion = data["Realtime Currency Exchange Rate"]
    #print(conversion)
    for rate in conversion:
        exchangerate = conversion ["5. Exchange Rate"]
    exchangerate=float(exchangerate)
    #print(exchangerate)
    cwd= Path.cwd()
    cash_on_hand = cwd/"csv_reports"/"Cash_on_Hand.csv"
    days=[]
    cash=[]
    cash_on_hand = cwd/"csv_reports"/"Cash_on_Hand.csv"
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
    for value in cash:
        if cash[0]>cash[1]:
            diff = cash[0]-cash[1]
            ans1 = f"[CASH SURPLUS] DAY:{days[1]}, AMOUNT: SGD{exchangerate*diff}"
            print(ans1)
        if cash[1]>cash[2]:
            diff1 = cash[1]-cash[2]
            ans2 = f"[CASH SURPLUS] DAY:{days[2]}, AMOUNT: SGD{exchangerate*diff1}"
            print(ans2)
        if cash[2]>cash[3]:
            diff2 = cash[2]-cash[3]
            ans3 = f"[CASH SURPLUS] DAY:{days[3]}, AMOUNT: SGD{exchangerate*diff2}"
