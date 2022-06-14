import random
import time
vida = 6
primeira = True
dicas = ["jogo", "enigma","Instrutor mais brabo","Instrutor mais monstro","o mais gostoso da ets","Naiury e ventura","coringa","Presidente","mata tubarão","Extinto","KA KA KA","murcho"]
letras_certas = []
letra_chutadas = []
aux = " "
difff = 0

def palavra():
    pla = ["forca","charada","clebinho","leonardo","wilson","representante","palhaço","vargas","golfinho","dinossauro","kamudo","pateta"]
    plac = random.choice(pla)
    return plac, pla
def jogo():

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
def diff():
    dif = int(input("1- Fácil\n2- Médio\n3-Dificil\nEscolha a dificuldade: "))
    if dif == 3:
        return 60
    elif dif == 2:
        return 90
    elif dif == 1:
        return 120

if __name__ == '__main__':
    while True:
        aux = ""
        if primeira == True:
            dif = diff()
            palacorreta, pla = palavra()
            dicain = pla.index(palacorreta)
            dica = dicas[dicain]
            primeira = False
            jogo()
            print("-" * len(palacorreta))
        else:
            print("A palavra tem ", len(palacorreta),"Letras")
            print("Dica: ",dica)
            print("Letras chutadas: ",letra_chutadas)
            tempo = time.time()
            lett = str(input("Digite uma letra: ")).lower()
            tempodiff = time.time() - tempo
            if tempodiff > int(dif):
                print("Acabou o câo, o general chegou")
                break
            if lett in palacorreta:
                letras_certas.append(lett)
                letra_chutadas.append(lett)
            else:
                letra_chutadas.append(lett)

                vida -= 1
            jogo()

            for letra_secreta in palacorreta:
                if letra_secreta in letras_certas:
                    aux += letra_secreta
                else:
                    aux += '_'
        if aux == palacorreta:
            print("Você venceu, a palavra era: ", palacorreta)
            break
        else:
            print(aux)
        tempoA = time.time()
        if vida == 0:
            jogo()
            print("Você perdeu, a palavra era: ",palacorreta)
            break