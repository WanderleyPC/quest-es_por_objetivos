def filtro_n_repetição(questões_novas):
    try:
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        import json
        import os
    
        """Recebe as novas questões recem criadas na forma de uma lista, une elas as questões anteriores, calcula a similiaridade entre elas e retorna apenas as questões que diferem o suficiente das já presente em uma lista"""
        # Verifica se o banco de questões já existe ou se ainda deve ser criado
        if os.path.exists('banco_de_questões.json'):
            # Trás as questões antigas do banco de questões
            with open('banco_de_questões.json', 'r', encoding='utf-8') as configuração:
                questões_anteriores=json.load(configuração)

            # Une as questões antigas as novas
            questões= questões_anteriores+questões_novas

        else:
            # Cria um banco de questões para quando não tem um 
            with open("banco_de_questões.json", "w", encoding="utf-8") as arquivo:
                json.dump(questões_novas, arquivo, ensure_ascii=False)
            # Considera apenas as questões novas como questões validas
            questões=questões_novas
            
        # Vetorização (sem stopwords automáticas)
        vectorizer = TfidfVectorizer(
            lowercase=True
        )

        matriz = vectorizer.fit_transform(questões)

        # Similaridade do cosseno
        similaridade = cosine_similarity(matriz)

        # Limiar de similaridade
        limiar = 0.6

        # Vai indetificar quais são as novas questões que são repetidas
        novas_questões_são_repetidas=[]
        parecidas=0

        for i in range(len(questões)):
            for j in range(i + 1, len(questões)):
                if similaridade[i][j] >= limiar:
                    # print(f"Questões {i+1} e {j+1} são parecidas ({similaridade[i][j]:.2f})")
                    parecidas=parecidas+1

                    # Ele vai salvar a **posição** da novas questões que sã0 repetidas
                    novas_questões_são_repetidas.append(j-len(questões_anteriores))
        
        # Remove elementos que estejam repetidos na minha lista: eles surgem pois as verses uma nova questão é igual a uma outra nova questão. No caso eu mando a posição das duas novas questões para ambas serem eliminadas.
        ''' # Não precisa mais pois eu já estou mandando as questões diretamente, mas se fosse a posição seria necessário desse filtro
        novas_questões_são_repetidas_limpo=[]
        for i in novas_questões_são_repetidas:
            if i not in novas_questões_são_repetidas_limpo:
                novas_questões_são_repetidas_limpo.append(i)
        
        if parecidas==0:
            print('Todas as questões são diferentes entre si')
        '''
        # Elimino as questões repetidas
        questões_não_repetidas=[]
        for i, a in enumerate(questões_novas):
            if i not in novas_questões_são_repetidas:
                questões_não_repetidas.append(a)
            
        return questões_não_repetidas
   
    except Exception  as e:
        print(f"Ocorreu um erro na Filtro_de_questões_repetidas.py. Erro: {e}")
