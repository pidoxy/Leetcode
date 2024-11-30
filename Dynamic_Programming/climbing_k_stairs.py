import time
start_time = time.time()

n = int(input())
k = int(input())

dp = [-1 for i in range(n+1)]

def number_of_ways(n):
    
    if n == 0:
        return 1
    if dp[n] != -1:
        return dp[n]
    sum_of_ways = 0

    for i in range(1, k + 1):
        if n - 1 >= 0:
            sum_of_ways += number_of_ways(n - i)
    dp[n] = sum_of_ways
    return dp[n]
print(number_of_ways(n))


end_time = time.time()
execution_time = end_time - start_time
print("Execution time:",execution_time)