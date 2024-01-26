# Registrar tarefas
def registro():
    tarefas = []
    while True:
        tarefa = input("Digite uma tarefa (ou 'sair' para parar): ")
        if tarefa.lower() == 'sair':
            break
        tarefas.append(tarefa)
    return tarefas

# Ver tarefas 
def vertarefas(tarefas):

    # enumerar os indices junto as tarefas:
    for index,regis in enumerate(tarefas, 1):
        print(f'{index} -  {regis}')

# Excluir tarefa
def excluir_tarefa(tarefas):
    indice = int(input('Numero da tarefa: ').strip()) - 1

    # Tentar excluir tarefa.
    try:
        tarefa_removida = tarefas.pop(indice)
        print(f'A tarefa {tarefa_removida} foi removida com sucesso.')

    # Caso não a registro da tarefa.
    except IndexError:
        print('Essa tarefa não foi registrada!')
