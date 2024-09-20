class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        '''
        sort the score list
        create a placements array 
        store the score list and placements into a hashmap (dictionary)
        read the original input and lookup placement 
        '''
        
        #sort the score list 
        scores_asc = sorted(score)
        #reverse the list 
        scores_desc = scores_asc[::-1]
        
        placements = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        if len(score) > 3:
            for i in range(3, len(score)):
                placements.append(str(i+1))
                
        # add the scores and placements to a dictionary 
        score_map = {}
        for i in range(len(scores_desc)):
            score_map[scores_desc[i]] = placements[i]
            
        # iterate through original scores and append the ranking 
        answer = []
        for i in range(len(score)):
            answer.append(score_map.get(score[i]))
            
        return answer
        
        
            

        