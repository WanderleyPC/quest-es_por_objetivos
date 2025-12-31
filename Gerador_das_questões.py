def gerar_questão(objetivo):
    # Gera a varias questão a partir de um objetivo e a entrega em dentro de um lista
    from google import genai
    from google.genai import types

    # Estou importando a chave da api de fora do programa
    with open("chave_da_api.txt", "r", encoding="utf-8") as f:
        Chave_da_api = f.read()

    # Estou importando como o gerador de questões deve se comportar
    with open("comportamento do gerador questões.txt", "r", encoding="utf-8") as f:
        comportamento = f.read()


    client = genai.Client(api_key=Chave_da_api)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction=comportamento,
            temperature=0.1),
        contents=f"Seu objetivo é: {objetivo}"
    )
    questões=response.text.split('[+++]')
    return (questões)


