import adicionar_questões_ao_banco_de_questões
import Gerador_das_questões_mar
import Filtro_de_questões_repetidas



# Gera mais questões
questões=Gerador_das_questões_mar.gerar_questão('1. Esclarecer a constituição (divisão anatômica e funcional) e função do sistema nervoso central.')

# Elimino as questões que estejam repetidas. Depois você pode mandar apenas as que você acertou, assim as que você errou continuaram sendo repetidas dela propria geração da ia, até que o usuário as acerte.
questões_novas_não_repetidas= Filtro_de_questões_repetidas.filtro_n_repetição(questões)

# Salva todas no banco de questões
adicionar_questões_ao_banco_de_questões.adicionar_questões(questões_novas_não_repetidas)