import re
def solution(record):
    uid_dict = {}
    messages = []
    for rec in record:
        x = rec.split(" ") 
        comm = x[0].strip()
        uid = x[1].strip()
        name = x[2] if len(x) > 2 else ""

        if comm == "Enter":
            messages.append(f"{uid}님이 들어왔습니다.")
        elif comm == "Leave":
            messages.append(f"{uid}님이 나갔습니다.")

        if comm in ["Enter", "Change"]:
            uid_dict[uid] = name

    pattern = re.compile(r"(.+?)님이 (들어왔습니다|나갔습니다)")
    def replace_name(match):
        uid = match.group(1)
        status = match.group(2)
        return f"{uid_dict.get(uid, uid)}님이 {status}"

    answer = [pattern.sub(replace_name, msg) for msg in messages]

    return answer

if __name__ == "__main__":
    test_case = [
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"],
    ]

    print(*map(solution, test_case), sep="\n")