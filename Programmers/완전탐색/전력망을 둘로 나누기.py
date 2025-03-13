def solution(n, wires):
    
    def getMaxConnectionCnt(wires):
        startPoint = wires[0]
        connected = { startPoint[0], startPoint[1]}
        for x, y in wires[1:]:
            if (x in connected): connected.add(y)
            if (y in connected): connected.add(x)
        return len(connected)
    
    connectionCnts = []
    for i in range(n-1):
        newWires = [v for idx, v in enumerate(wires) if idx != i]
        cnt = getMaxConnectionCnt(newWires)
        connectionCnts.append(cnt)
    
    return min(map(lambda x: abs(n - 2 * x), connectionCnts))