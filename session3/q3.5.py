# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 01:16:32 2026

@author: ZST25-3
"""

product=input('enter product name:')
price=float(input('enter price :'))
discountcode=input('enter discount:')
if discountcode=='z14':
    print('final price:',price*0.8)
    
--------------
    
product=input('enter product name:')
price=float(input('enter price :'))
discountcode=input('enter discount:')
if discountcode=='z14':
    print('final price:',price*0.8)
else:
    print('the code is incorrect')     
---------------  

product=input('enter product name:')
price=float(input('enter price :'))
discountcode=input('enter discount:')
if discountcode=='z14':
    print('final price:',price*0.8)
else:
   discountcode=input('tryagain:')
if discountcode=='z14':
     print('price*0.8')
else:
    print('you are blocked')     
     