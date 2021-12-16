while True:
    fin = False
    list = []
    while True:
        elemento = input("elemento de la lista:")
        if elemento == "fin":
            fin = True
            break
        while True:
            try:
                elemento2 = int(elemento)
                break
            except:
                print("El elemento tiene que ser int")
        if elemento == -9999:
            break
    if fin:
        break



