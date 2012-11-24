#!/usr/bin/env python

def is_palindrome(num):
    return str(num) == str(num)[::-1]
""""
numbers = []
for a in range(100,1000):
    for b in range(a, 1000):
         product = a * b
         if is_palindrome(product):
             numbers.append(product)
print max(numbers)

OR the answer below. Either way.
"""
print max([a*b for a in range(100, 1000) for b in range(a, 1000) if is_palindrome(a*b)])
