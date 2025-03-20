import os
import json
from datetime import date

leitura_file =[]
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
                  json.dump(tarefa, file, indent= 4)
      except:
            print('Erra na pasta')
#funcao para ler um arquivo json
def file_load():
      
      try: 
            with open(arquivo, "r") as file:
                  json.load(file)
      
      except Exception as e:
            print(f'arquivo vazio {e}')

#criando a função adicionar tarefas
def create_task():
      id = len(lista_tarefas)+1
      descricao = input('Descrição: ').title()
      status = input('Status: ').title()
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
      tarefas = file_load()
      
      listar = [tarefa for tarefa in tarefas]
      print(listar)
      
            
#programa principal
while True:
      print('1- adicionar tarefas')
      print('2- vizualizar tarefas')
      print('3- atualizar tarefas')
      
      ini_file()
      opcao = int(input('Digite uma opção: '))
      if opcao == 1:
            create_task()
                  
      if opcao == 2:
            read_task()
                  
      if opcao == 0:
            break
     
     