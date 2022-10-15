valor = [6,9,2,0,5,2,8,6]

def modificar(valor):

    lista = list(set(valor))
    lista.sort()

    for i, c in enumerate(lista):
        if (lista[i]%2)!=0:
            lista.remove(c)

    suma = sum(lista)
    lista.insert(0,suma)

    return lista


n_lista = modificar(valor)

print(n_lista[0]==sum(n_lista[1:]))

        





   




