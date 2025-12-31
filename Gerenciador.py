import Gerador_das_questões_mar
import json
import os


#Gera mais questões
questões=Gerador_das_questões_mar.gerar_questão('Pele humana')

# Mostra as novas questões geradas
for i in questões:
    print (i)

# Verifica se o banco de questões já existe ou se ainda deve ser criado
if os.path.exists('banco_de_questões.json'):
    # Trás as questões antigas do banco de questões
    with open('banco_de_questões.json', 'r', encoding='utf-8') as configuração:
        questões_anteriores=json.load(configuração)

    # Une as questões antigas as novas
    questões= questões_anteriores+questões

else:
    # Cria um banco de questões para quando não tem um 
    with open("banco_de_questões.json", "w", encoding="utf-8") as arquivo:
        json.dump(questões, arquivo, ensure_ascii=False)

# Salva todas no banco de questões
with open("banco_de_questões.json", "w", encoding="utf-8") as arquivo:
    json.dump(questões, arquivo, ensure_ascii=False)