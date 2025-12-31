# Elimina questões que são muito parecidas entre si, tanto comparando as que já foram criadas antes com as que estão sendo geradas agora.
# use o que o chat falou: https://chatgpt.com/c/69541e74-0724-8330-841c-d91f3a9e1500
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
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

# Vetorização (sem stopwords automáticas)
vectorizer = TfidfVectorizer(
    lowercase=True
)

matriz = vectorizer.fit_transform(questões)

# Similaridade do cosseno
similaridade = cosine_similarity(matriz)

# Limiar de similaridade
limiar = 0.8

parecidas=0
for i in range(len(questões)):
    for j in range(i + 1, len(questões)):
        if similaridade[i][j] >= limiar:
            print(f"Questões {i+1} e {j+1} são parecidas ({similaridade[i][j]:.2f})")
            parecidas=parecidas+1
if parecidas==0:
    print('Todas as questões são diferentes entre si')
