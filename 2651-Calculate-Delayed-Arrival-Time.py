class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        if delayedTime==0:
            return arrivalTime
        actTime=arrivalTime+delayedTime
        return actTime if actTime<24 else actTime-24
        