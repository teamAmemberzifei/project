import requests 
from pathlib import Path 
import csv 
def api(): 
        url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=XJ54Q43467ETNK7Y" 
        response = requests.get(url) 
        data = response.json() 
        conversion = data["Realtime Currency Exchange Rate"] 
        conversion_list = [] 
        for rate in conversion: 
                exchangerate = conversion ["5. Exchange Rate"] 
                exchangerate= f"[REAL TIME CURRENCY EXCHANGE RATE] USD1 = SGD{exchangerate}" 
                print(exchangerate) 
                cwd= Path.cwd() 
                summary = cwd/"summary_report.txt" 
                summary.touch() 
                with summary.open(mode="w", encoding="UTF-8",newline="")as file: 
                        writer=csv.writer(file) 
                        writer.writerow([exchangerate]) 
print(api()) 
