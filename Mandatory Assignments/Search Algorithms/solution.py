# Do not modify the classes below
class TreeNode:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, representation: str):
        '''
        representation: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        if not representation:
            return
        nodes = []
        for i, value in enumerate(representation):
            node = None
            if value is not None:
                node = TreeNode(value)
                if i > 0:
                    if i % 2 == 1:
                        parent = nodes[(i - 1) // 2]
                        parent.left = node
                    else:
                        parent = nodes[(i - 2) // 2]
                        parent.right = node
            nodes.append(node)
        self.root = nodes[0]


class GraphNode:
    def __init__(self, value=None):
        self.value = value
        self.adjacent = []


class Graph:
    def __init__(self, adjacency: list[list[bool]]):
        '''
        adjacency: list of values representing a binary tree. The left and right
        children of the ith element are 2i+1 and 2i+2, respectively.
        '''
        self.nodes = [GraphNode(i) for i in range(1, len(adjacency) + 1)]
        for node1, row in zip(self.nodes, adjacency):
            for node2, adjacent in zip(self.nodes, row):
                if adjacent and node1 is not node2:
                    node1.adjacent.append(node2)


# Implement the functions below
'''
pre_order -> root, left, right

in_order -> left, root, right

post_order -> left, right, root



breadth_first -> colocar root na queue, colocar todos os filhos na queue da esquerda para direita (?)

depth_first ->

'''

def pre_order_recursive(root: TreeNode) -> None:
    if root:
        print(root.value)
        pre_order_recursive(root.left)
        pre_order_recursive(root.right)


def pre_order_iterative(root: TreeNode) -> None:
    stack = []
    stack.append(root)
    while len(stack) > 0:
        current = stack.pop()
        print(current.value)

        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)


def in_order_recursive(root: TreeNode) -> None:
    if root.left:
        in_order_recursive(root.left)
    print(root.value)
    if root.right:
        in_order_recursive(root.right)


def post_order_recursive(root: TreeNode) -> None:
    if root.left:
        post_order_recursive(root.left)
    if root.right:
        post_order_recursive(root.right)
    print(root.value)


def breadth_first(root: TreeNode) -> None:
    queue = []
    queue.append(root)
    while len(queue) > 0:
        current = queue.pop()
        print(current.value)

        if current.left:
            queue.insert(0, current.left)
        if current.right:
            queue.insert(0, current.right)


def graph_depth_first_recursive(node: GraphNode, visited=None) -> None:
    if visited is None:
        visited = set()
    if node not in visited:
        visited.add(node)
        print(node.value)
        for next in node.adjacent:
            graph_depth_first_recursive(node=next, visited=visited)


def graph_depth_first_iterative(node: GraphNode) -> None:
    pass


def graph_breadth_first(node: GraphNode) -> None:
    queue = [node]
    visited = set(queue)
    while len(queue) > 0:
        current = queue.pop()
        print(current.value)

        for next in current.adjacent:
            if next not in visited:
                queue.insert(0, next)
                visited.add(next)
 
if __name__ == "__main__":

    def build_perfect_tree():
        return Tree(list(range(15)))

    pre_order_recursive(build_perfect_tree())