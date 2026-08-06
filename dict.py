# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 00:00:26 2026

@author: ZST25-3
"""

character={'name':'Tom','age':30,'job':'teacher','city':'Texas'}
print(character)
#show the values
character['age']=40
#change the keys value
character['gender']='male'
#make a new key and value
print(character.keys())
print(character.keys(),character.values())
#show values and keys
print(character.get('gender'))
#get and show the keys value
fakecharacter=character.copy()
print(fakecharacter)
#make copy of dict
character.pop('gender')
#remove the key
character.clear()
#remove all keys