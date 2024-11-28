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
            print("A fila está vazia. Não há clientes para remover.")
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

# Cadastro inicial, entrada a partir do terminal
while True:
    print("Cadastro de clientes para atendimento")
    person_name = input("Nome: ")
    book_title = input("Título do livro procurado: ")
    library_queue.enqueue(person_name, book_title)  # Adiciona à fila

    # Pergunta ao usuário se deseja cadastrar outra pessoa
    question = input("Quer cadastrar outra pessoa? [S/N]? ").strip().upper()  # strip remove espaços e upper deixa tudo maiúsculo
    
    # Verifica a resposta e sai do loop de cadastro se a resposta for 'N'
    if question == 'N':
        break  # Sai do cadastro inicial e vai para o Menu principal


# Menu Principal para visualizar e gerenciar a fila
while True:
    menu = int(input('''\nMENU
[0] Sair
[1] Visualizar lista de espera
[2] Cadastrar novos clientes
[3] Remover clientes da lista de espera
Escolha uma opção: '''))
    
    if menu == 0:
        print("Encerrando o programa...")
        break  # Encerra o programa

    elif menu == 1:
        # Exibe a fila de espera
        library_queue.display_queue()

    elif menu == 2:
        # Cadastra novos clientes
        person_name = input("Nome: ")
        book_title = input("Título procurado: ")
        library_queue.enqueue(person_name, book_title)
        print("\nEstado atual da fila de espera:")
        library_queue.display_queue()

    elif menu == 3:
        # Remove o cliente que chegou mais cedo
        library_queue.dequeue()
        print("\nEstado atual da fila de espera:")
        library_queue.display_queue()

    else:
        print("Opção inválida. Tente novamente.")
