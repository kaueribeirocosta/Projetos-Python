print('==' * 10)
print('Palpites da Mega Sena')
print('==' * 10)

# 1 passo - Importar a função sample da blib random.
from random import sample

# 2 passo -  Entra com quantos jogos serão sorteados.
qnt_jogos = int(input('Quantos Jogos serão?: ').strip())

# 3 passo - sortear os jogos .
print (f'-=-=-= Soteio dos Jogos -=-=-=')
for jogos in range(qnt_jogos): # Rodamos o for com quantidade de jogos.    
    for sorteios in range(1): # Usamos um for com um range de 1.
        sorteio_jogos = sample(range(1, 61), k=6) # Chamamos a função sample para sortear.
    
    print(f'{jogos+1}° Jogo - {sorteio_jogos}') # Printamos os jogos.

print ('=-' * 5 , 'Boa Sorte', '=-' * 5)

