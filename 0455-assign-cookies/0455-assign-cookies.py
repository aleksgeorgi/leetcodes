class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        
        g = sorted(g)
        s = sorted(s)
        count = 0 
        s_index = len(s)-1
        
        for child in range(len(g)-1, -1, -1): #iterate backwards
            # print(f"child: {child}, s_index: {s_index}")
            if s_index < 0:
                break # we've used all the cookies
            elif g[child] <= s[s_index]:
                count += 1
                s_index -= 1
            else:
                continue 
                
        return count 
            
        