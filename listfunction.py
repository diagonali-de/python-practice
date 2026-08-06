# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:33:47 2026

@author: ZST25-3
"""

teams=['barcelona','arsenal','juventus']
teams.append('chelsea')
print(teams)
#put element at the end of the variables

teams.insert(0,'argentina')
#in selected index put an element

newteams=['perspolis','teractor','sepahan']
teams.extend(newteams)
#add another lists elements to old list
teams.remove('juventus')
#remove selected value
teams.pop(4)
#remove element in selected index
print(teams.count('arsenal'))
#count the elements in list
print(teams.index('perspolis'))
#write the index of first element
teams.sort()
#sort the list
teams.reverse()
#reverse the list sort
teams.copy()
#make a copy of list
teams.clear()
#remove all elements