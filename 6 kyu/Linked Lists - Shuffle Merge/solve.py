class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def shuffle_merge(a, b):
    if a:
        result = Node(a.data)
        current_a = a.next
        current_b = b
    elif b:
        result = Node(b.data)
        current_a = a
        current_b = b.next
    else:
        return None

    current = result
    while current_a or current_b:
        if current_b:
            current.next = current_b
            current_b = current_b.next
            current = current.next

        if current_a:
            current.next = current_a
            current_a = current_a.next
            current = current.next

    return result
