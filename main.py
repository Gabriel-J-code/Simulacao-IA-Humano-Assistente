import pandas as pd
import numpy as np
from faker import Faker
import os
import random
import json

json_data = open("orgaos_servicos.json","r",encoding='utf-8')
servicos = json.load(json_data)

def sortear_idade(tentencia_min = 20, tendencia_max = 50) -> int: 
    # Parâmetros para o sorteio
    media = (tentencia_min + tendencia_max)/2  # Média, próxima ao centro de 20 a 45
    desvio_padrao = 10  # Ajuste do desvio para que os valores sejam mais concentrados entre 20 e 45

    # Gerar número aleatório com tendência ao intervalo desejado
    idade = random.gauss(media, desvio_padrao)

    # Garantir que o valor esteja no intervalo desejado entre 18 e 100
    return max(18, min(100, int(idade)))    

caminho_arquivo = "csv/human.csv"
list_nomes_servicos = []
for orgao in servicos:
        for servico in servicos[orgao]:
            list_nomes_servicos.append((orgao, servico["servico"]))


fake = Faker("pt_br")
def sortear_servico(exceto_servico = "") -> tuple[str,str]:
    escolha = ""
    is_diferente = False
    while (not is_diferente):
        escolha = fake.random_choices(list_nomes_servicos,length=1)
        if (escolha != exceto_servico):
            is_diferente = True
    return escolha

def sortear_2_servicos()-> tuple[tuple[str,str],tuple[str,str]]:
    escolha1 = sortear_servico()
    escolha2 = sortear_servico(escolha1)
    return escolha1,escolha2
  
def gerar_persona():
    nome = fake.name()
    idade = sortear_idade()
    cidade = fake.address()
    [(orgao1,demanda1)],[(orgao2,demanda2)] = sortear_2_servicos()
    return nome,idade,cidade,orgao1,demanda1,orgao2,demanda2
    

if os.path.exists(caminho_arquivo):
    humanos= pd.read_csv(caminho_arquivo)
else:
    humanos = pd.DataFrame(columns=["Nome","Idade","Cidade","Orgao1","Demanda1","Orgao2","Demanda2"])
    for i in range(0,1000):
        humanos.loc[humanos.index.size+1]=gerar_persona()
    humanos.to_csv(caminho_arquivo)

print("shape tabela humanos",humanos.shape)
print(humanos.head(5))




