
'We assume that x is less than y'

def print_odd_numbers(x,y):
    while x < y:
        if x % 2 != 0:
            print(x, end=' ')
        x += 1

print_odd_numbers(10,20)

#Solution
#
#start, end = 4, 19

# iterating each number in list
#for num in range(start,end+1):
#
#    # checking condition
#    if num % 2 != 0:
#        print(num, end= " ")