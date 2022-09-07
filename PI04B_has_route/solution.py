class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []  # List of Nodes this node points to

def has_route(start_node: GraphNode, end_node: GraphNode) -> bool:
    visited = set()
    def dfs(visited: set, node: GraphNode):
        if node not in visited:
            visited.add(node)
            for next in node.adjacent:
                dfs(visited, next)

    dfs(visited=visited, node=start_node)
    if end_node in visited:
        return True
    return False

if __name__ == "__main__":
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node5 = GraphNode(5)
    node6 = GraphNode(6)
    node7 = GraphNode(7)
    node8 = GraphNode(8)
    node9 = GraphNode(9)


    node1.adjacent.extend([node2, node8])
    node2.adjacent.extend([node1, node8, node9])
    node3.adjacent.extend([node4, node7])
    node4.adjacent.extend([node3, node5, node6, node7])
    node5.adjacent.extend([node4])
    node6.adjacent.extend([node4])
    node7.adjacent.extend([node3, node4])
    node8.adjacent.extend([node1, node2])
    node9.adjacent.extend([node2])
    
    r = has_route(start_node=node8, end_node=node6)
    print(r)