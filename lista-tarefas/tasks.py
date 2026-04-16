tasksList = []
doneTasks = []

def showTasks():
    print("Tarefas:")
    for i, task in enumerate(tasksList):
        print(f"{task} {doneTasks[i]}")

def addTask():
    task = str(input("Digite a tarefa: "))
    tasksList.append(task)
    doneTasks.append("[X]")

def markTaskDone():
    index = errorTreat(1)
    doneTasks[index] = "[V]"

def removeTask():
    index = errorTreat(2)
    tasksList.pop(index)
    doneTasks.pop(index)

def errorTreat(function):
    while True:
        try:
            for i, l in enumerate(tasksList):
                print(f"{i+1} - {l} - {doneTasks[i]}")
            number = int(input("Digite a tarefa a ser removida: "if function == 2 else "Digite a tarefa a ser concluida: "))

        except (ValueError, TypeError):
            print("O Valor Digita não é um número, tente novamente...")
            str(input("Aperte Enter para continuar...."))
        else:
            if number > len(tasksList):
                print("Opção inválida, tente novamente!!!!")
                str(input("Aperte Enter para continuar...."))
            else: return int(number-1)
