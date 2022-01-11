import csv

mydata = [('Apple','AAPL','172.19'),
('Microsoft','MSFT','314.27'),
('Tesla','TSLA','1058.12'),
('TomTom','TOM','8.97'),
('Google','GOOG','2771.48'),
('Samsung','SSUN','1334.00'),
('Cloud flare','NET','110.75'),
('Snow flakes','SNOW','302.73'),
('Delivery hero','DHER.DE','85.16'),
('Mc Donalds','MCD','264.41')
]

with open('my_stocks.csv', 'w', newline='') as csvfile:
    fieldnames = ['company_name', 'symbol','price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for item in mydata:
        d = {'company_name':item[0], 'symbol':item[1],'price':item[2]}
        writer.writerow(d)

