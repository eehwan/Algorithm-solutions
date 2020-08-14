import heapq
def solution(jobs):
    jobs.sort(key = lambda x : (x[0],x[1]))
    length = len(jobs)
    time = 0
    total = 0
    queue_list = []
    while True:
        while jobs:
            if jobs[0][0] <= time:
                print(f"jobs = {jobs}")
                temp1 = jobs.pop(0)
                print(f"temp1 = {temp1}")
                heapq.heappush(queue_list,(temp1[1],temp1[0]))
                print(f"queue_list = {queue_list}")
            else:
                if queue_list == []:
                    time += 1
                else:
                    break
        temp2 = heapq.heappop(queue_list)
        time += temp2[0]
        total += time - temp2[1]
        print(f"temp2 = {temp2}")
        print(f"queue_list = {queue_list}")
        print(f"time = {time}")
        print(f"total = {total}")
        print("--------------------------")
        if queue_list==[] and jobs ==[]:
            break
    return int(total/length)



print(solution([[0, 1], [3, 9], [3, 6]]))
