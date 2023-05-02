print('==' * 10)
print('Gerador da Mega Sena')
print('==' * 10)

# 1 passo - Importar a função choices da blib random.
from random import choices

# 2 passo -  Perguntar quantos jogos serão sorteados.
qnt_jogos = int(input('Quantos Jogos serão?: ').strip())

# 3 passo - sortear os jogos .
print (f'-=-=-= Soteio dos Jogos -=-=-=')
for sorteios in range(qnt_jogos): # Usamos um for com um range que o usuario pedir.
    sorteio_jogos = choices(range(1, 61), k=6) # Chamamos a função choices para sortear.
    print(f'{sorteios+1}° Jogo - {sorteio_jogos}') # Printamos os jogos.
