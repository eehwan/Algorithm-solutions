import sys
sys.setrecursionlimit(10000)

class Node():
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
        self.left = None
        self.right = None

    def __str__(self):
        return f'node {self.idx}'

def insert(parent:Node, child:Node):
    if child.x < parent.x:
        if parent.left is None:
            parent.left = child
        else:
            insert(parent.left, child)
    else:
        if parent.right is None:
            parent.right = child
        else:
            insert(parent.right, child)


def solution(nodeinfo):
    nodes = sorted([Node(x[0], x[1], idx + 1) for idx, x in enumerate(nodeinfo)], key=lambda node: (-node.y, node.x))

    start_node = nodes[0]
    for i, node in enumerate(nodes[1:]):
        insert(start_node, node)
    
    def preorder(node: Node, LIST):
        LIST.append(node)
        if node.left:
            preorder(node.left, LIST)
        if node.right:
            preorder(node.right, LIST)

    def postorder(node: Node, LIST):
        if node.left:
            postorder(node.left, LIST)
        if node.right:
            postorder(node.right, LIST)
        LIST.append(node)
    

    list1, list2= [], []
    preorder(start_node, list1) 
    postorder(start_node, list2)

    return [[node.idx for node in _list] for _list in [list1, list2]]


if __name__ == "__main__":
    test_cases = [
        [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]], # [[7, 4, 6, 9, 1, 8, 5, 2, 3], [9, 6, 5, 8, 1, 4, 3, 2, 7]]
    ]
    print(*map(solution, test_cases), sep="\n")