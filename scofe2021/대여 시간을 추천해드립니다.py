# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = input()
start = ["00", "00"]
end = ["23", "59"]
for _ in range(int(n)):
	startTemp, endTemp = input().split(" ~ ")
	startHour, startMin = startTemp.split(":")
	endHour, endMin = endTemp.split(":")
	if int(startHour) > int(start[0]):
		start[0] = startHour
		start[1] = startMin
	elif int(startHour) == int(start[0]) and int(startMin) > int(start[1]):
		start[1] = startMin
	if int(endHour) < int(end[0]):
		end[0] = endHour
		end[1] = endMin
	elif int(endHour) == int(end[0]) and int(endMin) < int(end[1]):
		end[1] = endMin
if start[0] > end[0] or (start[0] == end[0] and start[1] >= end[1]):
	print("-1")
else:
	print(f"{':'.join(start)} ~ {':'.join(end)}")