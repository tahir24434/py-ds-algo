from pdsa.lib.Queue.array_queue import Queue

class Vertex:
    def __init__(self, e):
        self._element = e

    def element(self):
        return self._element


class Edge:
    def __init__(self, origin, destination, e):
        self._origin = origin
        self._destination = destination
        self._element = e

    def endpoints(self):
        return (self._origin, self._destination)

    def element(self):
        return self._element

    def opposite(self, v):
        return self._destination if v is self._origin else self._destination


class Graph:
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def add_vertex(self, e):
        v = Vertex(e)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def add_edge(self, u, v, e):
        edge = Edge(u, v, e)
        self._outgoing[u][v] = edge
        self._incoming[v][u] = edge

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for edge_dict in self._outgoing.values():
            result.update(edge_dict.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u][v]

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return adj[v].values()

    def DFS(self, u, discovered):
        for e in self.incident_edges(u):
            v = e.opposite(u)
            if v not in discovered:
                discovered[v] = e
                self.DFS(v, discovered)

    def construct_path(self, u, v, discovered):
        path = []
        if v in discovered:
            path.append(v)
            walk = v
            while walk is not u:
                e = discovered[walk]
                parent = e.opposite(walk)
                path.append(parent)
                walk = parent
            path.reverse()
        return path

    def BFS(self, u, discovered):
        vq = Queue()
        vq.enqueue(u)
        while not vq._is_empty():
            v = vq.dequeue()
            for e in self.incident_edges(v)
                o = e.opposite(v)
                if o not in discovered:
                    discovered[o] = e
                    vq.enqueue(o)
