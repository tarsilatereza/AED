while True:
	print("Cadastro de clientes para atendimento")
	name = str(input("Nome: "))
	book = str(input("Título procurado: "))
	question = str(input("Quer cadastrar outra pessoa? [S/N]? ")).upper().strip() #ver pra que serve strip

	if question == 'N':
		print(name, book)
		break #sair da área de cadastro

# Cria uma instância da fila da biblioteca
library_queue = LibraryQueue()

# Adiciona pessoas à fila
nome = str(input("Nome da pessoa: "))
library_queue.enqueue(nome, "Orgulho e Preconceito")
library_queue.enqueue("Bob", "1984")
library_queue.enqueue("Carol", "O Pequeno Príncipe")

# Exibe o estado atual da fila
library_queue.display_queue()

# Atende a primeira pessoa da fila
library_queue.dequeue()

# Exibe o estado atual da fila após o atendimento
library_queue.display_queue()

# Atende a próxima pessoa da fila
library_queue.dequeue()

# Exibe o estado atual da fila após o segundo atendimento
library_queue.display_queue()
