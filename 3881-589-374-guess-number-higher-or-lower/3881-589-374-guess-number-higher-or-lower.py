# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        while (low <= high):
            p = low + (high - low) // 2
            res = guess(p)
            if res==0:
                return p
            elif res==1: # my guess was too low
                low = p + 1
            else: # my guess was too high
                high = p - 1

        return -1

        