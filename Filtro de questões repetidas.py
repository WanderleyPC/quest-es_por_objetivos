# Elimina questões que são muito parecidas entre si, tanto comparando as que já foram criadas antes com as que estão sendo geradas agora.
# use o que o chat falou: https://chatgpt.com/c/69541e74-0724-8330-841c-d91f3a9e1500
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Gerador_das_questões

# Suas questões (exemplo)
'''
questoes = [
    "O que é pressão arterial sistêmica?",
    "Defina pressão arterial e seus componentes",
    "Explique o mecanismo da pressão arterial",
    "O que é insuficiência cardíaca?",
    "O que é insuficiência cardiovascular?"
]'''

questões=Gerador_das_questões.gerar_questão('Pele humana')
for i in questões:
    print (i)

# Vetorização (sem stopwords automáticas)
vectorizer = TfidfVectorizer(
    lowercase=True
)

matriz = vectorizer.fit_transform(questões)

# Similaridade do cosseno
similaridade = cosine_similarity(matriz)

# Limiar de similaridade
limiar = 0.6

parecidas=0
for i in range(len(questões)):
    for j in range(i + 1, len(questões)):
        if similaridade[i][j] >= limiar:
            print(f"Questões {i+1} e {j+1} são parecidas ({similaridade[i][j]:.2f})")
            parecidas=parecidas+1
if parecidas==0:
    print('Todas as questões são diferentes entre si')