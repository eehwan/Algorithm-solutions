import sys
import math
num, rep = map(int, sys.stdin.readline().split())

price_1 = 1000
price_2 = 1000
for i in range(rep):
    a, b = map(int, sys.stdin.readline().split())
    if a<price_1:
        price_1 = a
    if b<price_2:
        price_2 = b

if(price_1 > price_2*6):
    result = price_2*num
    print("1 x",num)
else:
    result = math.floor(num/6)*price_1\
    + ((num%6)*price_2\
    if (num%6)*price_2 < price_1 else price_1)
    print("6 x",math.floor(num/6),"1 x",(num%6))
print(result)
