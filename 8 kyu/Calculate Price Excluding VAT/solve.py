def excluding_vat_price(price):
    if not price:
        return -1
    return round(price * 100 / 115, 2)
