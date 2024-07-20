# -*- coding: utf-8 -*-

"""
Created on Wed Jul 17 19:37:04 2024

@author: sourav

#Run the below command before saving scripts

import os

os.chdir("C:/Users/soura/Documents/GitHub/python_refresher/Work")

"""


#reading files

data_loc = 'C:/Users/soura/Documents/GitHub/python_refresher/Work/Data/portfolio.csv' 

with open(data_loc, 'rt') as f:
    data =f.read()

print(data)



#reading files line by line

with open(data_loc, 'rt') as f:
    for line in f:
        print(line, end = '')

#get the headers
f = open(data_loc, 'rt');
headers = next(f);

headers
f.close()
'''-------------------------------------------------------------------------'''

#calculate the cost of the portfolio
f = open(data_loc, 'rt');
headers = next(f);#move the pointer to the next line

cost = 0;
num_shares =0;
share_price = 0;

for line in f:
    row = line.split(',')
    num_shares = float(row[1])
    share_price = float(row[2])
    cost = cost + (num_shares*share_price)

f.close()

print('cost of portfolio', cost)

'''-------------------------------------------------------------------------'''

data_loc = 'C:/Users/soura/Documents/GitHub/python_refresher/Work/Data/portfolio.csv.gz'
    
import gzip

with gzip.open(data_loc, 'rt') as f:
    for line in f:
        print(line, end = '')

'''
Custom functions in python
'''

def sumcount(n):
    '''
    Returns the sum of the first n integers
    '''
    total = 0;
    for i in range(1,n+1):
        total = total + i;
    
    return total;


n =10;
print('sum of', n, 'integers', sumcount(n))

'''-------------------------------------------------------------------------'''

#calculate the cost of the portfolio

def portfolio_price(data_loc):
    f = open(data_loc, 'rt');
    headers = next(f);#move the pointer to the next line

    cost = 0;
    num_shares =0;
    share_price = 0;
    
    for line in f:
        row = line.split(',')
        num_shares = float(row[1])
        share_price = float(row[2])
        cost = cost + (num_shares*share_price)
    
    f.close()
    
    #print('cost of portfolio', cost)
    return cost;


data_loc = 'C:/Users/soura/Documents/GitHub/python_refresher/Work/Data/portfolio.csv'

print(portfolio_price(data_loc));
'''-------------------------------------------------------------------------'''


#calculate the cost of the portfolio with exception handling

def portfolio_price(data_loc):
    f = open(data_loc, 'rt');
    
    #move the pointer to the next line
    #headers = next(f);

    cost = 0;
    num_shares =0;
    share_price = 0;
    
    for line in f:
        try:
            row = line.split(',')
        except ValueError:
            print('cannot read line')
        try:
            num_shares = float(row[1])
            share_price = float(row[2])
            cost = cost + (num_shares*share_price)
        except ValueError:
            print('failed to read string into float')
    
    f.close()
    
    #print('cost of portfolio', cost)
    return cost;

#------------------------------------------------------------------------------
data_loc = 'C:/Users/soura/Documents/GitHub/python_refresher/Work/Data/missing.csv'

print(portfolio_price(data_loc));
'''-------------------------------------------------------------------------'''




















