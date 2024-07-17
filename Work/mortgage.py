# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 19:37:04 2024

@author: sourav

#Run the below command before saving scripts

import os

os.chdir("C:/Users/soura/Documents/Python Scripts/python_referesher")

"""
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)
