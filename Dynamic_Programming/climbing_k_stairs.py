n = int(input())
k = int(input())

def number_of_ways(n):
    if n == 0:
        return 1
    sum_of_ways = 0
    for i in range(1, k + 1):
        if n - 1 >= 0:
            sum_of_ways += number_of_ways(n - i)
    return sum_of_ways
print(number_of_ways(n))