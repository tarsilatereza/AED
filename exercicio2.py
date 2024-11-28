# Derick Carvalho Freitas; João Yuri Anderson da Silva Frazão; Tarsila Tereza Santos Pinheiro      
# 28/11/2024 - sequência de Fibonacci
# Disciplina de Algoritmos e Estruturas de Dados
# BICT - UFMA

#Pergunta ao usuário a quantidade de termos a mostrar
num = int(input('Quantos termos você quer mostrar? '))

#inicializa a sequência com os dois primeiros termos
fibonacci = [0, 1] 

#Geração da sequência
if num <= 0:
	print("Nada a ser mostrado")
else:
	for c in range(2, num):  
   		fibonacci.append(fibonacci[-1] + fibonacci[-2])  #Soma os dois últimos números
	print('-' * 30)
	print(" -> ".join(map(str, fibonacci)), end=" ") #map() modifica todos os elementos de fibonacci para string

#Exibição da sequência
print("\nFIM")
