"""Calculate the cost of the ingredients in a recipe."""

GRAMS_PER_PRICE_UNIT = 100


def piece_of_cake(prices, optionals=None, **quantities):
    """Return the cost given prices per 100 grams and quantities in grams."""
    excluded = set() if optionals is None else set(optionals)
    return sum(
        price * quantities[ingredient] / GRAMS_PER_PRICE_UNIT
        for ingredient, price in prices.items()
        if ingredient not in excluded
    )


get_recipe_price = piece_of_cake


if __name__ == "__main__":
    print(piece_of_cake({"chocolate": 18, "milk": 8}, chocolate=200, milk=100))
