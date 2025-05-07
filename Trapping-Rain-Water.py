class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax=rightMax=total=0
        low=0
        high=len(height)-1
        while low<high:
            if height[low]<=height[high]:
                if height[low]<leftMax:
                    total+=leftMax-height[low]
                else:
                    leftMax=height[low]
                low+=1
            else:
                rightMax=max(rightMax,height[high])
                if height[high]<rightMax:
                
                    total+=rightMax-height[high]
                else:
                    rightMax=height[high]
                high-=1
        return total


            

        