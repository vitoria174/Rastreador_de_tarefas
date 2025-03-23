import os
import json
from datetime import date


lista_tarefas=[]
arquivo = "dados_tarefas.json"
data = date.today()

#funcao para criar arquivo json
def ini_file():
      if not os.path.exists(arquivo):
            with open (arquivo, "w") as file:
                 json.dump([], file)
      else:
            pass

#função para escrever em arquivo json
def file_dump(tarefa):
      try:
            with open (arquivo, "w") as file:
                 return json.dump(tarefa, file, indent= 4)
      except:
            return print('Erra na pasta')
#funcao para ler um arquivo json
def file_load(escolha):
      
      try: 
            with open(arquivo, "r") as file:
                  lista_completa = json.load(file)
            
            if escolha == 1:
                  for listar in lista_completa:
                        print(listar)
                        
            if escolha == 2:
                  for concluidas in lista_completa:
                        if concluidas['Status'] == 'Concluidas':
                              print(concluidas)
                              
            if escolha == 3:
                  for naofeito in lista_completa:
                        if naofeito['Status'] == 'Nao Feito':
                              print(naofeito)
            
            if escolha == 4:
                  for andamento in lista_completa:
                        if andamento['Status'] == 'Andamento':
                              print(andamento)
                              
            if escolha == 5:
                  for cancelado in lista_completa:
                        if cancelado['Status'] == 'Cancelado':
                              print(cancelado)
            
      except Exception as e:
            print(f'arquivo vazio {e}')

#criando a função adicionar tarefas
def create_task():
      id = len(lista_tarefas)+1
      descricao = input('Descrição: ').title()
      status = input('Status: ').title().strip()
      data_criada =str(data) 
      data_atualizada = str(data)
      
      tarefas = {
            "ID" :id,
            "Descricao" : descricao,
            "Status":status,
            "Data Criada":data_criada,
            "Data Atualizada":data_atualizada
      }
      
      lista_tarefas.append(tarefas)
      
      file_dump(lista_tarefas)

def read_task():
      print('1- Listar todas as tarefas')
      print('2 - Tarefas concluidas')
      print('3 - Tarefas nao feita ') 
      print('4- Andamento')
      print('5- Cancelado')
      escolha = int(input('Digite uma opção: '))
      file_load(escolha)
      
def update_task():

      with open (arquivo, 'r') as file:
            up = json.load(file)
      
      id = int(input("Digite uma id: "))
      
      for update_file in up:
            if update_file["ID"] == id:
                  descricao = input('Descrição: ').title()
                  status = input('Status: ').title().strip()
                  data_criada =str(data) 
                  data_atualizada = str(data)
                  
                  update_file["Descricao"] = descricao
                  update_file["Status"] = status
                  update_file["Data Criada"] = str(data)
                  update_file["Data Atualizada"] = str(data)
                  
            file_dump(up)
            file_load(update_file)
            
#funcao  deletar
def delete_task():
      print('Digite o id que deseja deletar')
      with open(arquivo, "r") as file:
            deletar = json.loads(file)
      
      id = int(input('Digite o id: '))
      
      
      for lista_deletar in deletar:
            lista_deletar.pop(id)
            
            file_dump(deletar)

#programa principal
while True:
      print('1- adicionar tarefas')
      print('2- vizualizar tarefas')
      print('3- atualizar tarefas')
      print('4- deletar')
      
      ini_file()
      opcao = int(input('Digite uma opção: '))
      if opcao == 1:
            create_task()
                  
      if opcao == 2:
            read_task()
      
      if opcao == 3:
            update_task()
            
      if opcao == 4:
            delete_task()
                  
      if opcao == 0:
            break
     