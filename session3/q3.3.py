# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 15:55:14 2026

@author: ZST25-3
"""

number1=int(input('write number1:'))
number2=int(input('write number 2:'))
operation=input('wite operation(jam,tafrigh,zarb,taghsim):')
if operation == 'jam':
    print(number1+number2)
elif operation == 'tafrigh':
    print(number1-number2)
elif operation == 'zarb':
    print(number1*number2)
elif operation == 'taghsim':
    print(number1/number2)    
else:
    print('meghdare vared shode sahih nemibashad')    
    