

def add_data(numbers,max_lenght):
    while len(numbers) < max_lenght:
        try:
            numbers.append(float(input("Add your number : ")))
        except ValueError:
            print("The input is not correct, please, Insert a valid number:")

def calc_average(numbers):
    average = 0.0
    for i in numbers:
        average += i
    average = average / len(numbers)
    return average

numbers = []
add_data(numbers,3)
print("The average is : {0}".format(calc_average(numbers) ) )

