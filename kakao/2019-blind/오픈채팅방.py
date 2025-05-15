def solution(record):
    uid_dict = {}
    answer = []

    for rec in record:
        parts = rec.split()
        command, uid = parts[0], parts[1]
        if command in ("Enter", "Change"):
            uid_dict[uid] = parts[2]

    for rec in record:
        parts = rec.split() 
        command, uid, name = parts[0], parts[1], uid_dict[parts[1]]

        if command == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        elif command == "Leave":
            answer.append(f"{name}님이 나갔습니다.")

    return answer

if __name__ == "__main__":
    test_case = [
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"],
    ]

    print(*map(solution, test_case), sep="\n")