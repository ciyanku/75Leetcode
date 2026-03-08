class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        size = len(flowerbed)

        for i in range(size):
            if flowerbed[i] == 0 and \
               (i == 0 or flowerbed[i-1] == 0) and \
               (i == size-1 or flowerbed[i+1] == 0):

                flowerbed[i] = 1
                n -= 1

        return n <= 0