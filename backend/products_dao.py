from sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.products_id, products.products_name, products.uom_id, products.price_per_unit, uom_table.uom_name from products inner join uom_table on products.uom_id=uom_table.uom_id")

    cursor.execute(query)
    response = []

    for (products_id, products_name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'products_id': products_id,
            'products_name': products_name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    return response


def insert_new_products(connection, products):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(products_name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (products['products_name'], products['uom_id'],
            products['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, products_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(products_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    # print(get_all_products(connection))
    print(insert_new_products(connection, {
        'products_name': 'Moistured_Oil',
        'uom_id': '2',
        'price_per_unit': 70
    }))
