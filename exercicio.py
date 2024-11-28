# Lista de livros na biblioteca
biblioteca = []

# Função para adicionar um livro
def adicionar_livro(titulo, autor, ano):
    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano
    }
    biblioteca.append(livro)
    print(f"Livro '{titulo}' adicionado com sucesso!")

def buscar_por_titulo(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():  # Ignorando maiúsculas e minúsculas
            return livro
    return "Livro não encontrado."

def livros_por_autor(autor):
    livros_do_autor = [livro for livro in biblioteca if livro['autor'].lower() == autor.lower()]
    if livros_do_autor:
        return livros_do_autor
    else:
        return "Nenhum livro encontrado para este autor."

def ordenar_por_ano():
    biblioteca.sort(key=lambda livro: livro['ano'])
    print("Livros ordenados por ano de publicação.")

def remover_livro(titulo):
    for livro in biblioteca:
        if livro['titulo'].lower() == titulo.lower():
            biblioteca.remove(livro)
            print(f"Livro '{titulo}' removido com sucesso!")
            return
    print("Livro não encontrado.")

# Adicionar livros
adicionar_livro("Python para Iniciantes", "João Silva", 2021)
adicionar_livro("Algoritmos em Python", "Maria Souza", 2019)
adicionar_livro("Estruturas de Dados", "João Silva", 2020)

# Buscar livro por título
print(buscar_por_titulo("Python para Iniciantes"))

# Listar livros de um autor específico
print(livros_por_autor("João Silva"))

# Ordenar livros por ano de publicação
# ordenar_por_ano()
# print(biblioteca)

# Remover um livro
# remover_livro("Algoritmos em Python")
# print(biblioteca)
