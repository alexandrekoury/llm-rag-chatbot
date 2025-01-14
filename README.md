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

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

### Abstract <!-- Opcional! Caso não aplicável, remover esta seção -->

<!-- trocar o texto abaixo pelo resumo do trabalho, em inglês -->

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

Donec molestie, ante quis tempus consequat, mauris ante fringilla elit, euismod hendrerit leo erat et felis. Mauris faucibus odio est, non sagittis urna maximus ut. Suspendisse blandit ligula pellentesque tincidunt malesuada. Sed at ornare ligula, et aliquam dui. Cras a lectus id turpis accumsan pellentesque ut eget metus. Pellentesque rhoncus pellentesque est et viverra. Pellentesque non risus velit. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.

### 1. Introdução

A exploração de petróleo no Brasil se dá em campos terrestres e submarinos. Para realizar a produção de petróleo de um poço, se faz necessário realizar a conexão contínua entre o poço e as unidades de processamento e armazenamento. Esta conexão é realizada por meio da instalação de linhas de escoamento e de linhas de controle, sendo o ato de realizar tal conexão denominado “interligação”. Quando a interligação é realizada em um poço submarino, denota-se “interligação submarina”.

A Petrobras produz petróleo em diversos poços submarinos e as operações de interligação submarina são realizadas por empresas terceirizadas, chamadas “instaladoras”. Estas são responsáveis tanto por realizar a instalação das linhas de escoamento e controle quanto pelo planejamento operacional de tais atividades (elaborar procedimentos de engenharia, com segurança). Uma equipe de engenheiros da Petrobras é encarregada de prestar suporte técnico às instaladoras durante o planejamento das operações. Uma das formas de fazê-lo se dá através de documentos chamados TQFs (Technical Query Forms). Os TQFs são enviados pelas instaladoras quando há dúvidas técnicas que impedem o avanço do planejamento e precisam ser esclarecidas pela equipe de suporte técnico da Petrobras.

Enquanto um TQF não for respondido, a instaladora fica impossibilitada de concluir o seu procedimento operacional e, consequentemente, de realizar a interligação submarina. Isso pode gerar atrasos no planejamento das atividades, a depender dos prazos estabelecidos em cronograma. Esses atrasos, por sua vez, podem gerar custos para a petroleira.

O processo para responder TQFs pode ser demorado, uma vez que as informações se encontram desestruturadas e espalhadas em diversos diretórios e documentos diferentes. Em alguns casos, uma pesquisa aprofundada é requerida e isso acarreta buscas por vários arquivos, podendo chegar a dezenas. Além disso, membros menos experientes da equipe de suporte técnico encontram dificuldade em realizar as buscas por não conhecerem as estruturas de pastas e por não terem conhecimento suficiente para discernir as melhores fontes de informação. 

Existe, portanto, uma demanda latente por um sistema de busca inteligente, que possa auxiliar os membros da equipe de suporte técnico a encontrar insumos e embasamento para responder aos TQFs com agilidade e qualidade.

Recentemente, os grandes modelos generativos de linguagem (LLM, do inglês Large Language Models) tem atingido bom desempenho na tarefa de processamento de texto em linguagem natural. No entanto, a geração de conteúdo por modelos deste tipo possui riscos e fragilidades, como conhecimento desatualizado, falta de conhecimento sobre tópicos raros (long-tail knowledge, conhecimento de cauda longa) ou incapacidade de responder acerca de informações não públicas. A técnica RAG (Retrieval Augmented Generation) tem sido aplicada para contornar tais limitações. Ela consiste em acoplar um modelo de busca (retrieval) a um modelo generativo, de modo a melhorar o processo de geração por meio das informações encontradas pelo buscador.

Uma das principais vantagens de se utilizar RAG é a possibilidade de se aproveitar um modelo pré-treinado para uso com dados confidenciais ou de um nicho específico ([ZHAO et al] (https://arxiv.org/pdf/2402.19473), 2024). A depender da arquitetura utilizada, não é necessário sequer fazer ajuste fino do modelo. Este framework apresenta tantas vantagens que já se difundiu para diversas aplicações diferentes do processamento de texto, como áudio, vídeo e até produção científica ([HAN, SUSNJAK e MATHRANI] (https://doi.org/10.3390/app14199103), 2024). Uma aplicação comprovadamente eficaz é o desenvolvimento de chatbots baseados em RAG, capazes de responder perguntas com base em conjuntos de dados que não foram usados no seu treinamento. 

Segundo [Akkiraju et al](https://arxiv.org/pdf/2407.07858) (2024), o emprego de chatbots como sendo uma extensão de ferramentas de busca por informações relevantes em empresas tem aumentado. Com o advento de RAG, o que antes dependia de chatbots desenvolvidos internamente e de escopo limitado hoje pode se utilizar da robustez e precisão de modelos com bilhões de parâmetros, como os modelos GPT. Tais sistemas são capazes de entender linguagem natural e sintetizar conteúdo empresarial de forma coerente, o que os torna úteis para suportar atividades que dependam de conhecimento disponível de forma pouco estruturada.

#### 1.1. Objetivos

Este trabalho consistiu no desenvolvimento de um chatbot baseado em RAG para aplicação no contexto de suporte técnico de interligação submarina da Petrobras.

Inicialmente foi realizada uma pesquisa de campo através da aplicação de formulário com engenheiros da equipe para diagnóstico situacional. Em seguida, foram identificadas as fontes de informação aplicáveis. Realizou-se a extração, tratamento e carregamento dos dados das fontes de informação para um banco de dados de desenvolvimento e testes. A aplicação foi, então, desenvolvida em Python, por meio da biblioteca Langchain, utilizando uma API interna da Petrobras para comunicação com o LLM. Por fim, o acesso à aplicação foi disponibilizado para os membros da equipe de suporte técnico e testes foram realizados com coleta de suas impressões iniciais acerca do chatbot.

### 2. Modelagem

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

### 3. Resultados

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

### 4. Conclusões

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin pulvinar nisl vestibulum tortor fringilla, eget imperdiet neque condimentum. Proin vitae augue in nulla vehicula porttitor sit amet quis sapien. Nam rutrum mollis ligula, et semper justo maximus accumsan. Integer scelerisque egestas arcu, ac laoreet odio aliquet at. Sed sed bibendum dolor. Vestibulum commodo sodales erat, ut placerat nulla vulputate eu. In hac habitasse platea dictumst. Cras interdum bibendum sapien a vehicula.

Proin feugiat nulla sem. Phasellus consequat tellus a ex aliquet, quis convallis turpis blandit. Quisque auctor condimentum justo vitae pulvinar. Donec in dictum purus. Vivamus vitae aliquam ligula, at suscipit ipsum. Quisque in dolor auctor tortor facilisis maximus. Donec dapibus leo sed tincidunt aliquam.

---

Matrícula: 123.456.789

Pontifícia Universidade Católica do Rio de Janeiro

Curso de Pós Graduação *Business Intelligence Master*
