# 1번 문제
import copy
class TIME:
    def __init__(self, input: str):
        if input.count(":") < 2:
            self.minute = int(input.split(":")[0])
            self.second = int(input.split(":")[1])
        else:
            hour = int(input.split(":")[0])
            self.minute = int(input.split(":")[1]) + hour * 60
            self.second = int(input.split(":")[2])
    def __add__(self, other):
        tempSecond = (self.second + other.second)
        self.second = tempSecond % 60
        self.minute += (other.minute + tempSecond//60)
        return self
    def __sub__(self, other):
        tempSecond = self.second - other.second
        tempMinute = self.minute - other.minute
        if tempSecond < 0:
            tempSecond += 60
            tempMinute -= 1
        self.second = tempSecond
        self.minute = tempMinute
        return self
    # def __lt__(self, other):
    #     if self.minute > other.minute:
    #         return False
    #     elif self.second > other.second:
    #         return False
    #     else: return True
    # def __gt__(self, other):
    #     if self.minute < other.minute:
    #         return False
    #     elif self.second < other.second:
    #         return False
    #     else: return True

    def __str__(self):
        if self.minute >= 60:
            return f"{self.minute}:{self.second}"
        return f"{self.minute//60}:{self.minute%60}:{self.second}"

n, excTime = input().split(" ")
n, excTime = int(n), TIME(excTime)
# print("excTIME : ", excTime)
songs = []
for _ in range(n):
    songs.append(TIME(input()))

songCnt = 0
songStart = 0
for i in range(n):
    time = copy.deepcopy(excTime)
    for j in range(i, n):
        time -= songs[j]
        # print(i,j,time)
        if songCnt < j - i + 1:
            songCnt = j - i + 1
            songStart = i + 1
        if str(time)[0] == "-" or str(time) == "0:0:0":
            break
    #     print("--------------------")
    # print(songCnt)
print(songCnt, songStart)