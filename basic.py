#Q1. Distance Traveled

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:37:42 2017

"""

car_spd=60
print('The distance the car will travel in 5 hours is:',5*car_spd,'miles')
print('The distance the car will travel in 8 hours is:',8*car_spd,'miles')
print('The distance the car will travel in 12 hours is:',12*car_spd,'miles')

##################################################################################

#Q2. Land Calculation
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 18:47:19 2017

T_square=int(input('Enter the total square feet in a tract of land:'))
print('This land is',T_square/43560,'acre（s）')

##################################################################################

#Q3. Property Tax
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 16:43:24 2017

Actual_v=int(input("Enter the property's actual value:$" ))
Assessment_v=Actual_v*0.6
Tax=Assessment_v/100*0.64
print("The property's assessment value is:$",Assessment_v)
print("The property tax is:$",format(Tax,'.2f'))

##################################################################################

Q4. Total Purchase
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 19:02:37 2017


price_1=int(input('Enter the price of 1st item:'))
price_2=int(input('Enter the price of 2nd item:'))
price_3=int(input('Enter the price of 3rd item:'))
price_4=int(input('Enter the price of 4th item:'))
price_5=int(input('Enter the price of 5th item:'))
tax_rate=0.06
sub_sale=price_1+price_2+price_3+price_4+price_5
tax_sale=tax_rate*sub_sale
print('The subtotal sale is',sub_sale)
print( 'The sales tax is',tax_sale)
print('The total is',sub_sale+tax_sale)

