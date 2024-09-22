import random

def choice(a):
    if a == 1:
        return("Piedra")
    elif a == 2:
        return("Papel")
    elif a == 3: 
        return("Tijeras")
    elif a == 4:
        return("Lagarto")
    elif a == 5:
        return("Spock")
    else: 
        return("Una opción no válida.")
    
    
def tex():
    print(f'\nHas elegido: {choice(usuario)}')
    print(f'El PC ha elegido: {choice(pc)}')

rondas = 0
usuario_gana = 0
pc_gana = 0

while pc_gana < 3 or usuario_gana < 3:
    print('\nJuego de piedra, papel, tijeras, lagarto o Spock\n')
    print('*' * 30)
    print('Ronda', rondas)
    print('*' * 30)
    print('Puntuación PC: ', pc_gana)
    print('Puntuación Usuario: ', usuario_gana)

    
    usuario = int(
    input('Ingrese el número de la opción deseada: \n1 Piedra \n2 Papel \n3 Tijeras \n4 Lagarto \n5 Spock => '))
    pc = random.randint (1, 5)
    if pc == usuario:
        tex()
        print('Empate')
    elif (usuario == 1 and pc == 3) or (usuario == 2 and pc == 1) or (usuario == 3 and pc == 2) or (usuario == 4 and pc == 2) or (usuario == 5 and pc == 1) or (usuario == 1 and pc == 4) or (usuario == 2 and pc == 5) or (usuario == 3 and pc == 4) or (usuario == 4 and pc == 5) or (usuario == 5 and pc == 3):
        tex()
        print('Has ganado')
        usuario_gana += 1
    elif (usuario == 1 and pc == 2) or (usuario == 2 and pc == 3) or (usuario == 3 and pc == 1) or (usuario == 4 and pc == 1) or (usuario == 5 and pc == 2) or (usuario == 1 and pc == 5) or (usuario == 2 and pc == 4) or (usuario == 3 and pc == 5) or (usuario == 4 and pc == 3) or (usuario == 5 and pc == 4):
        tex()
        print('Has perdido')
        pc_gana += 1
    else:
        tex()
        print('El ordenador gana por error humano, vuelve a elegir.')
        pc_gana += 1
    
    if pc_gana == 3:
        print('El PC ha ganado')
        break
    if usuario_gana == 3:
        print('El PC ha ganado')
        break

rondas += 1