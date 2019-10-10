#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # check how many can be made from each ingredient
    # get lowest amount from all possibilities
    # also check if recipe key exists in ingredients.keys()

    # better solution: eliminate ingredients for loop?

    # possible_batches = []
    # for rk, rv in recipe.items():
    #     for ik, iv in ingredients.items():
    #         if rk == ik:
    #             # amount = iv // rv
    #             # print(amount)
    #             possible_batches.append(iv // rv)
    #     if rk not in ingredients.keys():
    #         return 0

    # return min(possible_batches)

    if len(recipe) > len(ingredients):
        return 0
    # 2nd solution
    possible_batches = []
    for key in recipe:
        if ingredients[key] >= recipe[key]:
            possible_batch = ingredients[key] // recipe[key]
            possible_batches.append(possible_batch)

    return min(possible_batches)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
