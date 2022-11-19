if __name__ == "__main__":
    from management import add_product
    from menu import products

    new_product = {
            "title": "Bolinho JS",
            "price": 1.0,
            "rating": 2,
            "description": "Bolinho de JS com cenoura",
            "type": "bakery",
        }

    print(add_product(products, **new_product))