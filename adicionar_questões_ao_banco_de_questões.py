def adicionar_questões(questões_novas):
    try:
        import json
        import os
        if questões_novas!='None':
            """Recebe as novas questões recem criadas na forma de uma lista, une elas as questões anteriores depois salva no banco de dados"""
            # Verifica se o banco de questões já existe ou se ainda deve ser criado
            if os.path.exists('banco_de_questões.json'):
                # Trás as questões antigas do banco de questões
                with open('banco_de_questões.json', 'r', encoding='utf-8') as configuração:
                    questões_anteriores=json.load(configuração)

                # Une as questões antigas as novas
                questões= questões_anteriores+questões_novas

            else:
                # Considera apenas as questões novas como questões validas
                questões=questões_novas

            # Salva todas as questões no banco de questões
            with open("banco_de_questões.json", "w", encoding="utf-8") as arquivo:
                json.dump(questões, arquivo, ensure_ascii=False)
            print('Novas questões adicionadas com sucesso')
        else:
            print('Você não mandou nenhuma questão para ser salva na função adicionar_questões.py')
    except Exception  as e:
        print(f"Ocorreu um erro na adicionar_questões_ao_banco_de_questões.py. Erro: {e}")
