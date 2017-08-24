class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Context:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source, dest):
    if source is None:
        raise ValueError
    return Context(source.next, Node(source.data, dest))
