from collections import deque

class FordFulkerson:
    def __init__(self, n, source, sink):
        self.n = n
        self.source = source
        self.sink = sink
        self.graph = {i: {} for i in range(n)}
        self.flow = {i: {} for i in range(n)}

    def add_edge(self, u, v, capacity):

        self.graph[u][v] = capacity
        self.graph[v][u] = 0
        self.flow[u][v] = 0
        self.flow[v][u] = 0

    def _bfs(self, parent):

        visited = set()
        queue = deque([self.source])
        visited.add(self.source)

        while queue:
            node = queue.popleft()
            for neighbor, capacity in self.graph[node].items():
                residual_capacity = capacity - self.flow[node].get(neighbor, 0)
                if neighbor not in visited and residual_capacity > 0:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    parent[neighbor] = node
                    if neighbor == self.sink:
                        return True
        return False

    def max_flow(self):

        max_flow = 0
        parent = {}

        while self._bfs(parent):

            path_flow = float('Inf')
            v = self.sink
            while v != self.source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v] - self.flow[u][v])
                v = parent[v]


            v = self.sink
            while v != self.source:
                u = parent[v]
                self.flow[u][v] += path_flow
                self.flow[v][u] -= path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow, self.flow
