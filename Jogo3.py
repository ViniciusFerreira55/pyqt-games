import random
class Jogo3():
    UP = 0
    CP = 0
    DR = 0
    J = 0
    def escolhaJogador(self):
        self.op = int(input("1-Pedra\n2-Papel\n3-Tesoura\nDigite sua escolha: "))
        if self.op >= 1 and self.op <= 3:
            return self.op - 1
        else:
            print("Opção Invalida")
            self.escolhaJogador(self)

    def escolhaPc(self):
        choice = {0: "Pedra", 1:"Papel", 2:"Tesoura"}
        self.computer = random.randint(1, 3)
        print("Computador escolheu: ",choice.get(self.computer))
        return self.computer

    def checarChecarVencedor(self):
        self.J += 1
        if self.computer == self.op:
            print("É um empate")
            self.DR += 1
        elif self.computer == 1 and self.op == 2:
            print("Usuário Ganhou")
            self.UP += 1
        elif self.computer == 1 and self.op == 3:
            print("Computador Ganhou")
            self.CP += 1
        elif self.computer == 2 and self.op == 1:
            print("Computador Ganhou")
            self.CP += 1
        elif self.computer == 2 and self.op == 3:
            print("Usuário Ganhou")
            self.UP += 1
        elif self.computer == 3 and self.op == 1:
            print("Usuário Ganhou")
            self.UP += 1
        elif self.computer == 3 and self.op == 2:
            print("Computador Ganhou")
            self.CP += 1

    def placar(self):
        print("---Placar---")
        print("Total de Jogo: ", self.J)
        print("Pontos do Computador: ", self.CP)
        print("Pontos do Usuário: ", self.UP)
        print("Empates: ", self.DR)

    def jogo(self):
        print("Vamos começar!!")
        self.escolhaJogador(self)
        self.escolhaPc(self)
        self.checarChecarVencedor(self)
        self.placar(self)
        op = input("Continuar? S/N: ").upper()
        while True:
            if op =="S":
                self.jogo(self)
            elif op == "N":
                print("Obrigado por Jogar!")
                break
            else:
                print("Opção Invalida")
                continue

x = Jogo3
x.jogo(x)
