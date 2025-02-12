from restaurants import Restaurant
from orders import Orders
from reviews import Reviews


if __name__ == '__main__':
    # creating a restaurant and the menu
    restaurant = Restaurant('Pizzaria IC', 'Rua do IC - UFAL')
    restaurant.add_menu_item('Pepperoni Pizza', 35.0)
    restaurant.add_menu_item('Margherita Pizza', 20.0)
    restaurant.add_menu_item('Mussarela Pizza', 5.0)

    # creating an order and add more items:
    order = Orders(1, 'Joao', restaurant)
    order.add_item('Pepperoni Pizza', 10)
    order.add_item('Margherita Pizza', 9)

    # showing initial order:
    print('##########################################')
    print('Initial order:')
    order.show_order()
    print('##########################################')

    # updating order and item_price:
    restaurant.update_item_price('Pepperoi Pizza', 30)
    order.update_amount('Pepperoni Pizza', 5)
    order.remove_item('Margherita Pizza')
    order.add_item('Mussarela Pizza', 5)

    # showing updated order:
    print('Updated order:')
    order.show_order()
    print('##########################################')

    # updating order status:
    print('Updated status')
    order.update_status('Out of Delivery')
    order.show_order()
    print('##########################################')

    # creating a review:
    review1 = Reviews('Joao', restaurant, 5, 'The greatest pizza in the world!')
    review2 = Reviews('Pedro', restaurant, 4, 'Good pizza!')

    # add reviews to restaurant reviews list:
    restaurant.add_review(review1)
    restaurant.add_review(review2)

    # showing reviews:
    print('Restaurant reviews:')
    restaurant.display_reviews()






