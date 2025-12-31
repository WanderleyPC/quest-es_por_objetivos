# 31/12/25
"""Esse programa muda as ordem com das alternativas das questões geradas. Serve para evitar o viés da IA de gerar um gabarito quase completamente comum unica alternativa"""


def aleatorizar_alternativas(questões):
    """**ELE SÓ MUDA AS ALTERNATIVA DE QUESTÕES QUE TENHAM AS ALTERNATIVAS COMO !A!**Recebe uma lista de questões, muda a ordem das alternativas e devolve a mesma lista de questões com as alternativas aleatorizadas e com a troca do !A! por A,B,C,D ou E"""
    try:
        import random

        questões_alternativas_aleatorizadas=[]
        for questão in questões:
            enunciado=[]
            alternativas=[]
            linhas=questão.split('\n')
            # Separa o enunciado das alternativas
            for linha in linhas:
                if '!A!' in linha:
                    alternativas.append(linha)
                else:
                    enunciado.append(linha)

            # Muda a ordem das alternativas de forma aleatoria usando a biblioteca random
            random.shuffle(alternativas)
            
            # Troca o !A! por uma letra
            letras=['a','b','c','d','e']
            alternativa=[]
            for i, a in enumerate(alternativas):
                alternativa.append(letras[i]+a[3:])
            alternativas=alternativa

            # Gerei uma questão na forma de lista
            questão_lista=enunciado+alternativas
            # Tranforma em uma questão só
            questão='\n'.join(questão_lista)
            questões_alternativas_aleatorizadas.append(questão)
        return questões_alternativas_aleatorizadas
    except Exception as e:
        print(f'A um erro na função aleatorizador_de_alternativas.py. Erro: {e}')

# Programa para testar a função se der algum erro
"""
import json
with open('banco_de_questões.json', 'r', encoding='utf-8') as arquivo:
    questões=json.load(arquivo)

a=aleatorizar_alternativas(questões)
for i in a:
    print(i)
    """
