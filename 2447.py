n = int(input())
max = n

def star(n):
    arr =[["*"]*max]*max
    if (n==3):
        for k in range(3):
            for j in range(3):
                # print(j)
                if (k==1 and j==1):
                    arr[k][j]= " "
    return arr
    for i in range(n):
        for j in range(n):
            if (i>=n/3 and i<n*2/3 and j>=n/3 and j<n*2/3):
                arr[i][j]=" "
            else:
                a = i%(3)
                b = j%(3)
                arr[i][j]=star(n/3)[a][b]
    return arr

# for i in range(n):
#     for j in range(n):
#         print(star(n)[i][j], end="")
#     print()
print(star(n))

# pic = ['*'] * n * n
# st_num = n
#
# def star_write(n):
#   for i in range(st_num):
#     for j in range(st_num):
#       if i%n >= n/3 and i%n < 2*n/3 and j%n >= n/3 and j%n < 2*n/3:
#         pic[j+i*st_num] = ' '
#   if n != 3:
#     star_write(int(n/3))
#   else:
#     for i in range(st_num):
#       for j in range(st_num):
#         print(pic[j+i*st_num], end='')
#       print()
#
# star_write(n)
