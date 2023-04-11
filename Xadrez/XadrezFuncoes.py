
def RenderizarTabuleiro(tabuleiro,vencedor):

    print("\033[H\033[J", end="")

    if vencedor == "EMPATE":
        print("Empate! Nao houveram vencedores!");
    else:
        if vencedor != "":
            if vencedor == "X": print("Voce ganhou!")
            else: print("O Bot ganhou!")

    print("     1   2   3   4   5   6   7   8")
    letras = ["A", "B", "C","D","E","F","G","H"]
    contadornumeros = 0

    for x in tabuleiro:
        print(f" {letras[contadornumeros]}  ", end="")
        contadornumeros += 1
        for y in x:
            print(f"[{y}]", end="")
        print()

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