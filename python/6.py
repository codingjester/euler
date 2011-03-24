#!/usr/bin/env python

nums = xrange(1,101)
nums_sum = sum(nums)
answer = nums_sum*nums_sum - sum([x*x for x in nums])
print answer
