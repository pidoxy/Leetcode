class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        # slope = collections.defaultdict(int)
        # for i in range(len(points)):
        #     for j in range(i+1, len(points)):
        #         y = points[j][1]- points[i][1]
        #         if points[j][0] == points[i][0]:
        #             ans = float('inf')
        #         else:
        #             x = points[j][0] - points[i][0]
        #             ans = y/x
        #         if slope[ans]:
        #             slope[ans] += 1
        #         else:
        #             slope[ans] = 1
        # print(slope)
        # res = max(slope.values())
        # return res

        res = 1
        for i in range(len(points)):
            count = collections.defaultdict(int)
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                if p2[0] == p1[0]:
                    slope = float('inf')
                else:
                    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
                count[slope] += 1
                res = max(res, count[slope] + 1)
        print(count)
        return res
