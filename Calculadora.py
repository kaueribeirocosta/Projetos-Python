print ('x' * 12)
print ('Calculadora')
print ('x' * 12)

from time import sleep

# Entrada de numeros int ou float.

numero_1 = float(input('Informe o primeiro número: ').strip().replace(',' , '.'))
numero_2 = float(input('Informe o segundo número: ').strip().replace(',' , '.'))

# Lista com as opções válidas.

opcoes_validas = ['+', '-', '/', 'x']
escolha_operacao = ''

# Escolha da operação Matematica com loop de verificação.

while escolha_operacao not in  opcoes_validas:
    escolha_operacao = input ('''Escolha uma das opações abaixo:\n
( + ) = Soma
( - ) = Subtração
( / ) = divisão
( x ) = Multiplicação\n
Sua escolha? : ''').strip()
    if escolha_operacao not in opcoes_validas:
        print('Escolha inválida! Tente novamente...')
        sleep (1.0)

# Realizaçao do calculo com math case.

match escolha_operacao:
    case ('+'):
        resultado = numero_1 + numero_2
    case ('-'):
        resultado = numero_1 - numero_2
    case ('/'):
        resultado = numero_1 / numero_2
    case ('x'):
        resultado = numero_1 * numero_2 

# Mostra o resultado da conta.

print (f'Resultado:\n{numero_1} {escolha_operacao} {numero_2} = {resultado}')

        