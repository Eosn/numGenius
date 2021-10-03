#Éllen Neves (ellenosneves@gmail.com)
#Trabalho solicitado pelo professor da disciplina de Programação II, Hilário Seibel Junior

import random
import os


def limpaTela():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def strToL(x):
    l = []
    for i in range(len(x)):
        l.append(int(x[i]))
    return l
    

def salvarArq(geral, maior, nome):
    if os.path.isfile('trab01.txt'): #se o doc existe, abre pra leitura, salva venc em tupla e fecha
        with open("trab01.txt", "r") as doc:
            geral = doc.read()
            geral = geral.splitlines()
            geral = tuple(geral)

    if int(geral[1]) < maior: #verifica maior e reescreve
        geral = (nome, maior)
        with open("trab01.txt", "w") as doc: #abre pra escrita e fecha
            doc.write(geral[0])
            doc.write("\n")
            doc.write(str(geral[1]))

    return geral


def main():
    nome = input("Digite seu nome: ")
    acertos = 0
    maior = 0 #maior número de acertos da seção
    geral = ("", 0) #maior pontuação geral (arquivo)
    repete = "S"

    sorteado = random.randint(0,9)
    correta = [sorteado]
    while repete != "N":
        print("O primeiro número sorteado foi: ", sorteado)
        x = strToL(input("Digite a sequência completa: ")) #transforma a str digitada pelo user em list

        while x == correta: #list user == list correta
            sorteado = random.randint(0, 9)
            correta.append(sorteado)

            limpaTela()
            print("O novo número é: ", sorteado)
            x = strToL(input("Digite a sequência completa: "))

        acertos = len(correta)-1
        print("Errou! Você acertou ", acertos, " números.")

        if acertos > maior: #verifica o maior da seção
            maior = acertos
        
        repete = input("Deseja jogar novamente? s/n ").upper() #zera tudo
        acertos = 0
        sorteado = random.randint(0,9)
        correta = [sorteado]

    geral = salvarArq(geral, maior, nome)

    print("Maior pontuacao da secao: %i acertos." % maior)
    print("Maior pontuacao geral: %s acertos, por %s" % (geral[1], geral[0]))

if __name__ == "__main__":
    main()
