from personagem import criar_personagem
from aventura import aventura

def main():
    personagem = criar_personagem()
    aventura(personagem)

if __name__ == '__main__':
    main()

