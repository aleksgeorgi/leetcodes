class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0 
        maxAlt = alt
        for i in range(len(gain)):
            alt += gain[i]
            maxAlt = max(maxAlt, alt)
        return maxAlt
        