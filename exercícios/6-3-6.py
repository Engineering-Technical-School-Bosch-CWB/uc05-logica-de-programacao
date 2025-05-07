def um():
    nome = input("Digite seu nome: ")
    cidade = input("Digite sua cidade: ")
    print(f"Olá, {nome}! Que legal saber que você é de {cidade}.")


def dois():
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))
    print(f"{base}^{expoente} = {base**expoente}")

    
def tres():
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    print(f"\nA média das notas é: {(nota1+nota2+nota3)/3}")


def quatro():
    temp = float(input("Digite a temperatura a ser convertida: "))
    print(f"Temperatura em celsius: {temp} C")
    print(f"Temperatura em fahrenheit: {(temp*1.8)+32} F")


def cinco():
    temp = float(input("Digite a temperatura a ser convertida: "))
    print(f"Temperatura em fahrenheit: {temp} F")
    print(f"Temperatura em celsius: {(temp-32)/1.8} C")


def seis():
    altura = float(input("Digite a altura do retangulo (em metros): "))
    largura = float(input("Digite a largura do retangulo (em metros): "))
    print(f"Area do retangulo = {altura*largura} m²")
    print(f"Perimetro do retangulo = {(altura+largura)*2} m")


def sete():
    raio = float(input("Digite o raio do circulo (em metros): "))
    print(f"Area do circulo = {raio**2*3.14159} m²")


quatro()