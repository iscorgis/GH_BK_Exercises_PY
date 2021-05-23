


def fibonnaci_algorithm(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fibonnaci_algorithm(10)