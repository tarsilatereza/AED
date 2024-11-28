class EvenQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Apenas adiciona o número à fila se ele for par
        if item % 2 == 0:
            self.queue.append(item)
        else:
            print(f"{item} não é par e não será adicionado à fila.")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Fila vazia"

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Conteúdo da fila:", self.queue)

# Exemplo de uso:
fila_par = EvenQueue()
fila_par.enqueue(2)
fila_par.enqueue(3)  # Não será adicionado
fila_par.enqueue(4)
fila_par.enqueue(5)  # Não será adicionado
fila_par.enqueue(6)

fila_par.display()  # Deve exibir [2, 4, 6]
