class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            if len(stack) == 0:
                stack.append(asteroid)
            else:
                while True:
                    last_val = stack.pop()
                    if last_val < 0:
                        stack.append(last_val)
                        stack.append(asteroid)
                        break
                    elif (last_val > 0 and asteroid > 0) or (last_val < 0 and asteroid < 0):
                        stack.append(last_val)
                        stack.append(asteroid)
                        break
                    else:
                        if abs(last_val) > abs(asteroid):
                            stack.append(last_val)
                            break
                        elif abs(last_val) == abs(asteroid):
                            break
                        else:
                            if len(stack) == 0:
                                stack.append(asteroid)
                                break
        return stack