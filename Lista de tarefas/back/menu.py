from registro import *

# Criando uma linha bonita.
def linha():
    print('-=' * 20)

# Menu de opções.
def menu():
    escolha = 0
    
    while escolha != 4:

        escolha = int(input('''1 - Registrar Tarefa 
2 - Ver tarefas 
3 - Excluir Tarefa 
4 - Sair
Sua escolha: ''').strip())
        # Registrar tarefas 
        if escolha == 1:
            tarefas = registro()
            

        # Ver tarefa
        elif escolha == 2:
            linha()
            vertarefas(tarefas)
            linha()

        # Excluir tarefa
        elif escolha == 3:
            excluir_tarefa(tarefas)
menu()
