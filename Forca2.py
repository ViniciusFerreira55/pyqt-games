#Importar as funções que vou usar
import random
import time



#Essa função abre o arquivo, sendo necessário colocar seu nome no paramentro e pega uma palavra aleatória
def abrir(nome_arquivo):
    with open(nome_arquivo, "r") as file:
        allText = file.read()
        words = allText.split("\n")
        return words

#Essa função mostra como o jogador está se saindo, contando as vidas do jogador e "printando" o desenho da forca em ASCII
def jogo(vida):
    if vida == 6:
        print("  +---+")
        print("  |   |")
        print("      |")
        print("      |")
        print("      |")
        print("      |")
        print("=========''','''")

    elif vida == 5:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("      |")
        print("      |")
        print("      |")
        print("=========''','''")
    elif vida == 4:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("      |")
        print("=========''','''")
    elif vida == 3:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("      |")
        print("=========''','''")
    elif vida == 2:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("      |")
        print("=========''','''")
    elif vida == 1:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("      |")
        print("=========''','''")
    elif vida == 0:
        print("  +---+")
        print("  |   |")
        print("  O   |")
        print("  _   |")
        print(" /|\  |")
        print(" / \  |")
        print("      |")
        print("=========''','''")


#Aqui o user coloca a opção desejada, para jogar ou adicionar ou remover.
def menu():
    op = int(input("1-Jogar\n2- Adcionar palavra\n3-remover palavra\nEscolha a opcao: "))
    return op


#Após selecionar jogar o user vem para esse menu onde ele seleciona a dificuldade, depedendo da dificuldade escolhida
# o tempo de jogo será mudado.
def diff():
    dif = int(input("1- Fácil\n2- Médio\n3-Dificil\nEscolha a dificuldade: "))
    if dif == 3:
        return 60
    elif dif == 2:
        return 90
    elif dif == 1:
        return 120

#aqui é onde o programa começa de verdade
def jogo_function():
    #essas são algumas das variveis utilizadas
    aux = " "
    letras_certas = []
    letra_chutadas = []
    vida = 6
    primeira = True
    #Dependo de qual op o user escolher ele vai para uma função ou algum codigo sera executado
    while True:
        opc = menu()
        #vai para o menu de difuculdade
        if opc == 1:
            dif = diff()
            break
        #Aqui ele adiciona uma nova palavra e uma nova dica no txt
        elif opc == 2:
            texto1 = input("Digite a palavra:"+"\n")
            with open('palavras.txt', 'a') as arquivo:
                arquivo.write(texto1 + "\n")

            texto2 = input("Digite a dica desta palavra:"+"\n")
            with open('dicas.txt', 'a') as arquivo2:
                arquivo2.write(texto2 + "\n")

        #Aqui ele deleta uma palavra e a dica correspondente do txt
        elif opc == 3:
            lista_palavras = abrir("palavras.txt")
            lista_dicas = abrir("dicas.txt")
            indice = 0
            print(lista_palavras)
            texto1 = input("Digite a palavra que deseja apagar:" + "\n")
            with open('palavras.txt', 'r') as arquivo:
                for row in arquivo:
                    row = row.replace('\n', '')
                    if texto1 == row:
                        indice = lista_palavras.index(texto1)
                        lista_palavras.pop(indice)
            with open('palavras.txt', 'w') as arquivo:
                texto_inteiro = ''
                for coisa in lista_palavras:
                    texto_inteiro += coisa + '\n'
                arquivo.write(texto_inteiro)
            with open('dicas.txt', 'w') as arquivo:
                lista_dicas.pop(indice)
                texto_inteiro2 = ''
                for coisa2 in lista_dicas:
                    texto_inteiro2 += coisa2 + '\n'
                arquivo.write(texto_inteiro2)
    #Aqui o jogo começa
    while True:
        #Aqui os preparativos como escolher a palavra, a dica e etc são feitos
        aux = ""
        if primeira == True:
            palavras = abrir("palavras.txt")
            palacorreta = random.choice(palavras)
            dicain = palavras.index(palacorreta)
            dicas = abrir("dicas.txt")
            dica = dicas[dicain]
            primeira = False
            jogo(vida)
            print("-" * len(palacorreta))
        #Aqui o user digita a primeira letra e da inicio ao jogo, começando o tempo!
        else:
            print("A palavra tem ", len(palacorreta),"Letras")
            print("Dica", dica)
            print("Letras chutadas: ",letra_chutadas)
            tempo = time.time()
            lett = str(input("Digite uma letra: ")).lower()
            tempodiff = time.time() - tempo
            #caso o tempo acabe o programa é finalizado
            if tempodiff > int(dif):
                print("Acabou o câo, o general chegou")
                break
            #Aqui é feita a checagem da letra!
            if lett in palacorreta:
                letras_certas.append(lett)
                letra_chutadas.append(lett)
            else:
                letra_chutadas.append(lett)
                vida -= 1
            jogo(vida)

            for letra_secreta in palacorreta:
                if letra_secreta in letras_certas:
                    aux += letra_secreta
                else:
                    aux += '_'
        #Caso o usuario acerte a palavra ele ganha e o programa é finalizado
        if aux == palacorreta:
             print("Você venceu, a palavra era: ", palacorreta)
             break
        else:
            print(aux)
        tempoA = time.time()
        #caso as vidas acabem o jogador perde e o programa é finalizado
        if vida == 0:
            jogo()
            print("Você perdeu, a palavra era: ",palacorreta)
            break

#Aqui é onde o programa é iniciado :)
if __name__ == '__main__':
        jogo_function()
