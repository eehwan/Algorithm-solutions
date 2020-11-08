# def solution(tickets):
#     def dfs(tickets, current, used):
#         for i in range(len(tickets)):
#             if used[i]:
#                 continue
#             if tickets[i][0] != current:
#                 continue
#             # 길이 끊기지 아니한 지 확인
#             canVisit = False
#             for j in range(len(tickets)):
#                 if used[j]:
#                     continue
#                 # 이후에 길을 이을 수 있는지
#                 if tickets[i][1] == tickets[j][0]:
#                     canVisit = True
#                 # 아니면 이 케이스가 맨 마지막 나머지인지
#                 elif len(used) - sum(used) == 1:
#                     canVisit = True
#             if canVisit:
#                 used[i] = 1
#                 result.append(tickets[i][1])
#                 print(tickets, used)
#                 return dfs(tickets, tickets[i][1], used)
#
#     tickets.sort(key=lambda x: x[1])
#     result = ["ICN"]
#     used = [0 for _ in tickets]
#     dfs(tickets, "ICN", used)
#     return result
#
def solution(tickets):
    tickets.sort(reverse=True)
    routes = dict()
    for t1, t2 in tickets:
        if t1 in routes:
            routes[t1].append(t2)
        else:
            routes[t1] = [t2]
    print(routes)
    st = ['ICN']
    ans = []
    while st:
        top = st[-1]
        if top not in routes or len(routes[top])==0:
            ans.append(st.pop())
            print(f"ans: {ans}")
        else:
            st.append(routes[top].pop())
            print(f"st: {st}")
        print(routes)
    ans.reverse()
    return ans

print(solution([["ICN", "A"], ["ICN", "B"], ["B", "c"], ["c", "B"], ["B", "ICN"]]))
