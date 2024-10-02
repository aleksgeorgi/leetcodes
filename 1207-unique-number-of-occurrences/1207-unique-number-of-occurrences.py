class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        occDict = {}
        
        # populate the map
        for num in arr:
            if num in occDict:
                occDict[num] = occDict[num] + 1
            else:
                occDict[num] = 1
                
        if len(occDict.values()) != len(set(occDict.values())):
            return False
        
        return True
        