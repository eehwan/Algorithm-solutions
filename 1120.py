import sys

a, b= map(str,sys.stdin.readline().split())
a_letter=list(a)
b_letter=list(b)

count = 0
len_a = len(a_letter)
len_b = len(b_letter)
if (len_b>len_a):
    len_a, len_b = len_b, len_a

count_1 = 0
for i in range(len_b-1):
    if (a_letter[i]!=b_letter[i]):
        count_1 += 1
count_2 = 0
for i in range(len_b-1):
    k = len_a-len_b+i
    if (a_letter[k]!=b_letter[i]):
        count_2 += 1

count = count_1<count_2 and count_1 or count_2
print(count)
