#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:50:10 2020

@author: rthomas

name = 'Randall Thomas'
number = 12
"""
# Using local number assignment and the format function 
print('Hello, my name is {x} and my age is {y}'.format(x=name,y=number))

# Lists
my_list = ['a','b','c','d']

# In slicing of lists, the right variable is < the index count not including
print(my_list[0:3])
# therefore this will print up to 'd' but not include it

# beginnings and ends can be denoted by null entries
# this is the same as above
print(my_list[:3])

# this will print to the end
print(my_list[2:])

# Nested Lists
nested_list = [0,1,2,['a','b','c']]

# to access 'b' via the following
print(nested_list[3][1])

# dictionaries are sets where the first "key" part is the unique part
d = {'key0':'any value', 'key1':'any value', 'key2':10}

print(d['key2'])

# to just print the keys in the dict
print(d.keys())

# to print the items in the dict to print tuples key:value pairs
print(d.items())

# to print the dictionary values
print(d.values())

# Booleans
print(1<2)

# for loops
seq = [1,2,3,4,5]

# for loop to print square of items in list
for item in seq:
    print(item ** 2)
# 'item' could be any word, 'num' or 'jelly'
    
# while loop
i = 1
while i < 5:
    print('Currently i is {}'.format(i))
    i = i + 1  # <== important step to avoid infinite while loop

# range function actually a sequence of numbers
print(list(range(5)))

for i in range(5):
    print(i)
    
# can also do steps in range and not starting with zero
for i in range(4,20,2):
    print(i)
# jupyter works correctly by not printing 0-4 unlike here


# List comprehension
# MEANS OF CONCISE CODE TO GET USED TO
x = [1,2,3,4]
out = []
for num in x:
    out.append(num**2)
    
# prints the assembled list called "out"
print(out)

# here is a shorthand way to do this
x = [1,2,3,4]
out = [num**2 for num in x]
print(out)

# creating a function that can be reused with a parameter
def my_func(param='default'):
    print(param)

# with a parameter    
my_func('Randall')

# without a parameter won't thow an error due to default value assigned
my_func()
# jupyter with <Ctrl><Tab> will pull not only the parameter but also 
# the documentation string

# Usually a function will have a return statement instead of a print
def my_func2(argument):
    return argument * 5

x = my_func2(5)
print(x)

# Lambda expressions are anonymous, one-time functions
# MEANS OF CONCISE CODE TO GET USED TO
def times_two(var):
    return var*2

result = times_two(4)
# print(result)

# above function converted to lambda function
seq = [1,2,3,4,5]
# y = list(map(lambda var: var*2, seq))
# print(y)

# standard function
def is_even(num):
    return num%2 == 0

r = list(filter(is_even,seq))
print(r)

# same even function converted to lambda function
p = list(filter(lambda num: num%2==0, seq))
print(p)

# split function takes a string and converts to list on delimiter
st = 'Trump is an asshole! #impotus'
t = st.split('#')
print(t)
# this allows to select on list index
u = st.split("#")[1]
print(u)

# More list stuff
my_list = [0,1,2,3,4]

# add values to within existing list
my_list.extend([5,6])

print(my_list)
bool = 6 in my_list
print(bool)

# pop deletes from the list but note +1 numbering
# my_list.pop(6)
# my_list.pop(5)

# del allows multiple values deleted
del my_list[-2:]

print(my_list)

# add values as NESTED list within list if multiple values
my_list.append([5,6])

print(my_list)
# note that the nested values are NOT in the base list
bool = 6 in my_list
print(bool)
# del function allows more precise deletion of first index value of 
# nested list
del my_list[5][0]
print(my_list)

# single pop statement to remove nested list at end
my_list.pop(5)

print(my_list)

bool = 6 in my_list
print(bool)
