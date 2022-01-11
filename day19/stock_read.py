import csv


sum_price = 0
count = 0
price_list = []
with open('my_stocks.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        sum_price += float(row['price'])
        price_list.append(float(row['price']))
        count += 1
    
    mean = sum_price / count
    
    sorted_list = sorted(price_list)
    median = round(sorted_list[4]+sorted_list[5] / 2, 2)
    
    high = max(price_list)
    low = min(price_list)

with open('my_stock_statistics.csv', 'w', newline='') as stat_csvfile:
    fieldnames = ['mean','median','high','low']
    writer = csv.DictWriter(stat_csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'mean':mean, 'median':median, 'high':high, 'low':low})
    
   