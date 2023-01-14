from datetime import datetime
from sql_connection import get_sql_connection


def insert_orders(connection, orders):

    cursor = connection.cursor()
    orders_query = ("INSERT INTO orders"
                    "(customer_name, total, datetime)"
                    "VALUES (%s, %s, %s)")

    orders_data = (orders['customer_name'],
                   orders['total'], datetime.now())

    cursor.execute(orders_query, orders_data)
    orders_id = cursor.lastrowid
    connection.commit()

    return orders_id


if __name__ == '__main__':
    connection = get_sql_connection()

    print(insert_orders(connection, {
        'customer_name': 'ironman',
        'total': '500',
        'datetime': datetime.now(),
        'orders_details': [
            {
                'product_id': 1,
                'quantity': 2,
                'total_price': 50
            },
            {
                'product_id': 3,
                'quantity': 1,
                'total_price': 30
            }
        ]
    }))
