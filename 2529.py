import sys

rep = int(sys.stdin.readline())
signs = list(map(str, sys.stdin.readline().split()))

nums = ["0","1","2","3","4","5","6","7","8","9"]
max_nums = []
for i in range(rep):
    # print("\n i : ",i,"\n")
    count=0
    for j in range(i,rep+1):
        # print(" j : ",j)
        if(j==rep or signs[j]==">"):
            # print(" generate")
            max_nums.append(nums.pop(-1-count))
            break
        else:
            # print(" count +")
            count+=1
max_nums.append(nums.pop(-1))
print("".join(max_nums))

nums = ["0","1","2","3","4","5","6","7","8","9"]
min_nums = []
for i in range(rep):
    # print("\n i : ",i,"\n")
    count=0
    for j in range(i,rep+1):
        # print(" j : ",j)
        if(j==rep or signs[j]=="<"):
            min_nums.append(nums.pop(count))
            break
        else:
            # print(" count +")
            count+=1
min_nums.append(nums.pop(0))
print("".join(min_nums))
