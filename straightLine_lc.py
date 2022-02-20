from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates)<3:
            return True
        slope1=self.slope(coordinates[0],coordinates[1])

        for i in range(2,len(coordinates)):
            if self.slope(coordinates[0], coordinates[i]) != slope1:
                return False 
        
        return True
        
    def slope(self,p1,p2):
        if p1[0]==p2[0]:
            return 'infinite'
        return (p1[1]-p2[1])/(p1[0]-p2[0])


s=Solution()
coordinates = [[1,3],[2,6],[3,9],[4,12]]
print(s.checkStraightLine(coordinates))





