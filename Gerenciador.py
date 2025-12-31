import Gerador_das_questões_mar
import Filtro_de_questões_repetidas
import json
import os


# Gera mais questões
questões=Gerador_das_questões_mar.gerar_questão('Pele humana')

# Identifica a posição das novas questões que estão repetidas.
posição_questões_repetidas= Filtro_de_questões_repetidas(questões)
print(posição_questões_repetidas)

# Elimina as questões que são repetidas

# Salva todas no banco de questões
with open("banco_de_questões.json", "w", encoding="utf-8") as arquivo:
    json.dump(questões, arquivo, ensure_ascii=False)