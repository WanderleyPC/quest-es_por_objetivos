def gerar_questão(objetivo):
    try:
        # Gera a varias questões a partir de um objetivo e a entrega em dentro de um lista usando o maritaca
        import openai
        import json
        import os


        # Estou importando a chave da api de fora do programa
        with open("chave_da_api.txt", "r", encoding="utf-8") as f:
            Chave_da_api = f.read()

        # Estou importando como o gerador de questões deve se comportar
        with open("comportamento do gerador questões.txt", "r", encoding="utf-8") as f:
            comportamento = f.read()

        # Chama a Ia para gerar a questão
        client = openai.OpenAI(
            api_key=Chave_da_api,
            base_url="https://chat.maritaca.ai/api",
        )

        response = client.chat.completions.create(
        model="sabia-3.1", #   sabia-3-small
        messages=[
            {"role": "system", "content": comportamento},
            {"role": "user", "content": f"Seu objetivo é: {objetivo}."},
        ],
        max_tokens=8000,
        temperature=0.1
        )
        resposta = response.choices[0].message.content

        # Separa as questões usando o [+++] se deija elementos vazio na minha lista
        questões=[]
        texto=''
        linhas=resposta.split('\n')
        for i in linhas:
            if '[+++]' in i:
                # O [:-1] serve para tira o \n que eu estava adicionando a mais sem necessidade.
                questões.append(texto[:-1])
                texto=''
            else:
                texto=texto+i+'\n'           
        return questões
    except Exception as e:
        print(f'Ocorreu um erro no Gerador_das_questões_mar.py. Erro: {e}')