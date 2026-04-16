from random import randint
matrix = []
addl = int(input("quantas linhas você quer adicionar na matrix?: "))
addc = int(input("Quantas colunas você quer adicionar na matrix?: "))
choose = str(input("Quer Digitar o valores da matriz manualmente?[S/N]: ")).upper().strip()
# Criando a matrix automaticamente
for l in range(0, addl):
    matrix.append([])
    for c in range(0, addc):
        matrix[l].append([])

if choose in "S":  
    # Gerando os números aleatoriamente
    for l in range(0, addl):
        for c in range(0, addc):
            matrix[l][c].append(randint(0, 999))
else:
    # O usario digita os valores da matriz
    for l in range(0, addl):
        for c in range(0, addc):
            matrix[l][c].append(int(input(f"Digite o valor na posição[{l+1}, {c+1}]")))

# Mostra a matriz
for l in range(0, addl):
    print("[", end=" ")
    for c in range(0, addc):
        print(matrix[l][c], end=" ")
    print("]")
