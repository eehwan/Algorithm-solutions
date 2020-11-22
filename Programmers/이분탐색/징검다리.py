def solution(distance, rocks, n):
    rocks.sort()
    start, end = 1, distance
    while start <= end:
        middle = (start + end) // 2
        print("=========================================\n", "middle:", middle)
        pre_rock = 0
        count_rock = 0
        mins = float('inf')
        for rock in rocks:
            print("\nrock:", rock)
            print(rock - pre_rock)
            if middle > rock - pre_rock:
                count_rock += 1
                print("count_rock: ", count_rock)
            else:
                mins = min(mins, rock - pre_rock)
                pre_rock = rock
                print("pre_rock: ", pre_rock)
        if count_rock > n:
            end = middle - 1
        else:
            answer = mins
            start = middle + 1
    return answer

# def solution(distance, rocks, n):
#     rocks.sort()
#     rocks.append(distance)
#     left, right = 0, distance
#     # 바위 사이의 최소거리보다 거리가 작을 경우 돌 삭제.
#     # 거리가 클 경우, 이 값들 중 최솟값을 구해둔다.
#     answer = 0
#     while left <= right:
#         # 이전 돌
#         prev = 0
#         # 돌 거리 최솟값.
#         mins = float("inf")
#         # 제거한 돌 개수
#         removed_rocks = 0
#
#         # 바위 사이의 최소거리
#         mid = (left + right) // 2
#         # 각 돌을 돌면서 제거할 돌을 찾는다.
#         for i in range(len(rocks)):
#             if rocks[i] - prev < mid:
#                 removed_rocks += 1
#             else:
#                 mins = min(mins, rocks[i] - prev)
#                 prev = rocks[i]
#
#         # 제거한 돌 개수가 기준보다 많다 = 바위 제거를 줄여야 한다.
#         # 바위 사이 최소거리의 기준을 낮춰야 한다
#         if removed_rocks > n:
#             right = mid - 1
#
#         # 제거한 돌 개수가 기준보다 적다 = 더 많은 바위 제거가 필요
#         # = 바위 사이 최소거리 기준을 높여야 한다
#         else:
#             answer = mins
#             left = mid + 1
#     return answer

print(solution(26, [2, 5, 14, 17, 23, 24], 3))
