class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n <= 1:
                return True
            if n < 1:
                return True
        else:
            for i in range(len(flowerbed)):
                if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
                elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] == 0:
                    count += 1
                elif flowerbed[i] == 0 and flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    flowerbed[i] = 1
                    count += 1
        return True if count >= n else False