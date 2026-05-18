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
            if x > 0 and stack and stack[-1] < 0:
                top = -1 * stack[-1]

                if top > x:
                    stack.pop()
                elif top == x:
                    stack.pop()
                    continue
                else:
                    continue
            
            if x < 0 and stack and stack[-1] > 0:
                top = stack[-1]
                y = -x

                if top > y:
                    stack.pop()
                elif top == y:
                    stack.pop()
                    continue
                else:
                    continue

            stack.append(x)

        return stack
