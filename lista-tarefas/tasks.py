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
    for i, l in enumerate(tasksList):
        print(f"{i+1} - {i} - {l}")
    task = int(input("Digite a tarefa a ser marcada como feita: "))
    doneTasks[task-1] = "[V]"

def removeTask():
    for i, l in enumerate(tasksList):
        print(f"{i+1} - {i} - {l}")
    task = int(input("Digite a tarefa a ser removida: "))
    tasksList.remove(task)
    doneTasks.remove(task)

