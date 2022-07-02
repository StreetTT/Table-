"""
{"user1": ["user2"],
"user2": ["user3"],
"user3": ["user1","user2"]}
"""
"""
User 1 follows User 2
User 2 follows User 3
User 3 follows User 1 and User 2
"""


class DirGraph:
    def __init__(self):
        self.adjacency_list = {}
        self.nodes = 0
        self.connections = 0

    def displayGraph(self):
        for i in self.adjacency_list:
            print(end=i + " follows ")
            following = ""
            for j in self.adjacency_list[i]:
                following = following + j + ", "
            print(following[:-2])

    def search(self, node):  # Search if node is in the adjacency_list
        node = str(node).title()
        x = self.adjacency_list.get(node)
        if x is None:
            return False
        else:
            return True

    def addNode(self, node):  # Adds a node to tree
        node = str(node).title()
        if self.search(node):
            return False  # Node already exists
        else:
            self.nodes = self.nodes + 1
            self.adjacency_list.update({node: []})

    def addConnection(self, node, connected_node):  # Connects node to connected_nodes (n -> cn)
        node = str(node).title()
        connected_node = str(connected_node).title()
        if self.search(node) is False:
            self.addNode(node)
        if self.search(connected_node) is False:
            self.addNode(connected_node)
        self.adjacency_list[node].append(connected_node)
        self.connections = self.connections + 1


class User:
    def __int__(self):
        self.Name = ""
        self.UserID = 0


def Test():
    follower_graph = DirGraph()
    follower_graph.addNode("Carla")
    follower_graph.addNode("Jay")
    follower_graph.addConnection("Carla", "Jay")
    follower_graph.addConnection("Jay", "David")
    follower_graph.addConnection("David", "Carla")
    follower_graph.addConnection("David", "Jay")
    follower_graph.displayGraph()


Test()
