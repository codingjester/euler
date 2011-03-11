#!/usr/bin/env python

print sum([num for num in xrange(1,1000) if num % 3 == 0 or num % 5 == 0])

#The if statment the real answer does pretty well too
print sum([num for num in xrange(1,1000) if not num % 3 or not num % 5])
