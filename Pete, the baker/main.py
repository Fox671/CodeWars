def cakes(recipe, available):
    return min([available[key] // recipe[key] if key in available else 0 for key in recipe])

d1 = {"flour": 500, "sugar": 200}
d2 = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}