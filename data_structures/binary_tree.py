class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# DFS
def pre_order(tree: TreeNode):
    if not tree:
        return
    print(tree.value, end=' ')
    pre_order(tree.left)
    pre_order(tree.right)


def in_order(tree: TreeNode):
    if not tree:
        return
    in_order(tree.left)
    print(tree.value, end=' ')
    in_order(tree.right)


def post_order(tree: TreeNode):
    if not tree:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.value, end=' ')


def pre_order_iterative(tree: TreeNode):
    stack = [tree]

    while stack:
        node = stack.pop()
        if node:
            print(node.value, end=' ')
            stack.append(node.right)
            stack.append(node.left)


# BFS
def level_order(tree: TreeNode):
    queue = [tree]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.value, end=' ')
            queue.append(node.left)
            queue.append(node.right)
