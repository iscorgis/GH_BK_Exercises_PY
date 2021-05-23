

def cuenta(total):
    if total >= 100:
        total -= total * 0.1
        print('Obtengo un 10% de descuento, total {0}'.format(total))
    else:
        print('La cuenta es inferior a 100€ y no tiene descuento, total = {0}'.format(total))

cuenta(1000)

#solución profe
#total_compra = 2500
#importe_a_pagar = total_compra

#if total_compra > 100:
#    tasa_descuento = 10
#    importe_descuento = total_compra * tasa_descuento / 100
#   improte_a_pagar = total_compra - importe_descuento

##print(improte_a_pagar)