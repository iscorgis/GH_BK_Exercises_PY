def create_menu(dictionary_menu):
    add_more_elements, name, price = True, "", ""

    while add_more_elements:
        name = input("Add the dish name: ")
        price = input("Add the dish price: ")
        dictionary_menu[name] = price

        if input("Do you want to add more dishes to the menu? (yes/no) ") != "yes":
            add_more_elements = False


def show_menu(dictionary_menu):
    for key in dictionary_menu:
        print("Dish : {0} - Price : {1}".format(key, dictionary_menu[key]))


def client_order(lst_order):
    add_more_elements = True
    dish = ""

    while add_more_elements:

        dish = input("Insert the dish that you want to eat: ")
        lst_order.append(dish)

        if input("Do you want to add more dishes to the order? (yes/no) ") != "yes":
            add_more_elements = False


def get_bill(dictionary_menu, lst_order, total_price):
    for item in lst_order:
        if item in dictionary_menu:
            total_price += int(dictionary_menu.get(item))
            # print(type(dictionary_menu.get(item)))
        else:
            print("The selected dish : {0} doesn't exists in the menu".format(item))

    return total_price


if __name__ == '__main__':
    dictionary_menu = {}
    lst_order = []

    # Var definition
    five, ten, twenty, fifty, hundred, two_hundred, five_hundred = 4, 10, 20, 50, 100, 200, 500
    total_price = 0

    # Create and insert data into the dictionary : dishes and prices
    create_menu(dictionary_menu)
    show_menu(dictionary_menu)

    # List to store the dishes ordered by the customer
    client_order(lst_order)

    print("The bill is: {0}".format(get_bill(dictionary_menu, lst_order, total_price)))
