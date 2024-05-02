class Product:
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self) -> str:
         return f"{self.id}\t{self.name}\t\t{self.quantity}\t\t${self.price:.2f}"

products_list = [
    Product("1", "T-Shirt", 15.99, 50),
    Product("2", "Jeans", 29.99, 30),
    Product("3", "Skirt", 24.99, 25)
]

cart=[]

def remove_product_by_id():
    product = search_product_by_id()
    products_list.remove(product)


def remove_product_by_name():
    product = search_product_by_name()
    products_list.remove(product)
def update_price_by_id():
    product = search_product_by_id()
    product.price = int(input("Enter Price"))
def update_price_by_name():
    product = search_product_by_name()
    product.price = int(input("Enter Price"))

def add_product():
    id = input("Enter ID: ")
    name = input("Enter Name: ")
    price = input("Enter Price: ")
    quantity = input("Enter Quantity: ")

    try:
        price = int(price)
        if(price <= 0):
            raise
    except:
        print("Can't add this product, the price is incorrect")

    try:
        quantity = int(quantity)
        if(price <= 0):
            raise
    except:
        print("Can't add this product, the quantity is incorrect")

    p = Product(id,name,price,quantity)
    products_list.append(p)

def display_menu():
    print("Welcome to the Shopping App!")
    print("1. Browse Products")
    print("2. Place Order")
    print("3. View Cart")
    print("4. Exit")

def browsing_menu():
    print("1. Display All Products")
    print("2. Search Product by ID")
    print("3. Search Product by Name")   
    print("4. Back")

def display_all_products():
    print("Available Products:")
    print("ID\tName\t\tQuantity\tPrice")
    for product in products_list:
        print(f"{product.id}\t{product.name}\t\t{product.quantity}\t\t${product.price:.2f}")


def search_product_by_id():
    id = input("Enter the Product ID ")
    c = 0
    for product in products_list:
        if product.id == id:
            c = c + 1
            return product
        
    if c == 0:
        return "PLEASE ENTER A VALID ID."
        
def search_product_by_name():
    name = input("Enter the Product Name ")
    c = 0
    for product in products_list:
        if product.name == name:
            c = c + 1
            return product
        
    if c == 0:
        return "PRODUCT NOT FOUND. PLEASE TRY ANOTHER SEARCH"
    
def update_quantity_by_id():
    product = search_product_by_id()
    product.quantity = int(input("Enter Quantity"))
def update_quantity_by_name():
    product = search_product_by_name()
    product.quantity = int(input("Enter Quantity"))

def manager_menu():
    print("1. Remove Product by ID")
    print("2. Remove Product by Name")
    print("3. Update Price by ID") 
    print("4. Update Price by Name")  
    print("5. Update Quantity by ID") 
    print("6. Update Quantity by Name")
    print("7. Add New Product")
    print("8. Display All Products")
    print("9. Exit")

def browse_products():
    while True:
        browsing_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_all_products()
        elif choice == '2':
            b=search_product_by_id()
            print(b)
            if b == "PLEASE ENTER A VALID ID.":
                continue
        elif choice == '3':
            b=search_product_by_name()
            print(b)        
        elif choice == '4':
            print("Exiting")
            return
        else:
            print("Error. Please enter a number between 1 and 4.")

def display_all_products():
    print("Available Products:")
    print("ID\tName\t\tQuantity\tPrice")
    for product in products_list:
        print(product)


def buy_products():
    
    while True:
        display_all_products()
        choice = input("\nEnter the name or ID of the product you want to buy (or 'done' to finish shopping): ").strip().lower()
        if choice == 'done':
            break
        else:
            found = False
            for product in products_list:
                if choice == product.name or choice == str(product.id):
                    found = True
                    try:
                        quantity = int(input(f"How many {product.name} do you want to buy? "))
                    except:
                        print("Invalid Entry")
                        continue
                    if quantity <= 0 or quantity > product.quantity:
                        print("Invalid quantity. Please try again.")
                    else:
                        cart.append([product.id, product.name, quantity, product.price])
                        product.quantity -= quantity
                        print(f"{quantity} {product.name} added to your cart.")
                    break
            if not found:
                print("Product not found. Please try again.")

    return cart

def view_cart(cart):
    total_price = 0
    print("\nYour Cart:")
    print("ID\tName\t\tQuantity\tPrice")
    for item in cart:
        print(f"{item[0]}\t{item[1]}\t{item[2]}\t\t${item[3] * item[2]:.2f}")
        total_price += item[3] * item[2]
    print(f"\nTotal Price: ${total_price:.2f}")

    while True:
        print("\n1. Checkout.")
        print("2. Edit Cart.")
        print("3. Exit.")
        choice = input("\nEnter Your Choice: ")
        if choice == '1':
            print("Thank you for shopping with us!")
            break
        elif choice == '2':
            edit_cart(cart)
            view_cart(cart)

        elif choice == '3':
            print("exiting ...")
            break
        else:
            print("Invalid choice. Please try again.")

def edit_cart(cart):
    while True:
        print("\nEdit Options:")
        print("1. Remove item")
        print("2. Edit quantity")
        print("3. Add new item")
        print("4. Done")
        choice = input("Enter your choice: ").strip().lower()

        if choice == '1':  
            item_id = input("Enter the ID of the item you want to remove: ").strip().lower()
            for item in cart:
                if str(item[0]) == item_id:
                    for product in products_list:
                        if str(product.id) == item_id:
                            product.quantity += item[2]
                            break
                    cart.remove(item)
                    print("Item removed from your cart.")
                    break
            else:
                print("Item not found in your cart.")
        
        elif choice == '2':  
            item_id = input("Enter the ID of the item you want to edit: ").strip().lower()
            for item in cart:
                if str(item[0]) == item_id:
                    try:
                        new_quantity = int(input(f"Enter the new quantity for {item[1]}: "))
                    except:
                        print("Inavlid Entry")
                        continue
                    for product in products_list:
                        if str(product.id) == item_id:
                            if new_quantity > 0 and new_quantity <= product.quantity:  
                                product.quantity += (item[2] - new_quantity)  
                                item[2] = new_quantity
                                print("Quantity updated.")
                            else:
                                print("Invalid quantity or item not available in sufficient quantity. Quantity unchanged.")
                            break
                    break
            else:
                print("Item not found in your cart.")
        
        elif choice == '3':  
            display_all_products()
            item_id = input("Enter the ID of the item you want to add: ").strip().lower()
            found = False
            for product in products_list:
                if str(product.id) == item_id:
                    quantity = int(input(f"How many {product.name} do you want to add? "))
                    if quantity > 0 and quantity <= product.quantity:
                        cart.append([product.id, product.name, quantity, product.price])
                        product.quantity -= quantity
                        print(f"{quantity} {product.name} added to your cart.")
                        found = True
                    else:
                        print("Invalid quantity or item not available. Please try again.")
                    break
            if not found:
                print("Item not found. Please try again.")

        elif choice == '4':  
            print("Exiting cart editing.")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
