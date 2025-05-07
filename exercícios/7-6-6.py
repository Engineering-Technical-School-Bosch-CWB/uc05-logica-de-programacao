def um():
    numero = int(input("Digite um número: "))

    if numero >= 0:
        print("O número é positivo.")
    else:
        print("O número é negativo.")


def dois():
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")


def tres():
    idade = int(input("Digite sua idade: "))

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")


def quatro():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a  segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1+nota2+nota3)/3
    print("")
    print("Media final:", media)

    if media>=7:
        print("Aprovado!!")
    else:
        if media>=4:
            print("Recuperação...")
        else:
            print("Reprovado :(")


def cinco():
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Você ainda não tem idade para tirar habilitação.")
    else:
        habilitado = input("Você já é habilitado? (sim/não): ")

        if habilitado == "sim":
            print("Você pode dirigir!")
        else:
            print("Você está apto a tirar a carteira de habilitação.")


def seis():
    usuario = input("Digite o nome de usuário: ")

    if usuario != "admin":
        print("Usuário inválido!")
    else:
        senha = input("Digite a senha: ")

        if senha == "admin@senha":
            print("Login bem-sucedido!")
        else:
            print("Senha incorreta.")


seis()