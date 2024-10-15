import pandas as pd
import numpy as np
from faker import Faker
import os
import random



def sortear_idade(tentencia_min = 20, tendencia_max = 50) -> int: 
    # Parâmetros para o sorteio
    media = (tentencia_min + tendencia_max)/2  # Média, próxima ao centro de 20 a 45
    desvio_padrao = 10  # Ajuste do desvio para que os valores sejam mais concentrados entre 20 e 45

    # Gerar número aleatório com tendência ao intervalo desejado
    idade = random.gauss(media, desvio_padrao)

    # Garantir que o valor esteja no intervalo desejado entre 18 e 100
    return max(18, min(100, int(idade)))    

caminho_arquivo = "csv/human.csv"

fake = Faker("pt_br")

servicos = {
    "DETRAN-PB": {
        "PRIMEIRA HABILITAÇÃO",
        "RENOVAÇÃO DA CNH SIMPLES",
        "SOLICITAÇÃO DE EFEITO SUSPENSIVO DE MULTAS",
        "LEILÃO DE VEÍCULOS DETRAN"
    },
    "PROCON": {
        "ATENDIMENTO AO CONSUMIDOR",
        "MEDIAÇÃO DE CONFLITOS ENTRE CONSUMIDOR E EMPRESA",
        "FISCALIZAÇÃO DE PRÁTICAS ABUSIVAS",
        "ORIENTAÇÃO JURÍDICA SOBRE DIREITOS DO CONSUMIDOR"
    },
    "CAGEPA": {
        "SOLICITAÇÃO DE SEGUNDA VIA DE CONTA",
        "PEDIDO DE LIGAÇÃO DE ÁGUA",
        "RELATÓRIO DE QUALIDADE DA ÁGUA",
        "REPARO DE VAZAMENTOS"
    },
    "PBGÁS": {
        "INSTALAÇÃO DE REDE",
        "CONSULTAR TARIFAS",
        "INFORMAR VAZAMENTO",
        "TIRAR DÚVIDAS SOBRE GÁS NATURAL"
    },
    "FUNDAC": {
        "PROGRAMAS SOCIAIS PARA ADOLESCENTES",
        "OFICINAS DE FORMAÇÃO PROFISSIONAL",
        "ATENDIMENTO PSICOSSOCIAL",
        "APOIO ÀS FAMÍLIAS DE ADOLESCENTES"
    }
}

if os.path.exists(caminho_arquivo):
    humanos= pd.read_csv(caminho_arquivo)
else:
    humanos = pd.DataFrame(columns=["Nome","Idade","Cidade","Demanda1","Demanda2"])
#humanos.add(
print([fake.name(),sortear_idade(), fake.address()])




