class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        seen=set()
        seen.add(source)
        #-----------BFS------------
        q=deque()
        q.append(source)

        while q:
            node=q.popleft()
            if node==destination:
                return True
            for nei_node in graph[node]:
                if nei_node not in seen:
                    seen.add(nei_node)
                    q.append(nei_node)
        return False


        
        #--------DFS recursive----------

        # def dfs(node):
        #     if node==destination:
        #         return True
        #     for nei_node in graph[node]:
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             if dfs(nei_node):
        #                 return True
                
        #     return False 
        # return dfs(source)
        #----------DFS iterative----------
        # stack=[source]

        # while stack:
        #     node=stack.pop()
        #     if node==destination:
        #         return True
        #     for nei_node in graph[node]:
        #         if nei_node not in seen:
        #             seen.add(nei_node)
        #             stack.append(nei_node)
                
        # return False 
        