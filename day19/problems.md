# Day 19

## Problem 1

Given a number x, write a function that will return True if x is a Prime number and False otherwise.

## Problem 2

You are working as a finance accountant and you would like to produce a report containing data of some companies. Your task is as follows:

- Find at least 10 companies you are interested in from the Internet
- Collect their Stock Price, Stock Symbol, Company name
- (You can do the above 2 steps from your web browser)
- Now you need to write a Python program that will produce a CSV report. A CSV is a Comma-Separated Values file (and can be read from MS Excel as well!)

Your python program should:
  - Store the above data in a dictionary
  - Generate a `my_stocks.csv` file which has a header followed by 1 row per stock.

Example output: 1 heading and 1 row.
```
stock_name,stock_ticker,stock_price
Apple,AAPL,100.0
```


## Problem 3

Now that you have created a CSV report as part of problem 2, your next task is to compute some statistics using this report.

Write a python program that does the following:
  - Reads the `my_stocks.csv` file
  - Calculates the mean stock price, the median stock price as well as the highest and lowest stock price.
  - Write a new CSV file: `my_stock_statistics.csv` which will have 1 header and 1 row:

Example output: 1 heading and 1 row expected.

```
mean,median,high,low
15.0,10.0,2.0,20.0
```
