# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from functools import reduce
def fibo(n):
	a, b = 0, 1
	for _ in range(n-1):
		a , b = b, a + b
	return b

n = int(input())
path = str(input())
nums = list(map(fibo, map(len, path.split("0"))))
print(reduce(lambda x, y: x*y, nums, 1))