<!-- antes de enviar a versão final, solicitamos que todos os comentários, colocados para orientação ao aluno, sejam removidos do arquivo -->
# Desenvolvimento de chatbot baseado em LLM utilizando framework RAG

#### Aluno: [Alexandre Marques Koury Monteiro](https://github.com/alexandrekoury)
#### Orientador: [Leonardo Alfredo Forero Mendonza](https://github.com/link_do_github).

---

Trabalho apresentado ao curso [BI MASTER](https://ica.puc-rio.ai/bi-master) como pré-requisito para conclusão de curso e obtenção de crédito na disciplina "Projetos de Sistemas Inteligentes de Apoio à Decisão".

<!-- para os links a seguir, caso os arquivos estejam no mesmo repositório que este README, não há necessidade de incluir o link completo: basta incluir o nome do arquivo, com extensão, que o GitHub completa o link corretamente -->
- [Link para o código](https://github.com/link_do_repositorio). <!-- caso não aplicável, remover esta linha -->

- [Link para a monografia](https://link_da_monografia.com). <!-- caso não aplicável, remover esta linha -->

- Trabalhos relacionados: <!-- caso não aplicável, remover estas linhas -->
    - [Nome do Trabalho 1](https://link_do_trabalho.com).
    - [Nome do Trabalho 2](https://link_do_trabalho.com).

---

### Resumo

<!-- trocar o texto abaixo pelo resumo do trabalho, em português -->

INSERIR RESUMO AQUI

### Abstract <!-- Opcional! Caso não aplicável, remover esta seção -->

<!-- trocar o texto abaixo pelo resumo do trabalho, em inglês -->

INSERIR ABSTRACT AQUI

### 1. Introdução

Os grandes modelos generativos de linguagem (LLM, do inglês Large Language Models) tem atingido bom desempenho na tarefa de processamento de texto em linguagem natural desde o início do emprego da arquitetura de Transformers. Embora sejam poderosos e capazes de gerar texto de maneira rápida e coerente, ainda há riscos e fragilidades em usar os LLMs para geração de conteúdo, por exemplo: conhecimento desatualizado, falta de conhecimento sobre tópicos raros (long-tail knowledge, conhecimento de cauda longa) ou incapacidade de responder acerca de informações não públicas ([KANG et al](https://arxiv.org/pdf/2402.03181), 2024). A estrutura RAG (Retrieval Augmented Generation) tem sido aplicada para contornar tais limitações. Ela consiste em acoplar um modelo de busca (retrieval) a um modelo generativo, de modo a melhorar o processo de geração por meio das informações encontradas pelo buscador.

Uma das principais vantagens de se utilizar RAG é a possibilidade de se aproveitar um modelo pré-treinado para uso com dados confidenciais ou de um nicho específico ([ZHAO et al](https://arxiv.org/pdf/2402.19473), 2024). A depender da arquitetura utilizada, não é necessário sequer fazer ajuste fino do modelo. Este framework apresenta tantas vantagens que já se difundiu para diversas aplicações diferentes do processamento de texto, como áudio, vídeo e até produção científica ([HAN, SUSNJAK e MATHRANI](https://doi.org/10.3390/app14199103), 2024). Uma aplicação comprovadamente eficaz é o desenvolvimento de chatbots baseados em RAG, capazes de responder perguntas com base em conjuntos de dados que não foram usados no seu treinamento. 

Segundo [Akkiraju et al](https://arxiv.org/pdf/2407.07858) (2024), o emprego de chatbots como sendo uma extensão de ferramentas de busca por informações relevantes em empresas tem aumentado. Com o advento de RAG, o que antes dependia de chatbots desenvolvidos internamente e de escopo limitado hoje pode se utilizar da robustez e precisão de modelos com bilhões de parâmetros, como os modelos GPT. Tais sistemas são capazes de entender linguagem natural e sintetizar conteúdo empresarial de forma coerente, o que os torna úteis para suportar atividades que dependam de conhecimento disponível de forma pouco estruturada. 

Em se tratando de empresas que requerem grande quantidade de mão-de-obra técnica, como a indústria do petróleo, os chatbots com RAG são bons candidatos para serem aplicações voltadas para aumento de produtividade. Uma vez que os LLMs apresentam cada vez maior capacidade de interpretação de texto, documentos grandes e complexos, como normas técnicas, ou muito especializados, como procedimentos operacionais e padrões de engenharia, podem ser mais facilmente pesquisados, interpretados e citados.

#### 1.1. Objetivos

Este trabalho consistiu no desenvolvimento de um chatbot baseado em RAG para aplicação no contexto de suporte técnico de engenharia submarina da Petrobras.

Inicialmente foi realizada uma pesquisa de campo através da aplicação de formulário com engenheiros da equipe para diagnóstico situacional. Em seguida, foram identificadas as fontes de informação aplicáveis. Realizou-se a extração, tratamento e carregamento dos dados das fontes de informação para um banco de dados de desenvolvimento e testes. A aplicação foi, então, desenvolvida em Python, por meio da biblioteca Langchain, utilizando uma API interna da Petrobras para comunicação com o LLM. Por fim, o acesso à aplicação foi disponibilizado para os membros da equipe de suporte técnico e testes foram realizados com coleta de suas impressões iniciais acerca do chatbot.

### 2. Modelagem



### 3. Resultados



### 4. Conclusões



---

Matrícula: 222.100.459

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
