from pathlib import Path
import requests
import csv

#create a function
def profitloss():

    #use the function and api given to find the conversion from USD to SGD
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=XJ54Q43467ETNK7Y"

    #use .get() to retrive data from server 
    response = requests.get(url)

    #use .json() to retrive data and store as JSON object
    data = response.json()

    #extract the keys of the dict to retrive the exchange rate
    conversion = data["Realtime Currency Exchange Rate"]
    #print(conversion)

    #extract the data from the keys to retrive the exchange rate 
    exchangerate = conversion ["5. Exchange Rate"]

    #exchange rate have to be a float in order to multipy 
    exchangerate=float(exchangerate)
    #print(exchangerate)

    
    cwd= Path.cwd()
    netprofit=[]
    days=[]
    profit_and_loss = cwd/"csv_reports"/"Profit_and_Loss.csv"
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
    for value in netprofit:
        if netprofit[0]>netprofit[1]:
            diff = netprofit[0]-netprofit[1]
            ans1 = f"[NET PROFIT SURPLUS] DAY:{days[1]}, AMOUNT: SGD{exchangerate*diff}"
            print(ans1)
        if netprofit[1]>netprofit[2]:
            diff1= netprofit[1]-netprofit[2]
            ans2 = f"[NET PROFIT SURPLUS] DAY:{days[2]}, AMOUNT: SGD{exchangerate*diff1}"
            print(ans2)
        if netprofit[2]>netprofit[3]:
            diff2 = netprofit[2]-netprofit[3]
            ans3 = f"[NET PROFIT SURPLUS] DAY:{days[3]}, AMOUNT: SGD{exchangerate*diff2}"
            print(ans3)
        if netprofit[3]>netprofit[4]:
            diff3 = netprofit[3]-netprofit[4]
            ans4 = f"[NET PROFIT SURPLUS] DAY:{days[4]}, AMOUNT: SGD{exchangerate*diff3}"
            print(ans4)
        if netprofit[4]>netprofit[5]:
            diff4 = netprofit[4]-netprofit[5]
            ans5 = f"[NET PROFIT SURPLUS] DAY:{days[5]}, AMOUNT: SGD{exchangerate*diff4}"
            print(ans5)
        if netprofit[5]>netprofit[6]:
            diff5 = netprofit[5]-netprofit[6]
            ans6 = f"[NET PROFIT SURPLUS] DAY:{days[6]}, AMOUNT: SGD{exchangerate*diff5}"
            print(ans6)
        if netprofit[6]>netprofit[7]:
            diff6 = netprofit[6]-netprofit[7]
            ans7 = f"[NET PROFIT SURPLUS] DAY:{days[7]}, AMOUNT: SGD{exchangerate*diff6}"
            print(ans7)
        if netprofit[7]>netprofit[8]:
            diff7 = netprofit[7]-netprofit[8]
            ans8 = f"[NET PROFIT SURPLUS] DAY:{days[8]}, AMOUNT: SGD{exchangerate*diff7}"
            print(ans8)
        if netprofit[8]>netprofit[9]:
            diff8 = netprofit[8]-netprofit[9]
            ans9 = f"[NET PROFIT SURPLUS] DAY:{days[9]}, AMOUNT: SGD{exchangerate*diff8}"
            print(ans9)
        if netprofit[9]>netprofit[10]:
            diff9 = netprofit[9]-netprofit[10]
            ans10 = f"[NET PROFIT SURPLUS] DAY:{days[10]}, AMOUNT: SGD{exchangerate*diff9}"
            print(ans10)
        break
    coh = cwd/"summary_report.txt"
    coh.touch()
    with coh.open(mode="w", encoding="UTF-8",newline="")as file:
        writer=csv.writer(file)
        writer.writerow([ans1])
print(profitloss())
