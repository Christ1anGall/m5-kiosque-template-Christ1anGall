from menu import products

def get_product_by_id(id:int):


    if type(id) != int:
        raise TypeError('id must be an integer')
         

    for elem in products:
        if elem['_id'] == id:
            return elem
    return {}


def get_products_by_type(type:str):


        if type(type) != str:
            raise TypeError('product type must be a str')


        list = []


        for elem in products:
            if elem['type'] == type:
                list.append(elem)


        return list


def menu_report() -> str:

        price = 0
        for elem in products:
            price += elem['price']
        

        common_name = ""
        common_number = 0

        for elem_out in products:
            count = 0

            for elem_in in products:
                if elem_out['type'] == elem_in['type']:
                    count += 1
                
            if (count > common_number):
                common_name = elem_out['type']
                common_number = count        



        return f"Products Count: {len(products)} - Average Price: ${price / len(products):.2f} - Most Common Type: {common_name}"


def add_product(menu, **new_product):
        last_id = 0
        for id in menu:
            if(id["_id"] > last_id):
                last_id = id["_id"]
        menu = [*menu , {**new_product, "_id": last_id + 1}]

        return {**new_product, "_id": last_id + 1}

