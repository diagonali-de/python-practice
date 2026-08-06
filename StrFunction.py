# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 12:02:26 2026

@author: ZST25-3
"""
name='  christopher  '
print(name.upper())
#capitalize all words
print(name.lower())
#make all words lower
print(name.capitalize())
#make the first letter capitalized
print(name.title())
#make every first letter of words capitalized
print(name.replace('chris','merris'))
#change two str with new word or sentence
print(name.find('ch'))
#find the first index of str
print(name.count('c'))
#count the numbers of one word or words in str
print(len(name))
#the lenght of str(count the letters)
print(name.swapcase())
#make upper words to lower and also reverse of it
print(name.rfind('s'))
#find the last inde
print(name.startswith('  '))
#true or false if started with this word or space or letter
print(name.endswith(' '))
#true or false if ended with this word or space or letter
print(name.strip())
#remove the first and last spaces
print(name.rstrip(),name.lstrip())
#remove left and right spaces
print(name.split())
#change a string to a list
name1=['a','b','c']
print('_'.join(name1))
print('$'.join(name1))
#change a list with('-',@,...) to string
name2=('a')
print(name2.isalpha())
#check if all are letters
name3=('klhjkjj214')
print(name3.isalnum())
#check if all are only letters or numbers
name4=('Ahmad')
print(name4.islower())
#check if all are lower
print(name4.isupper())
#check if all are upper
print(type(name2))
#check the type of the value
print(name2.center(4))
#put the str to the center of which place u want(0,1,2...)
print(name.ljust(0))
name5='david,ahmadi     '
print(name5.ljust(5))
#write the str from left
name6='935'
print(name6.zfill(4))
#put 0 to the firstr of str#**the numbers in () must be atleast one more than
 #the numbers to put 0
name7='AHmaD-reza-al'
print(name7.casefold())
#make all letters lower
print(name7.partition('-'))
#split the str from first '-' to three section
print(name7.rpartition('-'))
#split the str from last '-' to three section
text='david\nmath'
print(text.splitlines())
#change str to list from new line
print(name.encode())
#turn str to bytes
job='programmer'
weight=80
print('my job is {} and i am {} kg'.format(job,weight))
#put values in {}