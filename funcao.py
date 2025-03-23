import os
import json
from datetime import date

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
def file_load():
      
      try: 
            with open(arquivo, "r") as file:
                  return json.load(file)
      except Exception as e:
            print(f'arquivo vazio {e}')

#criando a função adicionar tarefas
def create_task():
      lista_tarefa = file_load()
      
      id = len(lista_tarefa)+1
      descricao = input('Descrição: ').title()
      print('Status: Concluido, Nao Feito, Andamento')
      status = input('Status: ').title().strip()
      while status not in ['Concluido', 'Andamento','Nao Feito']:
            print('Status invalido.')
            print('Escolha entre: "Concluido", "Andamento","Nao feita"')
            status=input('Status: ').title().strip()
      data_criada =str(data) 
      data_atualizada = str(data)
      
      tarefas = {
            "ID" :id,
            "Descricao" : descricao,
            "Status":status,
            "Data Criada":data_criada,
            "Data Atualizada":data_atualizada
      }
      
      lista_tarefa.append(tarefas)
      
      file_dump(lista_tarefa)

#Visualizar as tarefas
def read_task():
      print('1- Listar todas as tarefas')
      print('2 - Tarefas concluidas')
      print('3 - Tarefas nao feita ')
      print('4- Andamento')
      
      lista_tarefa = file_load()
      
      escolha = int(input('Digite uma opção: '))
      
      if escolha == 0 and escolha < 4:
            print('Escolha invalida')
      
      if escolha == 1:
            for listar in lista_tarefa:
                  print(listar)
                        
      if escolha == 2:
            for concluidas in lista_tarefa:
                  if concluidas['Status'] == 'Concluido':
                        print(concluidas)
                              
      if escolha == 3:
            for naofeito in lista_tarefa:
                  if naofeito['Status'] == 'Nao Feito':
                        print(naofeito)
            
      if escolha == 4:
            for andamento in lista_tarefa:
                  if andamento['Status'] == 'Andamento':
                        print(andamento)
 #funcao atualizar tarefa     
def update_task():

      lista_tarefa = file_load()
      
      id = int(input("Digite uma id: "))
      
      if id > len(lista_tarefa) or id < 0:
            print('Escolha invalida')
      
      for update_file in lista_tarefa:
            if update_file["ID"] == id:
                  descricao = input('Descrição: ').title()
                  print('Status: Concluido, Nao Feito, Andamento')
                  status = input('Status: ').title().strip()
                  while status not in ['Concluido', 'Andamento','Nao Feito']:
                        print('Status invalido')
                        print('Escolha: "Concluido", "Andamento", "Nao Feito"')
                        status = input('Status: ')
                  data_criada =str(data) 
                  data_atualizada = str(data)
                  
                  update_file["Descricao"] = descricao
                  update_file["Status"] = status
                  update_file["Data Criada"] = str(data)
                  update_file["Data Atualizada"] = str(data)
                  
      file_dump(lista_tarefa)
            
#funcao  deletar
def delete_task():
      print('Digite o id que deseja deletar')
      
      lista_tarefa = file_load()
      
      if len(lista_tarefa) == 0:
            print('Lista de tarefas vazia')
            
      else:
            id_update = int(input('Digite o id que deseja deletar: '))
            
            if id_update > len(lista_tarefa):
                  print('ID nao existe')
                  
            for i, cont in enumerate(lista_tarefa):
                  if cont["ID"] == id_update:
                        del lista_tarefa[i]
                        file_dump(lista_tarefa)

