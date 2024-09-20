class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # using a max heap 
        N = len(score)
        
        # create a heap of pairs (score, index)
        heap = []
        for index, score in enumerate(score):
            heapq.heappush(heap, (-score, index))
        
        # assign the rank to the athletes 
        rank = [0] * N # premake the list so we can index into it
        place = 1
        while heap:
            # get the original index from the heap element and place it into the list index 
            original_index = heapq.heappop(heap)[1] # the 1 index contains the original index, 0 is the score
            if place == 1:
                rank[original_index] = "Gold Medal"
            elif place == 2:
                rank[original_index] = "Silver Medal"
            elif place == 3:
                rank[original_index] = "Bronze Medal"
            else:
                rank[original_index] = str(place)
            place += 1
            
        return rank

        