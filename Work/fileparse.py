# -*- coding: utf-8 -*-

"""
Created on Wed Jul 17 19:37:04 2024

@author: sourav

#Run the below command before saving scripts

import os

os.chdir("C:/Users/soura/Documents/GitHub/python_refresher/Work")

"""

with open('Data/portfolio.csv', 'rt') as f:
        for line in f:
            print(line, end='')
