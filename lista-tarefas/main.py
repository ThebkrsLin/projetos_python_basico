import tasks
from time import sleep

#Main Lines
while True:
    print("-="*40)
    print(f"                            Lista de Tarefas")
    print("-="*40)
    print("1 - Ver Lista")
    print("2 - Adicionar tarefa")
    print("3 - Marcar como concluido")
    print("4 - Remover uma Tarefa")
    print("5 - Sair")
    try:
        choose = int(input("Digite a opção: "))

    except (ValueError, TypeError):
        print("O Valor Digita não é um número, tente novamente...")
        sleep(1.5)

    else:
        print("="*25)
        match choose:
            case 1:
                print("Coletando Lista......")
                sleep(1.5)
                tasks.showTasks()
                str(input("Aperte enter para continuar....."))
            
            case 2:
                tasks.addTask()
                print("Adicionando tarefa.....")
                sleep(1.5)
                str(input("Tarefa adicionado com sucesso, Aperte enter para continuar....."))


            case 3:
                tasks.markTaskDone()
                str(input("Tarefa concluida, Aperte enter para continuar....."))

            case 4:
                tasks.removeTask()
                print("Removendo Tarefa....")
                sleep(1.5)
                str(input("Tarefa Removida com sucesso, Aperte enter para continuar....."))


            case 5:
                print("Saindo do Programa....") 
                print("="*25)
                break
            
            case Default:
                print("Opção inválida tente novamente!!!")
                sleep(1.5)
    print("="*25)

print("Até Logo!!!!")