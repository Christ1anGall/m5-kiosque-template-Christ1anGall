
from .product_handler import get_product_by_id

def calculate_tab(comanda):
        subtotal = 0

        produtos = []

        for item in comanda:
            produtos.append(get_product_by_id(item["_id"])["price"] * item["amount"] )

        print(produtos)

        for item in produtos:
            subtotal += item



        return {'subtotal': f'${round(subtotal,2)}'}
