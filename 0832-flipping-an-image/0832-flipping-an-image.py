class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        rev_list_inv = []
        
        for row in image:
            rev_list = row[::-1]
            for i in range(len(rev_list)):
                if rev_list[i] == 1:
                    rev_list[i] = 0
                else:
                    rev_list[i] = 1
            rev_list_inv.append(rev_list)
                    
        return rev_list_inv
        