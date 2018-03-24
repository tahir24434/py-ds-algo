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

    def is_connected(self):
        if not self.is_directed():
            return self._is_connected_undirected()

    def _is_connected_undirected(self):
        """
        We can use the basic DFS function to determine whether a graph is
        connected. In the case of undirected graph, we simply start a depth-first
        search at an arbitrary vertex and then test whether len(discovered) equals n
        at the conclusion.
        :return: bool
            True if graph is connected. False otherwise
        """
        # Pick any random vertex
        v = list(self._outgoing.keys())[0]
        discovered = {v: None}
        self.DFS(v, discovered)
        if len(discovered) == len(self.vertices()):
            return True
        else:
            return False

    def BFS(self, s, discovered):
        level = [s]
        while len(level) > 0:
            next_level = []
            for u in level:
                edges = self.incident_edges(u)
                for e in edges:
                    v = e.opposite(u)
                    if v not in discovered:
                        discovered[v] = e
                        next_level.append(v)
            level = next_level

    def BFS_alt(self, u, discovered):
        vq = Queue()
        vq.enqueue(u)
        while not vq._is_empty():
            v = vq.dequeue()
            for e in self.incident_edges(v):
                o = e.opposite(v)
                if o not in discovered:
                    discovered[o] = e
                    vq.enqueue(o)

    def topological_sort(self):
        # Calculate indegree of all vertices. For topological sort, G must be
        # acyclic and thus it must have a vertex with no incoming edge.
        topo = []
        ready = []
        incount = dict()

        for v in self.vertices():
            incount[v] = self.degree(v, outgoing=False)
            if incount[v] == 0:
                ready.append(v)

        while len(ready) > 0:
            v = ready.pop()
            topo.append(v)
            for e in self.incident_edges(v):
                ov = e.opposite(v)
                incount[ov] -= 1
                if incount[ov] <= 0:
                    ready.append(ov)
        return topo

    def is_cyclic(self):
        topo = self.topological_sort()
        print(topo)
        if len(topo) < len(self.vertices()):
            return True
        return False


if __name__ == "__main__":
    g = Graph()
    es = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    vertices = []
    for e in es:
        vertices.append(g.add_vertex(e))
    g.add_edge(vertices[0], vertices[1], 'ab')
    g.add_edge(vertices[0], vertices[4], 'ae')
    g.add_edge(vertices[0], vertices[5], 'af')
    g.add_edge(vertices[1], vertices[2], 'bc')
    g.add_edge(vertices[1], vertices[5], 'bf')
    g.add_edge(vertices[2], vertices[3], 'cd')
    g.add_edge(vertices[2], vertices[6], 'cg')
    g.add_edge(vertices[3], vertices[6], 'dg')
    g.add_edge(vertices[3], vertices[7], 'dh')
    discovered = {vertices[0]: None}
    g.DFS(vertices[0], discovered)
    for v in discovered.keys():
        print(v.element())
    print("********")
    print(g.is_connected())
    print("********")
    print(g.is_cyclic())
    print("================ Directed Graph =================")
    g = Graph(directed=True)
    es = ['BOS', 'JFK', 'DFW', 'LAX', 'ORD', 'MIA', 'SFO']
    vertices = []
    for e in es:
        vertices.append(g.add_vertex(e))
    g.add_edge(vertices[0], vertices[1], 'BOS->JFK')
    g.add_edge(vertices[1], vertices[2], 'JFK->DFW')
    g.add_edge(vertices[2], vertices[4], 'DFW->ORD')
    g.add_edge(vertices[4], vertices[3], 'ORD->LAX')
    g.add_edge(vertices[3], vertices[5], 'LAX->MIA')
    g.add_edge(vertices[5], vertices[6], 'MIA->SFO')
    #g.add_edge(vertices[6], vertices[0], 'SFO->BOS')
    print(g.is_cyclic())
    print("================ BFS (Shortest Path) =================")
    g = Graph()
    es = ['Mini', 'William', 'Jayd', 'Omar', 'Noah', 'Amelia', 'Ren', 'Adam']
    vertices = []
    for e in es:
        vertices.append(g.add_vertex(e))
    g.add_edge(vertices[0], vertices[1], 'Mini->William')
    g.add_edge(vertices[0], vertices[2], 'Mini->Jayd')
    g.add_edge(vertices[0], vertices[3], 'Mini->Omar')
    g.add_edge(vertices[1], vertices[2], 'Willaim->Noah')
    g.add_edge(vertices[2], vertices[4], 'Jayd->Noah')
    g.add_edge(vertices[4], vertices[5], 'Jayd->Amelia')
    g.add_edge(vertices[5], vertices[7], 'Amelia->adam')
    discovered = {vertices[2]: None}
    g.BFS(vertices[2], discovered)
    for k,v in discovered.items():
        print(k.element(), v)
