def um():
    pass

def dois():
    pass

def tres():
    pass

def quatro():
    sec = int(input("Digite o tempo em segundos: "))

    horas = sec // 3600
    sec = sec % 3600
    minutes = sec // 60
    sec = sec % 60

    print(f'{horas}h {minutes}min {sec}s')

code = input("> ")
match code:
    case "1":
        um()
    case "2":
        dois()
    case "3":
        tres()
    case "4":
        quatro()
