def solution(bandage, health, attacks):
    hp, max_hp = health, health
    latest_time = 0

    for time, damage in attacks:
        cure_duration = max(time - latest_time - 1, 0)
        latest_time = time

        hp += cure_duration * bandage[1] + cure_duration // bandage[0] * bandage[2]
        hp = min(hp, max_hp)
        hp -= damage 
        
        if hp <= 0:
            return -1

    return hp

# test_cases = [
#     ([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]),
#     ([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]),
#     ([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]),
#     ([1, 1, 1], 5, [[1, 2], [3, 2]]),
# ]
# print(*map(lambda x: solution(*x), test_cases))