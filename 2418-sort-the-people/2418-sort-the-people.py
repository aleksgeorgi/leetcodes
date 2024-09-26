class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # max heap / priorty queue O(N)
        # find the minimum in heights, push the name index onto a stack O(N^2)
        
        # dictionary O(N)
        # key: height, value: index 
        sorted_names = []
        
        names_and_heights = dict(zip(heights, names))
        for index, value in enumerate(sorted(names_and_heights.items(), reverse=True)):
            sorted_names.append(value[1])
        
#         sorted_heights = sorted(heights, reverse = True)
        
#         sorted_names = [names_and_heights[height] for height in sorted_heights]
        
        return sorted_names
        
        