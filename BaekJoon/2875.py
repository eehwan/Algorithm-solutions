import sys
import math

w, m , c = map(int,sys.stdin.readline().split())
if w > m*2:
    team_count = m
    w -= 2*team_count
    m -= team_count

else :
    team_count = math.floor(w/2)
    w -= 2*team_count
    m -= team_count

if c> w + m:
    c -= w + m
    team_count -= math.ceil(c/3)

print(team_count>=0 and team_count or 0)
