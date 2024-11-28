class LibraryQueue:
    def __init__(self):
        # Inicializa a fila como uma lista vazia
        self.queue = []

    def enqueue(self, person_name, book_title):
        # Adiciona uma pessoa à fila para pegar um livro específico
        self.queue.append((person_name, book_title))
        print(f"{person_name} entrou na fila para pegar o livro '{book_title}'.")

    def dequeue(self):
        # Remove a primeira pessoa da fila, se houver alguém
        if self.queue:
            person_name, book_title = self.queue.pop(0)
            print(f"{person_name} foi atendido(a) e pode pegar o livro '{book_title}'.")
            return person_name, book_title
        else:
            print("A fila está vazia.")
            return None

    def display_queue(self):
        # Exibe a fila atual
        if self.queue:
            print("Fila de espera:")
            for i, (person_name, book_title) in enumerate(self.queue, start=1):
                print(f"{i}. {person_name} - '{book_title}'")
        else:
            print("A fila está vazia.")


# Instancia a fila da biblioteca fora do loop
library_queue = LibraryQueue()

while True:
    print("Cadastro de clientes para atendimento")
    person_name = input("Nome: ")
    book_title = input("Título procurado: ")
    library_queue.enqueue(person_name, book_title)  # Adiciona à fila

    # Pergunta ao usuário se deseja cadastrar outra pessoa
    question = input("Quer cadastrar outra pessoa? [S/N]? ").strip().upper()
    
    # Verifica a resposta e sai do loop se a resposta for 'N'
    if question == 'N':
        menu = int(input('''MENU
            [0] Sair
            [1] Visualizar lista de espera
            [2] Cadastrar novos clientes
            [3] Remover clientes da lista de espera
            '''))
        if menu == 1:
            library_queue.display_queue()
        if menu == 2:
                 
        break  # Sai do cadastro


# Exibe a lista completa de pessoas na fila após o cadastro
print("\nEstado final da fila de espera")
library_queue.display_queue()
