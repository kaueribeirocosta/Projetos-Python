print ('x' * 12)
print ('Calculadora')
print ('x' * 12)

# Entrada de numeros int ou float.

numero_1 = int and float(input('Informe o primeiro número: ').strip().replace(',' , '.'))
numero_2 = int and float(input('Informe o segundo número: ').strip().replace(',' , '.'))

# Escolha da operação Matematica.

escolha_operacao = input ('''Escolha uma das opações abaixo:\n
( + ) = Soma \n( - ) = Subtração \n( / ) = divisão \n( x ) = Multiplicação \n
Sua escolha? : ''').strip()

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

print (f'Resultado:\n{numero_1} {escolha_operacao} {numero_2} = {resultado}')


# while True:
#     quantidade_num = int(input('Quantos números serão calculados? : ').strip())
    
# # O for vai se repetir quantas o usuario quiser.
#     for numero in range(quantidade_num):
#         numero = input(f'Informe o {numero + 1}° número: ').strip().replace(',', '.')
        