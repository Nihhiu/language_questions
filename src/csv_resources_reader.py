import os
import csv
from collections import defaultdict

def read_csvs_and_group(pasta):
    dados = defaultdict(list)
    for arquivo in os.listdir(pasta):
        if arquivo.endswith('.csv'):
            caminho = os.path.join(pasta, arquivo)
            with open(caminho, encoding='utf-8') as f:
                leitor = csv.reader(f)
                for linha in leitor:
                    if len(linha) >= 3:
                        palavra = linha[0]
                        leitura = linha[1]
                        traducao = linha[2]
                        if palavra and leitura and traducao:
                            dados[(palavra, leitura, traducao)].append(arquivo)
    # Retorna lista de tuplos únicos (palavra, leitura, tradução)
    return [ (p, l, t) for (p, l, t) in dados.keys() ]