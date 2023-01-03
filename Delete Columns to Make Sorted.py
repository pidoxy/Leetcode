class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        answer = 0
        M = len(strs)
        N = len(strs[0])
        
        # Iterate over each index in the string.
        for col in range(M):
            for row in range(N-1):
                if strs[row][col] > strs[row + 1][col]:
                    answer += 1
                    break
        return answer

        # N=len(strs)
        # M=len(strs[0])
        # deleted_column=0
        # for col in range(M):
        #     for row in range(N-1):
        #         if strs[row][col] > strs[row+1][col]:
        #             deleted_column+=1
        #             break
        # return deleted_column





        # hash = defaultdict(list)

        # # for i in range(len(strs)):
        # #     for j in range(len(strs[i])):
        # #         print(i,j)
        # i = 0
        # j = 0
        # column = 0
        # prev = 0

        # while i < len(strs) and j < len(strs[0]):
        #     # print(i,j)
        #     # if hash[i]:
        #     #     hash[i].append(strs[i][j])
        #     # else:
        #     #     hash[i] = [strs[i][j]]
        #     # print(strs[i][j], prev)
        #     # print(ord(strs[i][j]) < prev)
        #     if i == 0:
        #         prev = ord(strs[i][j])
        #     else:
        #         if (prev > ord(strs[i][j]) ) : 
        #             # column +=1
        #             print(True, i)
        #             hash[i] = 1
        #         prev = ord(strs[i][j])
        #     if (i == len(strs)-1) and (j != len(strs)-1):
        #         j += 1
        #         i = 0
        #         prev = 0
        #     else: 
        #         i += 1
        # print(hash)
        # for value in hash.values():
        #     column += value
        #     print(value)
        # return column
