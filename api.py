import requests 
from pathlib import Path 
import csv
#create a function  
def api(): 
        #use the function and api given to find the conversion from USD to SGD 
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=XJ54Q43467ETNK7Y" 
        #use .get() to retrive data from server  
        response = requests.get(url)
        #use .json() to retrive data and store as JSON object 
        data = response.json() 
        #extract the keys of the dict to retrive the exchange rate 
        conversion = data["Realtime Currency Exchange Rate"] 
        #extract the data from the keys to retrive the exchange rate 
        exchangerate = conversion ["5. Exchange Rate"] 
        #print the summary report using f string to input the value  
        exchangerate= f"[REAL TIME CURRENCY EXCHANGE RATE] USD1 = SGD{exchangerate}" 
        print(exchangerate) 
        #create a cwd to check on my current location in the file system 
        cwd= Path.cwd()
        #create a new text file to input the summarized data from  
        summary = cwd/"summary_report.txt" 
        #create a new file with touch 
        summary.touch() 
        #use with text with write to write the data onto the summary page 
        with summary.open(mode="w", encoding="UTF-8",newline="")as file: 
                #create a writer object and named it as writer 
                writer=csv.writer(file) 
                #use writerow to print the answer 
                writer.writerow([exchangerate]) 
print(api()) 
