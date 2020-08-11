import sys

x, y = map(int, sys.stdin.readline().split())
A = []
B = []

for i in range(x):
    A.append(list(str(input())))
for i in range(x):
    B.append(list(str(input())))
# print(" A : ",A)
# print(" B : ",B)
def check_under33(matrix1,matrix2):
    if matrix1==matrix2:
        return 0
    return -1
def check_over33(matrix1,matrix2):
    count = 0
    for i in range(x-2):
        for j in range(y-2):
            if (matrix1==matrix2):
                return count
            else:
                for a in range(i,i+3):
                    for b in range(j,j+3):
                        if(matrix1[a][b]=="1"):
                            matrix1[a][b]="0"
                            # print(f"[{a}],[{b}] changed to 0")
                        else:
                            matrix1[a][b]="1"
                            # print(f"[{a}],[{b}] changed to 1")
                count += 1
    if (matrix1==matrix2):
        return count
    else:
        # print(f"matrix1 : {matrix1}\nmatrix2 : {matrix2}")
        return -1
def distinc(matrix1,matrix2):
    if ((x < 3) or (y < 3)):
        # print("under")
        print(check_under33(matrix1, matrix2))
    else:
        # print("over")
        print(check_over33(matrix1, matrix2))
distinc(A,B)
