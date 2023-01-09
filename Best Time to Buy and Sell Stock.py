class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' can't sell on 1st day
        can't buy and sell at a later date - left to right
        '''

        # O(n^2) time - too slow - brutal force
        res = 0
        for i in range(len(prices)):
            buy = prices[i]
            for j in range(i+1,len(prices)):
                sell = prices[j]
                profit = sell - buy
                # print(profit)

                if profit > 0:
                    res = max(res, profit)
        # print(res)
        return res
        
        # O(n) time - jargons that passes only 156 test cases
        l,r = 0, len(prices)-1
        res = 0

        while l != r:
            buy = prices[l]
            sell = prices[r]
            profit = sell - buy

            if profit > 0:
                res = max(res, profit)
            if buy > sell:
                l += 1
            elif buy < sell:
                r -= 1
            elif prices[l+1] < prices[r-1]:
                r -= 1
            else:
                l += 1

        l,r = 0, len(prices)-1
        while l != r:
            buy = prices[l]
            sell = prices[r]
            profit = sell - buy

            if profit > 0:
                res = max(res, profit)
            if buy < sell:
                l += 1
            elif buy > sell:
                r -= 1
            elif prices[l+1] > prices[r-1]:
                r -= 1
            else:
                l += 1

        print(res)
        return res

        buy = prices[0]
        profit = 0

        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            profit = max(profit, prices[i]-buy)
        return profit


