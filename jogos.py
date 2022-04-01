import forca
import jogo_adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("******Escolha o seu jogo!********")
    print("*********************************")

    print("Fim do jogo")

    print("(1)  Forca  (2) Adivinhação")

    jogo = int(input("Qual opção de jogo você prefere:"))

    if(jogo == 1):
        print("jogar o jogo da Forca")
        forca.jogar()
    else:
        print("jogar o jogo da Adivinhação")
        jogo_adivinhacao.jogar()

    


if(__name__ == "__main__"):
 escolhe_jogo()