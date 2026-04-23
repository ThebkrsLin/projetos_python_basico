from random import randint
from time import sleep
matrix = []
while True:
    try:
        addl = int(input("quantas linhas você quer adicionar na matrix?:"))
        addc = int(input("Quantas colunas você quer adicionar na matrix?: "))

    except:
        print("O valor digitado Não é um número, tente novamente!!")

    else:
        if(addc > 0 and addl > 0):
            print("Gerando as linhas e as colunas da matriz.....")
            sleep(1)
            for l in range(0, addl):
                matrix.append([])
                for c in range(0, addc):
                    matrix[l].append([])
            print("Matriz criada com sucesso!!!")
            choose = str(input("Quer gerar os valores da matriz automaticamente?[S/N]: ")).upper().strip()

            while True:
                match choose:
                    case "S": 
                        for l in range(0, addl):
                            for c in range(0, addc):
                                matrix[l][c].append(randint(0, 999))

                    case "N":
                        for l in range(0, addl):
                            for c in range(0, addc):
                                matrix[l][c].append(int(input(f"Digite o valor na posição[{l+1}, {c+1}]: ")))

                    case Default:
                        print("Opção inválida tente novamente")
                    
                break

            print("Matriz:", end=" ")
            for l in range(0, addl):
                print("[", end=" ")
                for c in range(0, addc):
                    print(matrix[l][c], end=" ")
                print("]")
            break
        else:
            print("Os valores da linha e/ou da coluna não podem ser menor ou igual a 0, tente novamente!!!")
