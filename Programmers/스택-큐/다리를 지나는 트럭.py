def solution(bridge_length, weight, truck_weights):
    current = [[truck_weights.pop(0),bridge_length]]
    sum_weight = current[0][0]
    time = 1
    while current!=[]:
        print(time, current)
        print(f"remain = {truck_weights}")
        for i,value in enumerate(current):
            current[i][1]-=1
        if current[0][1]==0:
            print(f"pop : {current[i]}")
            sum_weight-=current[0][0]
            current.pop(0)
        if truck_weights!=[] and sum_weight+truck_weights[0]<=weight:
            current.append([truck_weights.pop(0),bridge_length])
            sum_weight+=current[-1][0]
        time+=1
    return time

"""
import collections

DUMMY_TRUCK = 0


class Bridge(object):

    def __init__(self, length, weight):
        self._max_length = length
        self._max_weight = weight
        self._queue = collections.deque()
        self._current_weight = 0

    def push(self, truck):
        next_weight = self._current_weight + truck
        if next_weight <= self._max_weight and len(self._queue) < self._max_length:
            self._queue.append(truck)
            self._current_weight = next_weight
            return True
        else:
            return False

    def pop(self):
        item = self._queue.popleft()
        self._current_weight -= item
        return item

    def __len__(self):
        return len(self._queue)

    def __repr__(self):
        return 'Bridge({}/{} : [{}])'.format(self._current_weight, self._max_weight, list(self._queue))


def solution(bridge_length, weight, truck_weights):
    bridge = Bridge(bridge_length, weight)
    trucks = collections.deque(w for w in truck_weights)

    for _ in range(bridge_length):
        bridge.push(DUMMY_TRUCK)

    count = 0
    while trucks:
        bridge.pop()

        if bridge.push(trucks[0]):
            trucks.popleft()
        else:
            bridge.push(DUMMY_TRUCK)

        count += 1

    while bridge:
        bridge.pop()
        count += 1

    return count


def main():
    print(solution(2, 10, [7, 4, 5, 6]), 8)
    print(solution(100, 100, [10]), 101)
    print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 110)


if __name__ == '__main__':
    main()
"""

test_case = """
[\
2, 10, [7, 4, 5, 6]
100, 100, [10]
100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
]
"""
expected_value="""
[\
8
101
110
]
"""

print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
))
