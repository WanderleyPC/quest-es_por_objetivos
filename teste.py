import json

dados = [
    'questão 1',
    'Questão 2',
    'Questão 3'
]

# Escrever por cima
with open("dados.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False)


# Ler
with open('banco_de_questões.json', 'r', encoding='utf-8') as a:
    dados=json.load(a)

for a, i in enumerate(dados):

    print(f'Questão {a+1}: {i}')