
#lista = [1,2,3,4,5]
def print_negative_numbers(list_numbers):
    for item in list_numbers:
        if type(item) == int:
            if item < 0:
                print(item, end=" ")

list_numbers = [1,2,3,4,-1,-5,-20,2,1]
print_negative_numbers(list_numbers)



