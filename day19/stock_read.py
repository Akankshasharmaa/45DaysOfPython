import csv


sum_price = 0
count = 0
with open('my_stocks.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    sortedlist = sorted(reader, key=lambda row:(row['column_2']))
    print(sortedlist)

    for row in reader:
        sum_price += float(row['price'])
        count += 1
    
    mean = sum_price / count
    print(mean)


   