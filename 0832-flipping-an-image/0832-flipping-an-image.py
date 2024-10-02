class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        rev_list_inv = []
        
        for row in image:
            rev_list_inv.append(list(map(lambda x: 0 if x==1 else 1, row[::-1])))
                    
        return rev_list_inv
        