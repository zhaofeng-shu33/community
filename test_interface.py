import networkx as nx
import unittest
from GN import GN

class TestGN(unittest.TestCase):
    def test_6point(self):
        G=nx.Graph()
        G.add_edge(0, 2)
        G.add_edge(0, 1)
        G.add_edge(2, 1)
        G.add_edge(3, 4)
        G.add_edge(3, 5)
        G.add_edge(4, 5)
        G.add_edge(0, 5) 
        gn = GN()
        gn.fit(G)
        self.assertEqual(gn.Bestcomps, [{0, 1, 2}, {3, 4, 5}])
        print(gn.tree)

if __name__ == '__main__':
    unittest.main()
