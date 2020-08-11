import sys

rep = int(sys.stdin.readline())
time_table = [""]*rep
for i in range(rep):
    time_table[i] = list(map(int,sys.stdin.readline().split()))

def set_time(table):
    table = sorted(time_table,key=lambda x: (x[1],x[0]))

    count = 0
    end_time = 0
    for index in table:
        if (index[0]>=end_time):
            count+=1
            end_time = index[1]
    return count

print(set_time(time_table))
