import tasks
from time import sleep

#Main Lines
while True:
    print("-="*40)
    print("             Lista de Tarefas")
    print("-="*40)
    print("1 - Ver Lista")
    print("2 - Adicionar tarefa")
    print("3 - Marcar como concluido")
    print("4 - Remover uma Tarefa")
    print("5 - Sair")
    choose = int(input("Digite a opção: "))

    match choose:
        case 1:
            print("Coletando Lista......")
            sleep(1.5)
            print("="*25)
            tasks.showTasks()
            str(input("Aperte enter para continuar....."))
            print("="*25)
        
        case 2:
            print("="*25)
            tasks.addTask()
            print("Adicionando tarefa.....")
            sleep(1.5)
            str(input("Tarefa adicionado com sucesso, Aperte enter para continuar....."))
            print("="*25)


        case 3:
            print("="*25)
            tasks.markTaskDone()
            str(input("Tarefa concluida, Aperte enter para continuar....."))
            print("="*25)

        case 4:
            print("="*25)
            tasks.removeTask()
            print("Removendo Tarefa....")
            sleep(1.5)
            str(input("Tarefa Removida com sucesso, Aperte enter para continuar....."))
            print("="*25)


        case 5:
            print("Saindo do Programa....") 
            break
        
        case Default:
            print("Opção inválida tente novamente!!!")
            sleep(1.5)

print("Até Logo!!!!")