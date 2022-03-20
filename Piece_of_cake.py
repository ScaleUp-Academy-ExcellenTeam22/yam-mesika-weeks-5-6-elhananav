def get_recipe_price(prices, optionals=[], **ingredients):
    '''
    this function calculate the total price that the recipe costs
    :param prices: products dictionary of wanted recipe, key is the name of the product and the
                   value is the price for 100 grams
    :param optionals: list of products to be ignored
    :param ingredients: wanted amount of each product
    :return: the total price of the recipe
    '''
    total_price = 0
    for product, price in prices.items():
        if product not in optionals:
            total_price += price * ingredients.get(product)//100
    return total_price





