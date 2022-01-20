from __future__ import annotations


def level_order(tree: Node):
    queue = [tree]
    while queue:
        node = queue.pop(0)
        if node:
            print(node.value)
            queue.append(node.left)
            queue.append(node.right)
