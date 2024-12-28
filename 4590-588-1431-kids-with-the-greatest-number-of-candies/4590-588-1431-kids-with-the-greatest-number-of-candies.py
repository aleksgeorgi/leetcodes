class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # find the current greatest:
        max_curr_val = max(candies)
        res = []

        for candy in candies:
            if candy+extraCandies >= max_curr_val:
                res.append(True)
            else:
                res.append(False)

        return res