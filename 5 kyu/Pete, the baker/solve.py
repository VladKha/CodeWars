def cakes(recipe, available):
    return min(available.get(k, 0) // recipe[k] for k in recipe)
