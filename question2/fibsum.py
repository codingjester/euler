#!/usr/bin/env python

cache = {}
def fib(n):
    cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fib(n-1) + fib(n-2))
    return cache[n]

sum = 0
int = 0
while fib(int) <= 4000000:
    if not fib(int) % 2: sum = sum + fib(int)
    int = int + 1

#print cache
print sum
