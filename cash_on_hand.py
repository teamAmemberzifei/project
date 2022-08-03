from pathlib import Path
import csv
import requests

#create a function
def cash():

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

    #create a file path to the cash on hand csv to extract data
    cash_on_hand = cwd/"csv_reports"/"Cash_on_Hand.csv"

    #create an empty list for the days and cash
    days=[]
    cash=[]

    #using with statement and reading mode to read the data from the csv 
    with cash_on_hand.open(mode="r",encoding="UTF-8",newline="") as file:

        #instantiate a reader object
        reader = csv.reader(file)

        #next is used to skip the header
        next(reader)

        #create a for loop to extract all the data into one list
        for value in reader:

            #extract the days from the data
            values = value[0]

            #create the day into a float to append the days
            float1 = float(values)
            days.append(float1)

            #extract the value from the data
            values1 = value[1]

            #create the value into a float to append the values
            float2 = float(values1)
            cash.append(float2)
    
    #use the for loop to extract all the data that met the if condition 
    for value in cash:

        #if the cash on hand of the prev day is more than current day , the program will run and print the following
        #it is the same throughout 
        if cash[0]>cash[1]:
            diff = cash[0]-cash[1]

            #multiply the exchange rate with the difference of the value between 2 days to convert USD to SGD
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

        #use break to stop an iteration 
        break
    
    #create a new text file to input the summarized data  
    summary = cwd/"summary_report.txt"

    #create a new file with touch
    summary.touch()

    #use with text with append to add on the data to the summary page
    with summary.open(mode="a", encoding="UTF-8",newline="")as file:

        #create a writer object and named it as writer
        writer=csv.writer(file)

        #use writerow to print the answer
        writer.writerow([ans1])
        writer.writerow([ans5])
        writer.writerow([ans9])
        writer.writerow([ans10])
print(cash())
