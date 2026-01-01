import adicionar_questões_ao_banco_de_questões
import Gerador_das_questões_mar
import Filtro_de_questões_repetidas
import aleatorizador_de_alternativas


# Gera mais questões
questões=Gerador_das_questões_mar.gerar_questão('''
1. Esclarecer a constituição (divisão anatômica e funcional) e função do sistema nervoso central.
2. Esclarecer a estrutura e função do tecido nervoso: neurônios e das células da glia.
3. Descrever a bioeletrogênese (geração e propagação do impulso nervoso).
4. Caracterizar as sinapses e esclarecer os tipos e funções dos neurotransmissores.
5. Descrever a constituição e função das meninges, barreira hematoencefálica e do líquido cerebroespinhal.
''')

# Elimino as questões que estejam repetidas. Depois você pode mandar apenas as que você acertou, assim as que você errou continuaram sendo repetidas dela propria geração da ia, até que o usuário as acerte.
questões_novas_não_repetidas= Filtro_de_questões_repetidas.filtro_n_repetição(questões)

# aleatoriza as alternativas das questões_novas_não_repetidas
questões_Altenativas_aleatorias_novas= aleatorizador_de_alternativas.aleatorizar_alternativas(questões_novas_não_repetidas)

# Salva todas no banco de questões

adicionar_questões_ao_banco_de_questões.adicionar_questões(questões_Altenativas_aleatorias_novas)