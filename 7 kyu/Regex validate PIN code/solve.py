def validate_pin(pin):
    return len(pin) in (4, 6) and pin.isdigit()
