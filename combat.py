import random

def combat(personagem):
    inimigo_vida = 50
    print(f'\n O inimigo apareceu!!')
    while personagem['vida'] > 0 and inimigo_vida > 0:
        print(f'\n Sua vida: {personagem['vida']}, Vida do inimigo: {inimigo_vida}')
        print('1 - Atacar')
        print('2 - Fugir')
        opcao = input('Escolha uma opção(1 ou 2)')

        if opcao == '1':
            dano = random.randint(5, 15)
            inimigo_vida -= dano
            print(f'Voce atacou o inimigo e causou {dano} de dano!')
        elif opcao == '2':
            if random.random() > 0.5:
                print('Voce conseguiu fugir!')
                break
            else:
                print('Voce vacilou e sofreu um ataque')
                personagem['vida'] -= random.randint(5, 20)
        else:
            print('scolha inválida, voce perdeu sua vez')

        if inimigo_vida <= 0:
            print('\n Voce derrotou o inimigo!')
            break
        if personagem['vida'] <= 0:
            print('\n Voce morreu!')
            break