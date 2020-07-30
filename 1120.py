import sys

a, b= map(str,sys.stdin.readline().split())
a_letter=list(a)
b_letter=list(b)

len_a = len(a_letter)
len_b = len(b_letter)
count = 50
for i in range(len_b - len_a+1):
    count_tmp = 0
    for j in range(len_a):
        print("{}번째 +{} a, b: {},{}".format(j,i,a_letter[j],b_letter[j+i]))
        if (a_letter[j]!=b_letter[j+i]):
            count_tmp += 1
        print(count_tmp)
    count = count_tmp if count_tmp < count else count

print(count)
