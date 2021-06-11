import re

def solution(new_id):
    print(re.sub("[^\w(\-|_|\.)]", "", new_id.lower()))
    answer = re.sub("[\.]+", ".", re.sub("[^\w\-|_|\.]", "", new_id.lower())).strip(".")[:15].rstrip(".")
    print(answer)
    if len(answer) == 0:
        answer = "a"
    if len(answer) < 3:
        while len(answer) < 3:
            answer += answer[-1:]
    return answer

print(solution(	"......"))