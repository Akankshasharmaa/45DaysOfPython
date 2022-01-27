from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """
    :param dish_name: str
    :param dish_ingredients: list
    :return: tuple of (dish_name, ingredient set)

    This function should return a `tuple` with the name of the dish as the first item,
    followed by the de-duped `set` of ingredients as the second item.
    """
    ingredient_set = set(dish_ingredients)
    mydish = (dish_name, ingredient_set)
    return mydish

def check_drinks(drink_name, drink_ingredients):
    """
    :param drink_name: str
    :param drink_ingredients: list
    :return: str drink name + ("Mocktail" or "Cocktail")

    The function should return the name of the drink followed by "Mocktail" if the drink has
    no alcoholic ingredients, and drink name followed by "Cocktail" if the drink includes alcohol.
    """
    drink_set = set(drink_ingredients)
    if ALCOHOLS.isdisjoint(drink_set):
        return drink_name + " Mocktail"
    return drink_name + " Cocktail"

def categorize_dish(dish_name, dish_ingredients):
    """
    :param dish_name: str
    :param dish_ingredients: list
    :return: str "dish name: CATEGORY"

    This function should return a string with the `dish name: <CATEGORY>` (which meal category the dish belongs to).
    All dishes will "fit" into one of the categories imported from `sets_categories_data.py`
    (VEGAN, VEGETARIAN, PALEO, KETO, or OMNIVORE).
    """
    dish_set = set(dish_ingredients)
    category = " "
    if dish_set.issubset(VEGAN):
        category = "VEGAN"
    elif dish_set.issubset(VEGETARIAN):
        category = "VEGETARIAN"
    elif dish_set.issubset(PALEO):
        category = "PALEO"
    elif dish_set.issubset(KETO):
        category = "KETO"
    elif dish_set.issubset(OMNIVORE):
        category = "OMNIVORE"
    else:
        category = " "
    return dish_name + ": " + category

def tag_special_ingredients(dish):
    """
    :param dish: tuple of (str of dish name, list of dish ingredients)
    :return: tuple of (str of dish name, set of dish special ingredients)

    Return the dish name followed by the `set` of ingredients that require a special note on the dish description.
    For the purposes of this exercise, all allergens or special ingredients that need to be tracked are in the
    SPECIAL_INGREDIENTS constant imported from `sets_categories_data.py`.
    """
    ingredient_set = set(dish[1])
    if ingredient_set.isdisjoint(SPECIAL_INGREDIENTS):
        return dish[0]
    ingredients = ingredient_set.intersection(SPECIAL_INGREDIENTS)
    return (dish[0], ingredients)

def compile_ingredients(dishes):
    """
    :param dishes: list of dish ingredient sets
    :return: set

    This function should return a `set` of all ingredients from all listed dishes.
    """
    new_set = set()
    for myset in dishes:
        new_set = new_set.union(myset)
    return set(new_set)

def separate_appetizers(dishes, appetizers):
    """
    :param dishes: list of dish names
    :param appetizers: list of appetizer names
    :return: list of dish names

    The function should return the list of dish names with appetizer names removed.
    Either list could contain duplicates and may require de-duping.
    """
    dish_set = set(dishes)
    appetizer_set = set(appetizers)
    remaining_dish = dish_set - appetizer_set
    return remaining_dish

def singleton_ingredients(dishes, intersection):
    """
    :param intersection: constant - one of (
        VEGAN_INTERSECTION,
        VEGETARIAN_INTERSECTION,
        PALEO_INTERSECTION,
        KETO_INTERSECTION,
        OMNIVORE_INTERSECTION
    )
    :param dishes:  list of ingredient sets
    :return: set of singleton ingredients

    Each dish is represented by a `set` of its ingredients.
    Each `<CATEGORY>_INTERSECTION` is an `intersection` of all dishes in the category.
    The function should return a `set` of ingredients that only appear in a single dish.
    """
    all_ingredients = set()
    for dish in dishes:
        all_ingredients = all_ingredients.union(dish)
    common_ingredients = dishes[0]
    for dish in dishes:
        common_ingredients = common_ingredients.intersection(dish)
    unique = all_ingredients - common_ingredients
    return unique - intersection
