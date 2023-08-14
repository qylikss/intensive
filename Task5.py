class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right


root = Node(8, Node(5, Node(3), Node(6)), Node(10, Node(9), Node(11)))
print(root)

def bfs(root):

    print(root.key)
