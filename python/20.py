#!/usr/bin/env python

def factorial(n):
    mult = 1
    while n > 0:
        mult *= n
        n -= 1
    return mult
    

print sum([int(x) for x in str(factorial(100))])

#Kind of a more fun way to do it using lambdas and reduce
print sum([int(x) for x in str(reduce(lambda x, y: x*y, xrange(1,100)))])
