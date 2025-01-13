class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            # collision
            if stack and stack[-1] > 0 and asteroid < 0:

                # smaller right moving asteroids getting absorbed
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroid):
                    stack.pop()
                # Bigger right moving asteroid absorbs current
                if stack and stack[-1] > abs(asteroid):
                    continue
                # Both get absorbed
                elif stack and stack[-1] == abs(asteroid):
                    stack.pop()
                    continue
                
            stack.append(asteroid)

        return stack


        