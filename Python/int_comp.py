ahorro_inicial = int(input('Con cuánto dinero empiezas?: '))
cantidad_mensual = int(input('Cunánto dinero al mes quieres invertir?: '))
dinero_anual = cantidad_mensual*12

tiempo_años = int(input('Cuántos años vas a invertir?: '))
interes = int(input('Cuánto interés anual te ofrecen?(Sólo el número): '))
beneficio_anual = dinero_anual * (interes / 100)
int_compuesto = (dinero_anual + beneficio_anual)*tiempo_años

print(f'Al cabo de {tiempo_años} años, tendrás {int_compuesto} euros')

