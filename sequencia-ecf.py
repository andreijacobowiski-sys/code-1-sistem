Import os
Import sys


def leitura_dados():
    print("*** Mini Questionário\n")
    nome = input("Qual seu nome?\n")
    idade = input("Qual a sua idade?\n")
    genero = input("Voce é homem ou mulher?\n")
    endereco = input("Qual o seu endereço?\n")

    return nome, idade, genero, endereco

def impressao_dados(nome, idade, genero, endereco):
    print("*** Mini Questionário\n")
    print("olá,", nome, "\n")
    print("Idade: ", Idade, "\n")
    print("Gênero: ", Gênero, "\n")
    print("Endreço: ", Endereco, "\n")

def iniciar_app():
    leitura_dados()
    os.system('cls')
    impressao_dados()

iniciar_app()

