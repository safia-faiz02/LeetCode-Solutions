class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r
        while l <= r:
            hours = 0
            k = (l+r)//2
            for p in piles:
                hours += math.ceil(p / k)
            if hours <= h:
                result = min(result,k)
                r = k - 1
            else:
                l = k + 1
        return result 