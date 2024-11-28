class LibraryQueue:
    def __init__(self):
        # Inicializa a fila como uma lista vazia
        self.queue = []

    def enqueue(self, person_name, book_title):
        # Verifica se o usuário já está na fila com o mesmo livro
        for name, title in self.queue:
            if name.upper() == person_name.upper() and title.upper() == book_title.upper():
                print(f"O usuário {person_name} já solicitou o livro '{book_title}'.")
                return  # Se já houver um pedido igual, sai da função sem adicionar novamente

        # Caso não haja duplicidade, adiciona o usuário à fila
        self.queue.append((person_name, book_title))
        print(f"{person_name} entrou na fila para pegar o livro '{book_title}'.")

    def dequeue(self):
        # Remove o cliente mais antigo, se houver alguém
        if self.queue:
            person_name, book_title = self.queue.pop(0)
            print(f"{person_name} foi atendido(a) e pode pegar o livro '{book_title}'.")
            return person_name, book_title
        else:
            # Se não tiver ninguém, retorna que a lista está vazia
            print("A fila está vazia. Não há clientes para remover.")
            return None

    def display_queue(self):
        # Mostra o estado da fila com nome do cliente e livro
        if self.queue:
            print("Fila de espera:")
            for i, (person_name, book_title) in enumerate(self.queue, start=1):
                print(f"{i}. {person_name} - '{book_title}'")
        else:
            print("A fila está vazia.")


# Inicia a fila da biblioteca fora do loop
library_queue = LibraryQueue()

# Cadastro inicial, entrada a partir do terminal
while True:
    print("Cadastro de novos clientes para atendimento")
    
    # Nome do cliente - strip desconsidera os espaços em branco antes e depois do nome
    person_name = input("Nome: ").strip()
    # Se a pessoa não colocar o nome o programa "barra" enquanto não inserir um nome válido
    while not person_name:
        print("O nome não pode estar vazio.")
        person_name = input("Nome: ").strip()
    
    # Mesmo processo do nome, dessa vez para o livro
    book_title = input("Título do livro procurado: ").strip()
    while not book_title:
        print("O título do livro não pode estar vazio.")
        book_title = input("Título do livro procurado: ").strip()

    library_queue.enqueue(person_name, book_title)  # Adiciona nome e título à fila

    # Pergunta ao usuário se deseja cadastrar outra pessoa
    question = input("Quer cadastrar outra pessoa? [S/N]? ").strip().upper()  # strip remove espaços e upper deixa tudo maiúsculo
    
    # Verifica a resposta e sai do loop de cadastro se a resposta for 'N'
    if question == 'N':
        break  # Sai do cadastro inicial e vai para o Menu principal


# Menu Principal para visualizar e gerenciar a fila
while True:
    # esse \n é para deixar uma linha de espaço
    menu = int(input('''\nMENU 
[0] Sair
[1] Visualizar lista de espera
[2] Cadastrar novos clientes
[3] Remover clientes da lista de espera \n
Escolha uma opção: '''))

    # Ações ao selecionar as opções do menu:
    if menu == 0:
        print("Encerrando o programa...")
        break  # Encerra o programa

    elif menu == 1:
        # Exibe a fila de espera
        library_queue.display_queue()

    elif menu == 2:
        # Cadastra novos clientes
        person_name = input("Nome: ").strip()
        while not person_name:
            # Impede que o nome esteja vazio
            print("O nome não pode estar vazio.")
            person_name = input("Nome: ").strip()
        
        book_title = input("Título procurado: ").strip()
        while not book_title:
            # Impede que o títuo esteja vazio
            print("O título do livro não pode estar vazio.")
            book_title = input("Título procurado: ").strip()
        
        # Se estiver vazio o programa fica repetindo o cadastro

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

  # Disciplina de Algoritmos e Estrutura de Dados
  # BICT - UFMA
  # Derick Carvalho Freitas; João Yuri Anderson da Silva Frazão; Tarsila Tereza Santos Pinheiro      