def list_to_array(lst):
    result = []

    cur = lst
    while cur:
        result.append(cur.value)
        cur = cur.next

    return result
