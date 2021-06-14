def collectGas(gas, cost):  

    for i in range(0,len(gas)):
        start = i
        current = start
        total, stops = 0, 0
        print(len(gas),i,current)
        while total >= 0:
            

            if stops >= len(gas):
                # full circle
                return start

            total += (gas[current] - cost[current])
            stops += 1
            current = (current + 1) % len(gas)

    return -1


gas1 = [5,1,2,3,4]
cost1 = [4,4,1,5,1]

print(complete(gas1, cost1))
