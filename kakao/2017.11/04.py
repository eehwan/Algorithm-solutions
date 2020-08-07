import sys
from datetime import datetime as dt
# musicinfos:list = sys.stdin.readline()

m = list(input().replace("\"",""))
musicinfos = list(map(str,input().replace("[","").replace("]","").replace("\"","").split(", ")))

for i in range(len(musicinfos)):
    a,b,c,d = list(musicinfos[i].split(","))

    duration = round((dt.strptime(b,'%H:%M')-dt.strptime(a,'%H:%M')).seconds/60)
    if duration>len(d)-d.count("#"):
        share = duration//(len(d)-d.count("#"))
        remainder = duration%(len(d)-d.count("#"))
        d = d*share+ d[:remainder+d.count("#")]

    else:
        d = d[:duration+d.count("#")]
    musicinfos[i] = [c,list(d),duration]

print("\n musicinfos : ")
for _ in musicinfos:
    print(_)

result = []
for i in range(len(musicinfos)):
    for j in range(len(m)):
        if len(musicinfos[i][1])<j+len(m):
            break
        if m[0] == musicinfos[i][1][j]:
            # print(f"{musicinfos[i]}의 {j}번째")
            # print(musicinfos[i][1][j:j+len(m)])
            # print(m)
            if m == musicinfos[i][1][j:j+len(m)]:
                result.append(musicinfos[i])
                break
result.sort(key=lambda info: info[2],reverse=True)

print("\n result :")
if result==[]:
    print("(None)")
else:
    print(result[0][0])



"""
“ABCDEFG”
[“12:00,12:14,HELLO,CDEFGAB”, “13:00,13:05,WORLD,ABCDEF”]
“CC#BCC#BCC#BCC#B”
[“03:00,03:30,FOO,CC#B”, “04:00,04:08,BAR,CC#BCC#BCC#B”]
“ABC”
[“12:00,12:14,HELLO,C#DEFGAB”, “13:00,13:05,WORLD,ABCDEF”]
"""
