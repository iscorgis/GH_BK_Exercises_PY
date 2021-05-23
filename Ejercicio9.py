

def investing():
    while True:
        qty_quantity = input("Insert the quantity to invest: ")
        percentage = input("Insert the percentage: ")
        num_years = input("Insert the investing years period: ")
        try:
            qty_quantity = float(qty_quantity)
            percentage = float(percentage)
            num_years = int(num_years)
            return round(qty_quantity + ( qty_quantity * num_years * (percentage / 100) ),2)
        except ValueError:
            print("The input is not correct.")

print(investing() )





