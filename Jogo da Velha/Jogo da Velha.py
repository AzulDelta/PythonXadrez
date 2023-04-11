import numpy as np
import random as random

tabuleiro = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])

def RenderizarTabuleiro(vencedor):

    print("\033[H\033[J", end="")

    if vencedor == "EMPATE":
        print("Empate! Nao houveram vencedores!");
    else:
        if vencedor != "":
            if vencedor == "X": print("Voce ganhou!")
            else: print("O Bot ganhou!")

    print("     1  2  3")
    letras = ["A", "B", "C"]
    contadornumeros = 0

    for x in tabuleiro:
        print(f" {letras[contadornumeros]}  ", end="")
        contadornumeros += 1
        for y in x:
            print(f"[{y}]", end="")
        print()

def TestaVencedor(c):    

    for x in range(3):        
        if np.all(tabuleiro[x] == [c,c,c]):
            return c                                
        if np.all(tabuleiro[:,x] == [c,c,c]):
            return c                                
        if np.all(tabuleiro.diagonal() == [c,c,c]):
            return c            
        if np.all((np.fliplr(tabuleiro).diagonal()) == [c,c,c]):
            return c            
    if " " not in tabuleiro:
        return "EMPATE"
            


def ComputadorJoga():
    
   while(True):
       c1 = random.randint(0,2)
       c2 = random.randint(0,2)
       if tabuleiro[c1][c2] == " ": 
           tabuleiro[c1][c2] = "O"
           break

def PessoaJoga():
    
    while(True):

        jogada = input("Escolha uma casa para jogar: ")

        if not 3 > len(jogada) > 1:                        
            print("Jogada invalida. Digite uma casa valida e nao preenchida")    
            continue

        c1 = abs(65 - ord(jogada[0].upper()))                    
        c2 = int(jogada[1]) - 1

        if c2 > 2 or c1 > 2 or tabuleiro[c1][c2] != " ":                        
            print("Jogada invalida. Digite uma casa valida e nao preenchida")
            continue
        
        tabuleiro[c1][c2] = "X"
        break        
                
while(True):        

    RenderizarTabuleiro("")
    PessoaJoga()    
    encerrar = TestaVencedor("X")
    RenderizarTabuleiro(encerrar)

    if encerrar == "X" or encerrar == "O":
       resposta = input("Digite Sim caso queira jogar novamente: ")
       if resposta.upper() == ("SIM"):
           tabuleiro = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])
           continue
       else: break

    if encerrar == "EMPATE":
        resposta = input("Digite Sim caso queira jogar novamente: ")
        if resposta.upper() == ("SIM"):
           tabuleiro = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])
           continue
        else: break

    ComputadorJoga()
    encerrar = TestaVencedor("O")        
    RenderizarTabuleiro(encerrar)
    if encerrar == "X" or encerrar == "O":
        resposta = input("Digite Sim caso queira jogar novamente: ")
        if resposta.upper() == ("SIM"):
           tabuleiro = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])
           continue
        else: break

    if encerrar == "EMPATE":
        resposta = input("Digite Sim caso queira jogar novamente: ")
        if resposta.upper() == ("SIM"):
           tabuleiro = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])
           continue
        else: break
