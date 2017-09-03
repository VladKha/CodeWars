def fuelPrice(litres, pricePerLiter):
    discount = min(litres // 2 * 5, 25) * 0.01
    return round(litres * (pricePerLiter - discount), 2)
