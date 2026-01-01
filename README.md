# Comecei esse prejeti dia 30/12/25
# Programa
Esse programa vai:
1. Gerar 30 questões usando uma API do Gemini ou do MAritalk usando as informações de alguns livros e alinhado a um objetivo que o usuário vai dizer.
    - São questões que usaram mode-los predefinidos.
2. Aplicar filtros para verificar se a questão geradas são:
    - Relevantes
    - Corretas (sem erros)
    - Evitar questões repetidas ou muito parecidas: vai comparar com todas as questões anteriores e assim eliminar as muito parecidas (acho que existe algoritimos para isso, não precisa ser IA).
    - Aleatorizar as alternativas das questões para evitar que as questões tenham uma gabarito muito igual.
    - Eliminar questões na qual uma alternativa é muito maior que as demais (a ia tende a colocar a resposta certa maior que as outras opções).
3. Selecionar 10 questões aleatorias do numero de questões que passaram pelos filtros (se não tiver passado nem 10, então ele vai voltar na etapa anterior e vai gerar mais até dar as 10, se tiver a mais ele armazena o restante para depois). 
4. Gera o gabarito da questão.
5. Se o usuario clicar ele pode medir para a explicação do gabarito e ter um chat sobre essa questão.



# Ideias para ter mais diversidade nas questões
- Criar um banco de multiplas boas questões, separadas em:
    - questões de multipla escolha comum
    - questões de I, II, III, IV, V
    - questões de verdadeiro ou falso
    - etc
Depois o programa vai escolher aleatoriamente nesse banco de questões uma de cada e vai montar o prompt que defini o 
comportamento do gerador de questões. Isso vai garantir mais diversidade. Eu ainda posso implementar um mecanismo que
se o usuario clicar que a questão é uma questão bom ela vai automáticamente para um desses bancos de questões para 
servir como base para novas questões.
- Mudar a temperatura para mais alto, se o filtro que verifica se a resposta está certa ou não estiver dando muitas questões como errado então ele manda um comando para reduzir (temperatura dinamica).
- Criar um programa de IA que cria multiplos variações do objetivo que eu mandei (ele vai dizer o mesmo objetivo, mesma coisa, mas de forma diferente).
- Se mesmo assim, depois de algumas interações o filtro de questões repetidas estiver eliminando muitas questões, então o programa vai mandar para outro gerador de questões o objetivo, o material de referencia e as questões já acertadas e será esplicitamente dito para varias nos pontos abordados.
- Mudar a ordem com que o material de referencia é entregue para a IA.


# Ideias do mecanismo adapitativo
- O programa vai pegar questões que eu errei e vai gerar questões parecidas a ela. Essas questões que eu erro serão salvas separado pois eu não quero que o filtro de questões repetidas elimine questões pareciadas as que eu já errei. Ele só vai usa como criterio de eliminação questões que eu já acertei

# Ideias para a busca do material extra
- Um programa extrai os marcadores dos livros disponiveis (o sumário de cada livro) e agrega em um sumário só, na forma de uma lista. A Ia analiza os marcadores disponiveis e seleciona quais são os capitulos mais relevantes em ordem, coloca uma saida padronizada onde a IA só indica os itens da lista dos capitulos mais relevantes para os mais irrelevantes. O programa extrais esses capitulos, calcula o seu tamanho total e se for muito grande ativa um mecanismo auxiliar que resume os capítulos mais irrelevantes usando algum programa de resumir livro (uma ideia, talvez não funcione essa parte, mas as ideia de usar os marcadores para pegar os capítulos mais importânte é melhor que usar 


# Ideias: outros
- Dar a referência de qual livro e quais capitulos (determinado pelos marcadores) foram usados para criar cada uma das questões.

---

# Ideias que deram errado:
- mandar as questões que ele já fez e falar para fazer diferente: Se eu mandar as questões que ele já fez e falar para fazer diferente, pelos meus teste de similiaridade, tem mais chance de ele gerar questões igual (ou muito parecidas ) as que ele já fez do que deixa sem esse contexto.