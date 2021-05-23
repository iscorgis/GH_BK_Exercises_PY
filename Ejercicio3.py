


def print_year_report(year):
    if year <= 2055:
        print('INformes del Año: {0}'.format(year) )
        print_year_report(year+1)
    else:
        print('Fin')
print_year_report(2040)