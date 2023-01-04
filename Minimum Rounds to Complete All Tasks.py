class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        hash = defaultdict(list)
        rounds = 0
        for i in tasks:
            if hash[i]:
                hash[i] += 1
            else:
                hash[i] = 1
        # print(hash)

        val = [value for value in hash.values()]
        print(val)
        for i in val:
            if i == 1:
                return -1
            elif i == 2 or i == 3:
                rounds += 1
                print(rounds)
            elif i > 3 and (i%3 == 2):
                # print(i % 3)
                rounds = rounds + i // 3 + 1
                print(rounds)
            elif i > 3 and (i%3 == 1):
                # here is a condition that if it remains 1 then instead of 3 per the last round, 2 per the last 2 rounds could be used to complete it
                rounds = rounds + i // 3 + 1
                print(rounds)
            elif i > 3 and (i%3 == 0):
                # no remainder if divided by 3
                rounds = rounds + i // 3
                print(rounds)
        return rounds
                
