def solution(items, index, default_value):
    return items[index] if -len(items) <= index < len(items) else default_value
