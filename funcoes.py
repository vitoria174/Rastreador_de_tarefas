import json
import os
from datetime import date

data_atual = date.today()


lista_tarefa =[]
lista_concluida = []
lista_nao_feita = []
lista_andamento =[]

arquivo = "dados.json"
def init_file():
      if not os.path.exists(arquivo):
            with open (arquivo, "w") as file:
                  json.dump([], file)
            print("arquivo criado")
      else:
            pass


def load_file():
      with open (arquivo, "w") as file:
            json.load(file)

def create_task():

      id = len(lista_tarefa) +1
      descricao = input("Descrição: ")
      status = input("Status: ")
      dta_hoje = str(data_atual)
      dta_atualizada = str(data_atual)
      
      tarefas = {
            "ID" : id,
            "Descrição" : descricao,
            "Status" : status,
            "Data Hoje": dta_hoje,
            "Data Atualizada" : dta_atualizada
      }
      
      lista_tarefa.append(tarefas)
      with open (arquivo, "w") as file:
            json.dump(lista_tarefa, file)
            
def read_task():
      try:
            with open(arquivo,"r") as file:
                  arquivo_tr = json.load(file)
            for listar in arquivo_tr:
                  print(listar)
      except:
            print('not exists')

def update_task():
      id_tarefa = int(input('ID tarefa: '))
      
      for listar in lista_tarefa:
            if id_tarefa == listar["ID"]:
                  nova_descricao = input("Nova Descrição: ")
                  novo_staus = input('Status: ')
                  listar['Descrição'] = nova_descricao
                  listar['Status'] = novo_staus
            
      print(listar)
      

while True:
      print('1-Adicionar tarefa\n2- Ler tarefas\n3- Atualizar tarefas\n0-Sair')
      opcao = int(input('Escolha uma opção: '))
      
      init_file()
      
      if opcao == 1:
            create_task()
            
      if opcao == 2:
            read_task()
      
      if opcao == 3:
            update_task()
            
      if opcao == 0:
            break