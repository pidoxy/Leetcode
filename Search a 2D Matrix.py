class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)-1
        res = False
        while l <= r:
            mid = (l+r)//2
            guess = matrix[mid]

            low, high = 0, len(guess)-1

            while low <= high:
                middle = (low+high)//2
                current = guess[middle]
                print(current)

                if target == current:
                    res = True
                    return True
                elif target < current:
                    high = middle - 1
                else:
                    low = middle+1

            if not res:
                if target == guess[0]:
                    return True
                elif target < guess[0]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                return res
            # return False

            
