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

#create a cwd to check on my current location in the file system  

    cwd= Path.cwd() 
#create an empty list for netprofit and day 
    netprofit=[] 
    days=[] 
#create a file path to the profit and loss csv to extract data 
    profit_and_loss = cwd/"csv_reports"/"Profit_and_Loss.csv" 
#using with statement and reading mode to read the data from the csv  
    with profit_and_loss.open(mode="r",encoding="UTF-8",newline="") as file: 
#instantiate a reader object 
        reader = csv.reader(file) 
#next is used to skip the header 
        next(reader) 
#create a for loop to extract all the data into one list 
        for value in reader: 
#extract the value of net profit from the data 
            values = value[4] 
#create the value into a float to append the values 
            float1 = float(values) 
            netprofit.append(float1) 
#extract the days from the data 
            values1 = value[0] 
#create the days into a float to append the days 
            float2 = float(values1) 
            days.append(float2) 
#use the for loop to extract all the data that met the requirements  
    for value in netprofit: 
#if the netprofit of the prev day is more than current day , the program will run and print the following 
#it is the same throughout  
        if netprofit[0]>netprofit[1]: 
            diff = netprofit[0]-netprofit[1] 
#multiply the exchange rate with the difference of the value between 2 days to convert USD to SGD 
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
#use break to stop an iteration  
        break 
#create a new text file to input the summarized data  
    summary = cwd/"summary_report.txt" 
#create a new file with touch 
    summary.touch() 
#use with text with append to add on the data to the summary page  
    with summary.open(mode="a", encoding="UTF-8",newline="")as file: 
        writer=csv.writer(file) 
        writer.writerow([ans1]) 
        writer.writerow([ans4]) 
        writer.writerow([ans6]) 
        writer.writerow([ans8]) 
        writer.writerow([ans10]) 

print(profitloss()) 

 