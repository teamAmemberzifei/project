from pathlib import Path
import csv
import requests
def cash():
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=XJ54Q43467ETNK7Y"
    response = requests.get(url)
    data = response.json()
    conversion = data["Realtime Currency Exchange Rate"]
    #print(conversion)
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
            print(ans3)
        if cash[3]>cash[4]:
            diff3 = cash[3]-cash[4]
            ans4 = f"[CASH SURPLUS] DAY:{days[4]}, AMOUNT: SGD{exchangerate*diff3}"
            print(ans4)
        if cash[4]>cash[5]:
            diff4 = cash[4]-cash[5]
            ans5 = f"[CASH SURPLUS] DAY:{days[5]}, AMOUNT: SGD{exchangerate*diff4}"
            print(ans5)
        if cash[5]>cash[6]:
            diff5 = cash[5]-cash[6]
            ans6 = f"[CASH SURPLUS] DAY:{days[6]}, AMOUNT: SGD{exchangerate*diff5}"
            print(ans6)
        if cash[6]>cash[7]:
            diff6 = cash[6]-cash[7]
            ans7 = f"[CASH SURPLUS] DAY:{days[7]}, AMOUNT: SGD{exchangerate*diff6}"
            print(ans7)
        if cash[7]>cash[8]:
            diff7 = cash[7]-cash[8]
            ans8 = f"[CASH SURPLUS] DAY:{days[8]}, AMOUNT: SGD{exchangerate*diff7}"
            print(ans8)
        if cash[8]>cash[9]:
           diff8 = cash[8]-cash[9]
           ans9 = f"[CASH SURPLUS] DAY:{days[9]}, AMOUNT: SGD{exchangerate*diff8}"
           print(ans9)
        if cash[9]>cash[10]:
           diff9 = cash[9]-cash[10]
           ans10 = f"[CASH SURPLUS] DAY:{days[10]}, AMOUNT: SGD{exchangerate*diff9}"
           print(ans10)
        break

    coh = cwd/"summary_report.txt"
    coh.touch()
    with coh.open(mode="w", encoding="UTF-8",newline="")as file:
        writer=csv.DictWriter(file, fieldnames=[ans1,ans5,ans9,ans10])
        writer.writeheader()
    file.close()
print(cash())