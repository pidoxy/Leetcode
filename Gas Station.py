class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#       O(n^2) time
        N = len(gas)

        for i in range(N):
            tank = 0
            for j in range(N):
                print(cost[(i+j)%N])
                # print((i+j)%N)
                tank += gas[(i+j)%N]
                tank -= cost[(i+j)%N]
                if tank < 0 : break
                if j == N-1: return i
        return -1

#       O(n) time - Greedy solution
        total = 0
        res = 0
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            print(total)

            if total < 0:
                total = 0
                res = i + 1
        return res
