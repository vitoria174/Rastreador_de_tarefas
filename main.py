import funcao as f

#programa principal
while True:
      print('1- adicionar tarefas')
      print('2- vizualizar tarefas')
      print('3- atualizar tarefas')
      print('4- deletar')
      
      f.ini_file()
      opcao = int(input('Digite uma opção: '))
      if opcao == 1:
            f.create_task()
                  
      if opcao == 2:
            f.read_task()
      
      if opcao == 3:
            f.update_task()
            
      if opcao == 4:
            f.delete_task()
                  
      if opcao == 0:
            break
     