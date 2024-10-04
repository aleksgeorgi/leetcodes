class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        origin = [0,0]
        
        for i in moves:
            if i=="U":
                origin[1] += 1
            if i=="D":
                origin[1] -= 1
            if i=="L":
                origin[0] -= 1
            if i=="R":
                origin[0] += 1
                
        return origin == [0,0]

        
        