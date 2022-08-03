from pathlib import Path
import csv
def overheads():
        cwd= Path.cwd()
        overheads = cwd/"csv_reports"/"Overheads.csv"

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
        empty_list = []
        empty_list1 = []

        with overheads.open(mode="r",encoding="UTF-8", newline="") as file:
                reader = csv.reader(file)
                next(reader)
                for value in reader:
                        values = value[1]
                        floaty = float(values)
                        empty_list.append(floaty)
                        category = value[0]
                        empty_list1.append(category)
                        empty_list.sort()
        overhead_value = f"[HIGHEST OVERHEADS] {empty_list1[0]}: SGD{exchangerate*empty_list[10]}"
        print(overhead_value)
        summary = cwd/"summary_report.txt"
        summary.touch()
        with summary.open(mode="w", encoding="UTF-8",newline="")as file:
                writer=csv.writer(file)
                writer.writerow([overhead_value])
print(overheads())                
