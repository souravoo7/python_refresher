"""
Created on Wed Jul 17 19:37:04 2024

@author: sourav

#Run the below command before saving scripts

import os

os.chdir("C:/Users/soura/Documents/GitHub/python_refresher/Work")

"""

import csv

data_loc = 'C:/Users/soura/Documents/GitHub/python_refresher/Work/Data/prices.csv' 
f = open(data_loc, 'r')
rows = csv.reader(f);

for row in rows:
    print(row)

f.close()

'''
A function to read prices into a dictionary
'''

def read_prices(data_loc):
    
    '''
    read the data into a dictionary   
    '''
    
    f = open(data_loc, 'r');
    rows = csv.reader(f);
    
    prices = {}; #define a blank dictionary
    for row_num, row in enumerate(rows, start=1):
        try:
            prices[row[0]] = float(row[1]);
        except IndexError:
            print('could not read', row_num);
    f.close()
    return prices

data_loc = 'C:/Users/soura/Documents/GitHub/python_refresher/Work/Data/prices.csv' 
prices = read_prices(data_loc);
print(prices);

#------------------------------------------------------------------------------

columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = dict(zip(columns, values))

#------------------------------------------------------------------------------

'''
calculate the cost of the portfolio with exception handling and reporting the error row number
'''

def portfolio_price(data_loc):
    f = open(data_loc, 'rt');
    
    #move the pointer to the next line
    #headers = next(f);

    cost = 0;
    num_shares =0;
    share_price = 0;
    
    for line_num, line in enumerate(f, start=1):
        try:
            row = line.split(',')
        except ValueError:
            print('cannot read line', line_num)
        try:
            num_shares = float(row[1])
            share_price = float(row[2])
            cost = cost + (num_shares*share_price)
        except ValueError:
            print('failed to read string into float @line', line_num)
    
    f.close()
    
    #print('cost of portfolio', cost)
    return cost;

#------------------------------------------------------------------------------
data_loc = 'C:/Users/soura/Documents/GitHub/python_refresher/Work/Data/missing.csv'

print('portfolio price', portfolio_price(data_loc));
'''-------------------------------------------------------------------------'''





















