import bubble_short as bs

while True:
    list = []
    fin = False

    while True:

        while True:
            elemento = input("elemento de la lista:")
            if elemento == "fin":
                fin = True
                break
            try:
                elemento = int(elemento)
                break
            except:
                print("El elemento tiene que ser int")
#       list.append(elemento)
        if fin:
            break
        if elemento == -9999:
            break
        list.append(elemento)
    if fin:
        break
    l = bs.Bubble_short(list)
    l.method_bs()
    print("lista ordenada:", l.sorted_lista)
    del(l)



