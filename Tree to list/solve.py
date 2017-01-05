class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes


def tree_to_list(node):
    result = [node.data]

    if node.child_nodes is not None:
        result += [c.data for c in node.child_nodes]
        for child in node.child_nodes:
            if child.child_nodes is not None:
                for c in child.child_nodes:
                    result += tree_to_list(c)

    return result
