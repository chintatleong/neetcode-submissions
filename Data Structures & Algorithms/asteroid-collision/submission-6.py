class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # indice of asteroids = relative positions in space
        # value of that index represent its size
        # sign represent the direction 
        # if two asteroids meet, smaller gone, same size both gone
        # same direction = never meet
        # [2,4,-4,-1]
        stack = []
        
        for x in asteroids:
            if stack:
                while (stack[-1] > 0 and x < 0):
                    y = -x

                    if y > stack[-1]:
                        stack.pop()
                    elif y == stack[-1]:
                        stack.pop()
                        x = 0
                    else:
                        x= 0
                        break

                while (stack[-1] < 0 and x > 0):
                    top = stack[-1]
                    top_size = -top

                    if x > top_size:
                        stack.pop()
                    elif x == top_size:
                        stack.pop()
                        x = 0
                    else:
                        x = 0
                        continue
                
                if not x == 0:
                    stack.append(x)

                

            if not stack:
                stack.append(x)

        return stack
