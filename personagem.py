def criar_personagem():
    nome = input("Digite o nome do seu personagem: ")
    print('Escolha sua classe: ')
    print('1 - Guerreiro')
    print('2 - Sage')
    print('3 - Archer')
    classe = input("Digite o número da classe: ")

    if classe == "1":
        classe = "Guerreiro"
    elif classe == "2":
        classe = "Sage"
    elif classe == "3":
        classe = "Archer"
    else:
        print('Classe inválida, voce será um guerreiro por padrão')
        classe = "Guerreiro"
    
    personagem = {
        'nome': nome,
        'classe': classe,
        'vida': 100,
        'ouro': 0, 
        }
        
    print(f'\n Ficha do personagem: ')
    print(f'Nome: {personagem["nome"]}')
    print(f'Classe: {personagem["classe"]}')
    print(f'Vida: {personagem["vida"]}')
    print(f'Ouro: {personagem["ouro"]}')

    return personagem


