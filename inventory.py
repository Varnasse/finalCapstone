#========The beginning of the class==========
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = int(quantity)

    def get_cost(self):
        return float(self.cost)

    def get_quantity(self):
        return int(self.quantity)

    def __str__(self):
        return f'{self.product} ({self.code}) from {self.country} - ${self.cost} each, {self.quantity} in stock'

#=============Shoe list===========
shoes_list = []

#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as f:
            next(f) # skip the first line
            for line in f:
                country, code, product, cost, quantity = line.strip().split(',')
                shoes_list.append(Shoe(country, code, product, cost, quantity))
    except FileNotFoundError:
        print("Error: Could not find inventory.txt")
    
def capture_shoes():
    country = input('Enter the country: ')
    code = input('Enter the code: ')
    product = input('Enter the product: ')
    cost = input('Enter the cost: ')
    quantity = input('Enter the quantity: ')
    shoes_list.append(Shoe(country, code, product, cost, quantity))

def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
    for shoe in shoes_list:
        print(shoe.__str__())


def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    lowest_quantity = 100000
    lowest_quantity_shoe = None
    for shoe in shoes_list:
        if int(shoe.get_quantity()) < lowest_quantity:
            lowest_quantity = int(shoe.get_quantity())
            lowest_quantity_shoe = shoe
    if lowest_quantity_shoe:
        answer = input(f"Would you like to re-stock the {lowest_quantity_shoe.product} shoes? (y/n) ")
        if answer.lower() == 'y':
            quantity_to_add = int(input("Enter the quantity to add: "))
            lowest_quantity_shoe.quantity += quantity_to_add
            update_inventory_file(lowest_quantity_shoe)
        else:
            print("Okay, no shoes have been re-stocked!")
            menu()

def update_inventory_file(shoe):
    # update the quantity in the inventory.txt file
    with open('inventory.txt', 'w') as file:
        file.write("Country,Code,Product,Cose,Quantity\n")
        for shoe in shoes_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")

def search_shoe(code):
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''
    for shoe in shoes_list:
        if shoe.code == code:
            return shoe

def value_per_item():
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    for shoes in shoes_list:
        value = shoes.get_cost() * shoes.get_quantity()
        print(f'Total value for shoes with code {shoes.code}: {value}')

def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''
    highest_quantity = -1000000
    highest_quantity_shoe = None
    for shoe in shoes_list:
        if float(shoe.get_quantity()) > highest_quantity:
            highest_quantity = float(shoe.get_quantity())
            highest_quantity_shoe = shoe
    if highest_quantity_shoe:
        print(f"{highest_quantity_shoe.product} shoes are for sale!")

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def menu():
    print("Welcome to the shoe inventory!")
    while True:
        print("Please choose an option:")
        print("1. Read shoes data")
        print("2. Capture shoes")
        print("3. View all shoes")
        print("4. Re-stock shoes")
        print("5. Search for a shoe")
        print("6. Calculate value per item")
        print("7. Determine highest quantity shoe")
        print("8. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            read_shoes_data()
        elif choice == "2":
            capture_shoes()
        elif choice == "3":
            view_all()
        elif choice == "4":
            re_stock()
        elif choice == "5":
            code = input("Enter the code of the shoe you want to search for: ")
            shoe = search_shoe(code)
            if shoe:
                print(shoe)
            else:
                print("Shoe not found.")
        elif choice == "6":
            value_per_item()
        elif choice == "7":
            highest_qty()
        elif choice == "8":
            print("Thank you for using the shoe inventory. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
