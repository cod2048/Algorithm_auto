import sys
sys.setrecursionlimit(10001)

class Node:
    def __init__(self, data, x):
        self.data = data
        self.x = x
        self.left = None
        self.right = None

def insert(node, newNode):
    if newNode.x < node.x:
        if node.left is None:
            node.left = newNode
        else:
            insert(node.left, newNode)
    else:
        if node.right is None:
            node.right = newNode
        else:
            insert(node.right, newNode)

def preorder(node, arr):
    if node is not None:
        arr.append(node.data)
        preorder(node.left, arr)
        preorder(node.right, arr)

def postorder(node, arr):
    if node is not None:
        postorder(node.left, arr)
        postorder(node.right, arr)
        arr.append(node.data)

def solution(nodeinfo):
    nodes = sorted([(val[1], idx+1, val[0]) for idx, val in enumerate(nodeinfo)], reverse=True)
    root = Node(nodes[0][1], nodes[0][2])

    for node in nodes[1:]:
        insert(root, Node(node[1], node[2]))

    preorder_result = []
    postorder_result = []
    preorder(root, preorder_result)
    postorder(root, postorder_result)

    return [preorder_result, postorder_result]

# 예시 입력
nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))
