def gameboard(x=5, y=5):
    lista = []
    for rzad in range(x):
        lista.append([])
        for kolumn in range(y):
            if rzad == 0 or rzad == x-1 or kolumn == 0 or kolumn == y-1:
                lista[rzad].append('x')
            else:
                lista[rzad].append(' ')
    return lista


def display_board(lista):
    for i in lista:
        print('  '.join(i))

display_board(gameboard(25, 25))
