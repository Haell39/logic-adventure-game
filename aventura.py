from combat import combat

def aventura(personagem):
    print(f'\n Bem-vindo ao mundo de Lore!')
    print('Voce chegou em uma bifurcação na floresta negra')
    print('1 - Adentra ainda mais a floresta')
    print('2 - Ir pela caverna')
    opcao = input('Ecolha a opção 1 ou 2: ')

    if opcao == '1':
        print('Voce adentra a floresta negra')
        combat(personagem)
    elif opcao == '2':
        print('Voce adentra a caverna')
        personagem['ouro'] += 10
    else:
        print('\n Escolha inválida -> Game Over')