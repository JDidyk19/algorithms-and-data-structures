from __future__ import annotations


def pre_order(tree: Node):
    if not tree:
        return
    print(tree.value)
    pre_order(tree.left)
    pre_order(tree.right)


def in_order(tree: Node):
    if not tree:
        return
    in_order(tree.left)
    print(tree.value)
    in_order(tree.right)


def post_order(tree: Node):
    if not tree:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.value)


def pre_order_iterative(tree: Node):
    stack = [tree]

    while stack:
        node = stack.pop()
        if node:
            print(node.value)
            stack.append(node.right)
            stack.append(node.left)
