

def countdown(x):
    print(x)
    if x > 0:
        countdown(x-1)
    else:
        print('Booooom!')

countdown(10)

