class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        result=[[float('inf')]*cols for _ in range(rows)]
        queue=deque()

        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    queue.append((i,j))
                    result[i][j]=0
        while queue:
            x,y=queue.popleft()
            for dx,dy in directions:
                newx, newy=x+dx, y+dy
                if 0<=newx<rows and 0<=newy<cols and result[newx][newy] > result[x][y]+1:
                    result[newx][newy]=result[x][y]+1
                    queue.append((newx,newy))
        return result


        
        