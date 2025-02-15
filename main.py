from delivery import DeliveryOptions, DeliveryTracking
from orders import Orders, OrderHistory
from promotions import Promotion
from restaurants import Restaurant, RestaurantAnalytics
from reviews import Reviews
from support import Support


from restaurants import Restaurant, RestaurantAnalytics
from orders import Orders, OrderHistory
from payments import Payment
from promotions import Promotion
from reviews import Reviews
from support import Support
from delivery import DeliveryTracking, DeliveryOptions

def main():
    # System Initialization
    restaurant = Restaurant("Pizzeria IC", "IC Street - UFAL")
    restaurant.add_menu_item("Pepperoni Pizza", 35.0)
    restaurant.add_menu_item("Margherita Pizza", 20.0)
    restaurant.add_menu_item("Mozzarella Pizza", 5.0)

    order_history = OrderHistory()
    support = Support()
    analytics = RestaurantAnalytics()

    while True:
        print("\n=== Food Delivery System ===")
        print("1. Manage Restaurant")
        print("2. Place an Order")
        print("3. View Order History and Reorder")
        print("4. Process Payment")
        print("5. Add Review")
        print("6. Manage Promotions")
        print("7. Track Delivery")
        print("8. Customer Support")
        print("9. View Restaurant Analytics")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Manage Restaurant
            print("\n=== Manage Restaurant ===")
            print("1. Add Menu Item")
            print("2. Remove Menu Item")
            print("3. Update Item Price")
            print("4. View Menu")
            sub_choice = input("Choose an option: ")

            if sub_choice == "1":
                item = input("Item name: ")
                price = float(input("Item price: "))
                restaurant.add_menu_item(item, price)
                print(f"Item '{item}' added to the menu.")
            elif sub_choice == "2":
                item = input("Name of the item to be removed: ")
                restaurant.remove_menu_item(item)
                print(f"Item '{item}' removed from the menu.")
            elif sub_choice == "3":
                item = input("Item name: ")
                new_price = float(input("New price: "))
                restaurant.update_item_price(item, new_price)
                print(f"Price of item '{item}' updated.")
            elif sub_choice == "4":
                print("\nRestaurant Menu:")
                for item, price in restaurant.menu.items():
                    print(f"- {item}: ${price:.2f}")
            else:
                print("Invalid option.")

        elif choice == "2":
            # Place an Order
            print("\n=== Place an Order ===")
            customer = input("Customer name: ")
            order = Orders(len(order_history.get_order_list()) + 1, customer, restaurant)

            while True:
                print("\nMenu Items:")
                for item, price in restaurant.menu.items():
                    print(f"- {item}: ${price:.2f}")
                item = input("Enter item name (or 'exit' to finish): ")
                if item.lower() == "exit":
                    break
                amount = int(input("Quantity: "))
                order.add_item(item, amount)

            order_history.add_order(order)
            print("\nOrder successfully created!")
            order.show_order()

        elif choice == "3":
            # View Order History and Reorder
            print("\n=== Order History ===")
            for past_order in order_history.get_order_list():
                past_order.show_order()
                print("-----------------------------")

            reorder_id = input("Enter the order ID to reorder (or 'exit' to go back): ")
            if reorder_id.lower() != "exit":
                reordered_order = order_history.reorder(int(reorder_id), "Reordered Customer", restaurant)
                if reordered_order:
                    print("\nReordered order:")
                    reordered_order.show_order()

        elif choice == "4":
            # Process Payment
            print("\n=== Process Payment ===")
            order_id = int(input("Order ID: "))
            order = None
            for o in order_history.get_order_list():
                if o.order_id == order_id:
                    order = o
                    break
            if order:
                print("Payment methods: credit_card, debit_card, pix, money")
                payment_method = input("Payment method: ")
                payment_details = {}
                if payment_method in ["credit_card", "debit_card"]:
                    payment_details["card_number"] = input("Card number: ")
                    payment_details["expiry_date"] = input("Expiry date (MM/YY): ")
                    payment_details["cvv"] = input("CVV: ")
                order.process_payment(payment_method, payment_details)
            else:
                print("Order not found.")

        elif choice == "5":
            # Add Review
            print("\n=== Add Review ===")
            customer = input("Customer name: ")
            rating = int(input("Rating (1-5): "))
            comment = input("Comment: ")
            review = Reviews(customer, restaurant, rating, comment)
            restaurant.add_review(review)
            print("Review successfully added!")

        elif choice == "6":
            # Manage Promotions
            print("\n=== Manage Promotions ===")
            print("1. Create Promotion")
            print("2. Apply Discount")
            sub_choice = input("Choose an option: ")

            if sub_choice == "1":
                code = input("Promotion code: ")
                discount = float(input("Discount (%): "))
                promotion = Promotion()
                promotion.create_promotion(code, discount)
                print(f"Promotion '{code}' successfully created.")
            elif sub_choice == "2":
                code = input("Promotion code: ")
                total_price = float(input("Total order price: "))
                promotion = Promotion()
                discounted_price = promotion.apply_discount(code, total_price)
                print(f"Discounted price: ${discounted_price:.2f}")
            else:
                print("Invalid option.")

        elif choice == "7":
            # Track Delivery
            print("\n=== Track Delivery ===")
            order_id = int(input("Order ID: "))
            order = None
            for o in order_history.get_order_list():
                if o.order_id == order_id:
                    order = o
                    break
            if order:
                delivery_tracking = DeliveryTracking(order)
                new_status = input("New delivery status: ")
                delivery_tracking.update_status(new_status)
                print(f"Delivery status updated to: {new_status}")
            else:
                print("Order not found.")

        elif choice == "8":
            # Customer Support
            print("\n=== Customer Support ===")
            print("1. Create Ticket")
            print("2. Close Ticket")
            sub_choice = input("Choose an option: ")

            if sub_choice == "1":
                customer = input("Customer name: ")
                issue = input("Problem: ")
                comment = input("Comment: ")
                support.create_ticket(customer, issue, comment)
                print("Ticket successfully created.")
            elif sub_choice == "2":
                customer = input("Customer name: ")
                support.close_ticket(customer)
            else:
                print("Invalid option.")

        elif choice == "9":
            # View Restaurant Analytics
            print("\n=== Restaurant Analytics ===")
            analytics.record_order(restaurant, 135.0)
            print(f"Analytics for {restaurant.name}: {analytics.get_analytics(restaurant)}")

        elif choice == "0":
            print("Exiting the system...")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
