from functions import *

if __name__=="__main__":
    while True:
            print("Are You a User Or Manager")
            print("1. Manager")
            print("2.User")
            choice = input("Enter your choice (1-2): ")

            if choice == '1':
                while True:
                     manager_menu()
                     choice = input("Enter your choice (1-4): ")
                     if choice == '1':
                         remove_product_by_id()
                     elif choice == '2':
                        remove_product_by_name()
                     elif choice == '3':
                        update_price_by_id()
                     elif choice == '4':
                        update_price_by_name()
                     elif choice == '5':
                          update_quantity_by_id()
                     elif choice == '6':
                        update_quantity_by_name()
                     elif choice == '7':
                        add_product()
                     elif choice == '8':
                        display_all_products()
                     elif choice == '9':
                         break
                     else:
                         print("Error. Please enter a number between 1 and 9.")
                            
            elif choice == '2':
                    while True:
                        display_menu()
                        choice = input("Enter your choice (1-4): ")

                        if choice == '1':
                            browse_products()
                        elif choice == '2':
                            cart = buy_products()
                            if cart:
                                view_cart(cart)
                        elif choice == '3':
                            view_cart(cart)
                        elif choice == '4':
                            print("Exiting")
                            break
                        else:
                            print("Error. Please enter a number between 1 and 4.")
                    