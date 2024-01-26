from tkinter import *

janela = Tk()
titulo = janela.title('Lista de Tarefas')

texto_apresentacao= Label(janela, text='Lista de Tarefas! ' )
texto_apresentacao.grid(column=0, row=0)

texto_adicionartarefa = Label(janela, text='Adicionar Tarefa' )
texto_adicionartarefa.grid(column=0, row=1)

janela.mainloop()