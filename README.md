
# Avaliação de desempenho de um sistema RAG para responder perguntas

#### Aluno: [Alexandre Marques Koury Monteiro](https://github.com/alexandrekoury)
#### Orientador: [Leonardo Alfredo Forero Mendonza](https://github.com/link_do_github).

---

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".


- [Link para o código](./source/).


---

### Resumo
O estudo avaliou o desempenho de um sistema RAG (Retrieval-Augmented Generation) desenvolvido em Python para responder perguntas, utilizando diferentes modelos de embeddings para a busca de informações em um conjunto de dados. O LLM escolhido foi o Llama 3.2 com 1 bilhão de parâmetros, e os modelos de embeddings testados foram Gecko (Google), all-mpnet-base-v2 e all-MiniLM-L6-v2 (Sentence Transformers). O conjunto de perguntas foi retirado do Stanford Question Answering Dataset (SQuAD).
Os resultados mostraram que o uso de RAG aumentou a precisão das respostas em comparação com a abordagem sem RAG, sendo a configuração com o modelo Gecko a mais eficaz. Também foi observado que modelos com embeddings de maior dimensão tiveram melhor desempenho. No entanto, a técnica RAG introduziu desafios, como o aumento de respostas sem sentido em algumas configurações, possivelmente devido ao excesso de informações passadas ao LLM. A análise do processo de busca revelou que encontrar o documento correto nem sempre resultou em respostas corretas, destacando a necessidade de otimização no balanceamento entre recuperação de documentos e geração de respostas.

### Abstract 
This study evaluated the performance of a Python-based Retrieval-Augmented Generation (RAG) system designed to answer questions using different embedding models for information retrieval. The chosen LLM was Llama 3.2 with 1 billion parameters, and the tested embedding models were Gecko (Google), all-mpnet-base-v2, and all-MiniLM-L6-v2 (Sentence Transformers). The question set was sourced from the Stanford Question Answering Dataset (SQuAD).
The results indicated that RAG improved the accuracy of answers compared to a non-RAG configuration, with the Gecko model yielding the best performance. Higher-dimensional embeddings generally provided better results. However, RAG introduced challenges such as an increase in nonsensical answers in some configurations, potentially due to information overload for the LLM. The retrieval process analysis showed that finding the correct document did not always lead to accurate answers, emphasizing the need for further optimization in balancing document retrieval and response generation.

### 1. Introdução

Os grandes modelos generativos de linguagem (LLM, do inglês Large Language Models) tem atingido bom desempenho na tarefa de processamento de texto em linguagem natural desde o início do emprego da arquitetura de Transformers. Embora sejam poderosos e capazes de gerar texto de maneira rápida e coerente, ainda há riscos e fragilidades em usar os LLMs para geração de conteúdo, por exemplo: conhecimento desatualizado, falta de conhecimento sobre tópicos raros (long-tail knowledge, conhecimento de cauda longa) ou incapacidade de responder acerca de informações não públicas ([KANG et al](https://arxiv.org/pdf/2402.03181), 2024). A estrutura RAG (Retrieval Augmented Generation) tem sido aplicada para contornar tais limitações. Ela consiste em acoplar um modelo de busca (retrieval) a um modelo generativo, de modo a melhorar o processo de geração por meio das informações encontradas pelo buscador.

Uma das principais vantagens de se utilizar RAG é a possibilidade de se aproveitar um modelo pré-treinado para uso com dados confidenciais ou de um nicho específico ([ZHAO et al](https://arxiv.org/pdf/2402.19473), 2024). A depender da arquitetura utilizada, não é necessário sequer fazer ajuste fino do modelo. Este framework apresenta tantas vantagens que já se difundiu para diversas aplicações diferentes do processamento de texto, como áudio, vídeo e até produção científica ([HAN, SUSNJAK e MATHRANI](https://doi.org/10.3390/app14199103), 2024). Uma aplicação comprovadamente eficaz é o desenvolvimento de chatbots baseados em RAG, capazes de responder perguntas com base em conjuntos de dados que não foram usados no seu treinamento. 

Segundo [Akkiraju et al](https://arxiv.org/pdf/2407.07858) (2024), o emprego de chatbots como sendo uma extensão de ferramentas de busca por informações relevantes em empresas tem aumentado. Com o advento de RAG, o que antes dependia de chatbots desenvolvidos internamente e de escopo limitado hoje pode se utilizar da robustez e precisão de modelos com bilhões de parâmetros, como os modelos GPT. Tais sistemas são capazes de entender linguagem natural e sintetizar conteúdo empresarial de forma coerente, o que os torna úteis para suportar atividades que dependam de conhecimento disponível de forma pouco estruturada. 

Em se tratando de empresas que requerem grande quantidade de mão-de-obra técnica, como a indústria do petróleo, os chatbots com RAG são bons candidatos para serem aplicações voltadas para aumento de produtividade. Uma vez que os LLMs apresentam cada vez maior capacidade de interpretação de texto, documentos grandes e complexos, como normas técnicas, ou muito especializados, como procedimentos operacionais e padrões de engenharia, podem ser mais facilmente pesquisados, interpretados e citados.

Embora traga vantagens comprovadas, a técnica RAG requer atenção a alguns aspectos diferentes para ser efetiva. Isso porque ela introduz novos elementos ao sistema de perguntas e respostas, que precisam ser adequadamente planejados e otimizados.

Em primeiro lugar, destaca-se a necessidade de preparação adequada do espaço de busca. Sejam documentos em PDF, planilhas, bancos de dados ou páginas na internet, o material que será consultado precisa ser adequadamente formatado e indexado para uma busca eficiente por parte do módulo de busca. Para isso, algumas técnicas são utilizadas, sendo uma das mais comuns a técnica de chunking, que consiste em dividir documentos de texto longos em trechos menores para melhor segmentação do conteúdo e maior assertividade nas buscas.

Além disso, faz-se necessário otimizar o sistema de busca propriamente dito. É possível realizar busca de diferentes maneiras, como por exemplo: busca por palavras-chave, busca por similaridade semântica ou uma busca híbrida. Uma das formas mais comuns para utilização de RAG com LLMs é o uso de busca semântica através de vetores densos, ou embeddings. Estes vetores são gerados por modelos de IA específicos, que são treinados para representar as relações semânticas entre as palavras como sendo uma distribuição de vetores em um espaço vetorial de várias dimensões. A busca semântica que utiliza este método tende a ser eficaz para captar nuances semânticas, embora seja mais lenta do que uma busca por palavras-chave.
Por fim, destaca-se a necessidade da elaboração de um prompt adequado para que o LLM possa gerar as respostas conforme a necessidade. Algumas técnicas de engenharia de prompt podem ser aplicadas a RAG, como one-shot ou few-shot prompting.

#### 1.1. Objetivos

Este trabalho consistiu na avaliação do desempenho de um sistema RAG desenvolvido em Python para responder perguntas. Foram consideradas três configurações de RAG diferentes, cada uma com um modelo de embeddings distinto, além de uma configuração que responde perguntas sem usar RAG. Cada uma das configurações foi utilizada para responder a um conjunto de 100 perguntas cujas respostas eram conhecidas. As respostas geradas pelos sistemas foram avaliadas manualmente pelo autor e classificadas em corretas, incorretas e sem sentido. Por fim, os desempenhos de cada sistema foram comparados, com relação à capacidade de identificar os documentos corretos, ao número de respostas certas e ao número de respostas sem sentido.

### 2. Modelagem

#### 2.1 Descrição geral das configurações

##### 2.1.1 Modelo LLM utilizado
Para realizar a etapa de geração de resposta, foi utilizado o modelo Llama 3.2. Os modelos Llama são uma família de LLMs de código aberto, treinados e disponibilizados pela Meta Platforms Inc. em diversas configurações e versões diferentes. A configuração escolhida foi a menor de todas as disponíveis, com 1 bilhão de parâmetros, por dois motivos: a) incorrer em menores custos de inferência, visto ser um modelo menor e b) ter capacidade mais limitada de responder perguntas do que os modelos maiores, o que torna mais perceptível o efeito potencializador da técnica RAG.

##### 2.1.2 Modelos de embeddings utilizados
Para efeito de comparação do desempenho, foram utilizados três diferentes modelos de embeddings pré-treinados, a saber: Gecko, também chamado text-embedding-004, um modelo generalista com 768 dimensões, disponibilizado pela Google através do serviço Google AI Studio; all-mpnet-base-v2 e all-MiniLM-L6-v2, modelos generalistas de 768 e 384 dimensões respectivamente, ambos disponibilizados pela organização Sentence Transformers Hugging Face.

Assim, foram avaliadas quatro configurações diferentes:
1)	Resposta sem RAG
2)	Resposta com RAG utilizando o modelo de embeddings Gecko
3)	Resposta com RAG utilizando o modelo de embeddings all-mpnet-base-v2
4)	Resposta com RAG utilizando o modelo de embeddings all-MiniLM-L6-v2

Cada uma das configurações foi utilizada para responder às mesmas perguntas, na mesma ordem.


#### 2.2 Implementação da lógica
Para implementação da lógica de RAG, utilizou-se um script em Python, construído com base no framework LangChain.

LangChain é uma biblioteca projetada para facilitar a construção de aplicações baseadas em Large Language Models (LLMs). Ela possui recursos aplicáveis a todas as etapas do ciclo de vida de uma aplicação, desde o desenvolvimento até seu lançamento, os quais podem ser acessados por meio de uma interface padronizada.

Criou-se um arquivo em Python contendo duas classes: DocumentProcessingClient e QuestionAnsweringClient. Ambas as classes utilizam a biblioteca LangChain como fundamento para seu funcionamento.

A classe DocumentProcessingClient precisa ser inicializada passando um modelo de embeddings no formato usado pela biblioteca LangChain. A classe possui dois métodos, split_documents e create_chroma_vectorstore_from_docs. O primeiro é responsável por fazer o processamento dos textos originais e gerar os documentos que serão consultados posteriormente pelo sistema RAG, enquanto o segundo método utiliza os documentos gerados para gerar um banco de dados vetorial com os embeddings de cada documento.

Por outro lado, a classe QuestionAnsweringClient requer um modelo LLM e um banco de dados vetorial, ambos no formato utilizado pela biblioteca LangChain, para ser inicializada. A classe também possui dois métodos, answer_question e answer_question_with_rag. O primeiro método recebe uma pergunta e retorna uma resposta diretamente gerada pelo modelo LLM, enquanto o segundo implementa a técnica RAG para geração da resposta.

(Figuras/Esquematico_QuestionAnsweringClient.png?raw=true)

#### 2.3 Conjunto de dados de avaliação
##### 2.3.1 Preparação dos documentos de contexto
De modo a avaliar o desempenho do sistema de RAG construído, utilizou-se o conjunto de desenvolvimento do Stanford Question Answering Dataset (SQuAD), originalmente desenvolvido por [Rajpurkar et al](https://arxiv.org/pdf/1606.05250) (2016). Trata-se de um conjunto de perguntas e respostas extraído de artigos da Wikipédia que se consagrou como um benchmark na área de treinamento de modelos de processamento de texto. Existem dois subconjuntos disponibilizados, sendo um de desenvolvimento (Dev Set) e um de treino (Training Set). O conjunto selecionado foi o Dev Set, por ser menor e de mais fácil manuseio, contendo 11873 perguntas com suas respectivas respostas, distribuídas em 35 áreas de conhecimento diferentes.

Além das perguntas, o SQuAD contém parágrafos dos artigos da Wikipédia que foram usados para formulá-las. Estes parágrafos foram utilizados para a etapa de busca (Retrieval) do sistema RAG desenvolvido. 
Para tanto, os parágrafos foram inicialmente subdivididos em trechos de até 1000 caracteres, uma técnica conhecida como chunking. Esta técnica tem o objetivo de padronizar o tamanho dos trechos que serão consultados, ao mesmo tempo em que reduz a quantidade de informação que cada trecho vai apresentar, o que tende a facilitar a localização de informação durante a etapa de busca. Os trechos gerados pela etapa de chunking são geralmente referenciados como chunks ou simplesmente “documentos”. 

(Figuras/Num_docs_area_conhecimento.png?raw=true)

Após a realização do chunking, foram criados embeddings de cada um dos documentos, os quais foram armazenados em um banco de dados vetorial, que, por sua vez, foi salvo localmente com uso da biblioteca ChromaDB. Cada um dos três modelos de embeddings foi usado separadamente para dar origem a um banco de vetores distinto dos demais.

##### 2.3.2 Seleção das perguntas
Do conjunto de desenvolvimento, foram selecionadas aleatoriamente 100 perguntas para serem respondidas. As perguntas abrangeram 33 das 35 áreas de conhecimento disponíveis

(Figuras/Num_perg_area_conhecimento.png?raw=true)

#### 2.4 Obtenção das respostas
Para a configuração que não utilizou RAG, aplicaram-se os passos descritos a seguir:
1) a pergunta foi inserida em um prompt;
2) o prompt foi enviado para o LLM e a resposta foi obtida.

##### 2.4.2 Configurações com RAG
Para cada uma das configurações que utilizaram RAG, aplicaram-se os passos descritos a seguir:
1)	a pergunta foi transformada em um vetor através do modelo de embeddings;
2)	utilizando o embedding da pergunta, foi feita uma busca por similaridade no banco vetorial de documentos; 
3)	foram selecionados os 10 embeddings que apresentaram o maior escore de similaridade e ordenados em ordem decrescente (os mais parecidos aparecem primeiro);
4)	os embeddings foram convertidos para texto e adicionados ao prompt, juntamente com a pergunta
5)	o prompt foi enviado para o LLM e a resposta foi obtida.

### 3. Resultados

#### 3.1 Número de respostas corretas
Uma vez classificadas as respostas, foi possível fazer uma comparação direta do desempenho de cada uma das configurações. Inicialmente compararam-se os números de respostas corretas geradas, conforme mostra a Figura XX. Os resultados evidenciam que o emprego de RAG melhorou a capacidade do sistema de responder corretamente às perguntas em todos os casos, o que é um indicativo da efetividade desta técnica. A configuração mais efetiva foi a que utiliza RAG com o modelo de embeddings Gecko.

(Figuras/Num_respostas_corretas.png?raw=true)

A configuração sem RAG respondeu adequadamente a 46 perguntas do total de 100. Estas respostas foram dadas apenas com o conhecimento adquirido pela rede neural durante o treinamento do modelo. Como o conjunto de perguntas e respostas utilizado (SQuAD) se baseia em dados disponíveis abertamente na internet (Wikipédia), era esperado que o LLM conseguisse dar respostas corretas, visto que os mesmos dados foram utilizados em seu treinamento. Em um cenário no qual as perguntas feitas dissessem respeito a dados que o modelo não conheceu durante seu treinamento (como, por exemplo, dados sigilosos de uma empresa), seria esperado que a configuração sem RAG apresentasse um número de respostas certas mais perto de zero.

Com relação às configurações com RAG, nota-se uma superioridade dos casos em que se usou um modelo de embeddings com vetores maiores (Gecko e all-mpnet-base-v2, ambos com 768 dimensões), em comparação com a configuração que usou vetores menores (all-MiniLM-L6-v2 com 384 dimensões). Esse resultado também era esperado, visto que vetores de maiores dimensões tendem a captar melhor as nuances de sentido entre as palavras e frases, o que permite um desempenho superior na tarefa de localização de informação.

Um aspecto notável dos resultados é o desempenho consideravelmente superior da configuração com o modelo Gecko, que é um modelo comercial desenvolvido pela Google, em relação ao modelo all-mpnet-base-v2, que é um modelo de código aberto. É possível que isso se dê pelo fato de o modelo all-mpnet-base-v2 não ser otimizado para a tarefa de busca em bases de dados vetoriais, enquanto o modelo Gecko foi desenvolvido a partir de um LLM para ser um buscador eficiente ([Lee et al.](https://arxiv.org/pdf/2403.20327), 2024).

#### 3.2 Número de respostas sem sentido
Além da comparação direta de respostas corretas, também foi avaliada a ocorrência de respostas “sem sentido”. Trata-se de casos específicos de resposta errada em que a resposta gerada não configura sequer um texto coerente. Exemplos de respostas sem sentido podem ser: uma sequência numérica longa ou abstrata, sem nenhuma correlação com o que foi perguntado; a repetição da pergunta feita; um texto que repete uma expressão diversas vezes, sem significado; a repetição do prompt ou de parte dele etc.

A configuração sem RAG e a configuração com o modelo Gecko apresentaram o menor número de respostas sem sentido, com 19 cada. As configurações all-mpnet-base-v2 e all-MiniLM-L6-v2 apresentaram 21 e 23, respectivamente.

O fato de duas das três configurações que usaram RAG terem causado uma piora no número de respostas sem sentido pode estar relacionado à quantidade de texto introduzida na janela de contexto do LLM. Respostas sem sentido são tipicamente ocasionadas por limitações do modelo de linguagem em si, comumente associadas a um número de parâmetros limitado. Neste trabalho, utilizou-se um modelo com 1 bilhão de parâmetros, considerado um número razoavelmente pequeno. Como foram utilizados 10 documentos de contexto para cada pergunta, é possível que o modelo tenha sido direcionado a alucinações devido ao excesso de informação que precisou processar para cada pergunta. Isso demonstra a necessidade de fazer ajustes no módulo de busca e na quantidade de documentos que serão recuperados e passados ao LLM como contexto, de modo a não o sobrecarregar na etapa de geração da resposta.

(Figuras/Num_respostas_sem_sentido.png?raw=true)

#### 3.3 Avaliação do retrieval

Também foi avaliada a capacidade de cada um dos sistemas de RAG de encontrar o documento correto (aquele que contém a resposta) para cada uma das perguntas. Considerou-se que o documento correto foi encontrado se ele estava presente dentre os 10 documentos recuperados pelo retriever.

As configurações apresentaram um desempenho semelhante, com o modelo Gecko tendo recuperado mais vezes (94 de 100), seguido do modelo all-MiniLM-L6-v2 (92 de 100) e depois do all-mpnet-base-v2 (91 de 100). Novamente, a configuração com modelo Gecko apresentou o melhor desempenho, embora com uma margem consideravelmente menor. Nota-se também que este foi o único teste em que o modelo all-MiniLM-L6-v2 superou o all-mpnet-base-v2.

Os números dos testes de busca mostram que houve diversos casos, para todas as três configurações, em que o sistema encontrou o documento correto e mesmo assim a resposta gerada não foi adequada. Tal fenômeno indica que a capacidade de responder corretamente não está associada somente ao fato de ter o documento correto dentro da janela de contexto do LLM. É preciso também considerar a possibilidade de que a presença de outros documentos tenha influência negativa na geração de resposta por parte do LLM. Para o caso deste trabalho, é possível que os documentos recuperados pela configuração com o modelo Gecko tenham sido mais coerentes entre si na maior parte das vezes, tendo menor impacto negativo no desempenho do LLM.

(Figuras/Num_docs_encontrados.png?raw=true)

### 4. Conclusões

O estudo demonstrou que a técnica RAG é eficaz para melhorar a precisão de respostas geradas por LLMs, especialmente quando aplicada com modelos de embeddings mais robustos, como o Gecko. A comparação entre as configurações revelou que o uso de embeddings com maior dimensionalidade favoreceu a recuperação de informações mais relevantes, resultando em um maior número de respostas corretas. No entanto, observou-se que a inclusão de múltiplos documentos de contexto pode sobrecarregar o modelo, levando a um aumento no número de respostas sem sentido, especialmente em configurações que utilizaram embeddings menos sofisticados. Além disso, a análise mostrou que a presença do documento correto no conjunto recuperado não garante, por si só, a geração de respostas adequadas, destacando a importância de ajustar o número de documentos recuperados e de otimizar a elaboração do prompt. Assim, a implementação de sistemas RAG deve considerar cuidadosamente a escolha do modelo de embeddings e a configuração do processo de busca para potencializar a performance do LLM.

---

Matrícula: 222.100.459

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
