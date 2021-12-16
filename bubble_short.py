class Bubble_short:
    def __init__(self, lista):
        self.sorted_lista = lista
    def method_bs(self):
        n = len(self.sorted_lista)
        for i in range(n - 1):
            for j in range(n - 1 - i):
                if self.sorted_lista[j] > self.sorted_lista[j + 1]:
                    aux = self.sorted_lista[j + 1]
                    self.sorted_lista[j + 1] = self.sorted_lista[j]
                    self.sorted_lista[j] = aux

