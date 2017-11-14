def excluding_vat_price(price):
    if not price:
        return -1
    return round(price * 20 / 23, 2)
