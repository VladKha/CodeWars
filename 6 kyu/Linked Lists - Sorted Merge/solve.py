class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def sorted_merge(first, second):
    if not first:
        return second
    if not second:
        return first
    result = Node()
    head = result
    while result:
        if first and second:
            if first.data < second.data:
                result.data, first = first.data, first.next
            else:
                result.data, second = second.data, second.next
        elif first:
            result.data, first = first.data, first.next
        else:
            result.data, second = second.data, second.next

        if first or second:
            result.next = Node()
        result = result.next
    return head
