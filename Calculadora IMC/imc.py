print ('-=' * 15)
print ('Ìndice de Massa Corporal (IMC)')
print ('-=' * 15)


# Loop infinito.
while True:

    # Entrada do usuário.
    altura = input('Informe o sua altura (ex: 1.70): ').strip().replace(',' , '.')
    peso = input('Informe seu peso (ex: 80): ').strip().replace(',' , '.')

    # Verifica se o usuário entrou com números.
    if peso.replace (".", "", 1).isdigit() and altura.replace (".", "", 1).isdigit():

        # Converte os inputs em float.
        peso = float(peso)
        altura = float(altura)

        # Verifica se altura ou peso é diferente de 0.
        if altura == 0 or peso == 0:
            print ('Oops! O peso e altura não podem ser zero...')
        
        # Interrompe o loop caso o if acima não seja atendido.
        else:
            break

    # Printa um erro na tela do usuário.    
    else:
        print (f'Oops! Os valores informados não são números...')
    
# calculo do IMC.
imc = peso / (altura ** 2) 

# exibe o resultado do IMC.
print ('-=' * 9)
print(f'Seu IMC é de {imc:,.1f}')
print ('-=' * 9)

# classifica o IMC com base no resultado.
if imc <= 18.5:
    print('Você está abaixo do peso!')
elif 18.6 <= imc <= 24.9:
    print('Você está no seu peso ideal!')
elif 25 <= imc <= 29.9:
    print('Você está levemente acima do peso!')
elif 30 <= imc <= 34.9:
    print('Você está com obesidade grau I.')
elif 35 <= imc <= 39.9:
    print('Você está com obesidade grau II (Severa)!')
else:
    print('Você está com obesidade grau III (Mórbida)!')
