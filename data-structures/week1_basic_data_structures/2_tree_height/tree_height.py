# python3

import sys
import threading
import queue


class Node:
    def __init__(self, id):
        self.children = []
        self.id = id

    def add_child(self, child):
        self.children.append(child)

    def get_children(self):
        return self.children

    def __str__(self):
        return str(self.id)

    def __repr__(self):
        children = 'node ' + str(self.id) + ' has children:'
        for child in self.children:
            children += ' ' + str(child)
        return children


def build_trees(n_nodes, parents):
    nodes = []
    for id in range(n_nodes):
        node = Node(id)
        nodes.append(node)

    for child_idx in range(len(parents)):
        parent_idx = parents[child_idx]
        if parent_idx == -1:
            root = child_idx
        else:
            nodes[parent_idx].add_child(nodes[child_idx])

    return root, nodes


def compute_height(root, tree):
    height = 0
    q = queue.Queue(maxsize=len(tree))
    q.put(tree[root])
    # use None as a marker to indicate the current level
    # has been traversed
    q.put(None)

    while not q.empty():
        cur_node = q.get()
        if cur_node is None:
            if not q.empty():
                q.put(None)
            height += 1
        else:
            children = cur_node.get_children()
            for child in children:
                q.put(child)

    return height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    root, tree = build_trees(n, parents)
    print(compute_height(root, tree))


if __name__ == "__main__":
    main()
