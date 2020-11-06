def solution(tickets):
    def dfs(tickets, current, used):
        for i in range(len(tickets)):
            if used[i]:
                continue
            if tickets[i][0] == current:
                used[i] = 1
                result.append(tickets[i][1])
                return(dfs(tickets, tickets[i][1], used))

    tickets.sort(key=lambda x: x[1])
    result = ["ICN"]
    used = [0 for _ in tickets]
    dfs(tickets, "ICN", used)
    return result

print(solution([["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
