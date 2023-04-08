print ('x' * 12)
print ('Calculadora')
print ('x' * 12)

from time import sleep

# Entrada do número de valores a serem calculados.

num_valores = int(input('Informe quantos valores serão calculados: ').strip())

# Entrada de numeros int ou float.

valores = []
for i in range(num_valores):
    valor = input(f'Informe o {i+1}º valor: ').strip().replace(',' , '.')
    valores.append(valor)

# Lista com as opções válidas.

opcoes_validas = ['+', '-', '/', 'x']
escolha_operacao = ''

# Escolha da operação Matematica com loop de verificação.

while escolha_operacao not in  opcoes_validas:
    escolha_operacao = input ('''Escolha uma das opções abaixo:
    ( + ) = Soma
    ( - ) = Subtração
    ( / ) = Divisão
    ( x ) = Multiplicação\n
    Sua escolha? : ''').strip()
    if escolha_operacao not in opcoes_validas:
        print('Escolha inválida! Tente novamente...')
        sleep(1.0)

# Realização do cálculo com math case.
resultado = float(valores[0])
for i in range(1, len(valores)):
    valor = float(valores[i])
    operador = escolha_operacao
    match escolha_operacao:
        case ('+'):
            resultado = resultado + valor
            valores_separados = ' + '.join(valores)
        case ('-'):
            resultado = resultado - valor
            valores_separados = ' - '.join(valores)
        case ('/'):
            if valor == 0:
                print("Erro! Divisão por zero não é permitido.")
                resultado = None
                break
            else:
                resultado = resultado / valor
                valores_separados = ' / '.join(valores)
        case ('x'):
            resultado = resultado * valor 
            valores_separados = ' x '.join(valores)

# Mostra o resultado da conta.

if resultado is not None:
    print(f'Resultado:\n{valores_separados} = {resultado}')