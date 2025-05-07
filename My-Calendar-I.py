class Node:
    def __init__(self,start,end,left=None,right=None):
        self.start=start
        self.end=end
        self.left=left
        self.right=right
class MyCalendar:
    def __init__(self):
        self.root=None

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root=Node(startTime,endTime)
            return True
        return self.insert(self.root,startTime,endTime)
    def insert(self, node,start,end)-> bool:
        if end<=node.start:
            if not node.left:
                node.left=Node(start,end)
                return True
            return self.insert(node.left,start,end)
        elif start>=node.end:
                if not node.right:
                    node.right=Node(start,end)
                    return True
                return self.insert(node.right,start,end)
        else:
            return False
            

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)