from langchain_text_splitters.character import RecursiveCharacterTextSplitter
from langchain_core.language_models.llms import LLM
from langchain_core.vectorstores.base import VectorStore
from langchain_core.embeddings.embeddings import Embeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing_extensions import List
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os


class QuestionAnsweringClient():

    """
    Implementa um objeto capaz de responder a perguntas por meio de um Large Language Model (LLM).
    Baseia-se nos objetos da biblioteca LangChain.
    """

    def __init__(self, llm_model: LLM, vectorstore: VectorStore = None, **kwargs):
        
        self.llm_model = llm_model
        self.vectorstore = vectorstore
        if vectorstore is not None:
            self.retriever = vectorstore.as_retriever(**kwargs) # Responsável por encontrar os documentos relevantes

    def answer_question(self, question:str, verbose=False) -> str:
        """
            Gera uma resposta de um modelo LLM para uma pergunta informada no input, sem utilizar RAG.

            Args:
            `question`: a pergunta que será respondida.
            verbose: opção para printar a pergunta.

            Returns:
            Retorna o texto da resposta.
        """

        prompt_text = """Answer the following question with your knowledge.
        Use three sentences maximum.
        Question: {question}
        Answer:"""

        prompt_template = ChatPromptTemplate([
            ("system", "You are a helpful assistant for question-answering tasks."),
            ("human", prompt_text)
        ])

        prompt = prompt_template.invoke({'question':question})
        output_parser = StrOutputParser()
        if verbose:
            print(f'Gerando resposta (sem RAG) para: {question}')
        return output_parser.invoke(self.llm_model.invoke(prompt))    

    def answer_question_with_rag(self, question:str, verbose=False) -> str:
        """
            Esta função gera uma resposta de um modelo LLM para uma pergunta informada no input, utilizando RAG.
            
            Args:
            `question`: a pergunta que será respondida.

            Returns:
            Retorna o texto da resposta.
        """

        if self.vectorstore is None:
            raise ValueError("É necessário instanciar QuestionAnsweringClient com um vectorstore.")

        prompt_text = """Use the following pieces of retrieved context to answer the question.
        Use three sentences maximum.
        Do NOT include the context in your answer.
        Context: {docs_content}
        Question: {question}
        Only answer based on the context and nothing else, do NOT use your previous knowledge.
        When giving an answer, do not say "based on the context" or similar phrases, just give the answer straight away.
        If you don't find the answer to the question, just say "I'm sorry, but I am unable to answer this question".
        When givin an answer, ALWAYS quote DOC TITLE and DOC NUM at the end, in brackets like this: "(DOC TITLE, DOC NUM)".
        Answer: """

        prompt_template = ChatPromptTemplate([
            ("system", "You are a helpful assistant for question-answering tasks."),
            ("human", prompt_text)
        ])

        retrieved_docs = self.retriever.invoke(question)
        docs_content = "\n==== DOCUMENT END ====\n".join(f"\n==== DOCUMENT START ====\n DOC TITLE: {doc.metadata['title']}\n DOC NUM: {doc.metadata['doc_num']} \n DOC CONTENT: {doc.page_content}" for doc in retrieved_docs)
        prompt = prompt_template.invoke({'question':question, 'docs_content':docs_content})
        output_parser = StrOutputParser()
        if verbose: print(f'Buscando resposta para: {question}')
        return output_parser.invoke(self.llm_model.invoke(prompt))

class DocumentProcessingClient():
    def __init__(self, embedding_model: Embeddings):
        self.embedding_model = embedding_model 

    def split_documents(
        self,
        chunk_size: int,
        knowledge_base: List[Document]
    ) -> List[Document]:
        """
        Divide os documentos de uma base de conhecimento em trechos com número de caracteres máximo definido.
        Utiliza a classe `RecursiveCharacterTextSplitter` da biblioteca LangChain.

        Args:
        `chunk_size`: Número de caracteres máximo de cada trecho
        `knowledge_base`: Lista de documentos da base de conhecimento

        Returns:
        Lista de documentos divididos.
        """
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_size //10,
            add_start_index=True,
            strip_whitespace=True,
            separators=["\n\n", "(?<=\. )", "(?<=\? )", "(?<=\! )", "\n", " ", ""],
        )

        docs_processed = []
        for doc in knowledge_base:
            docs_processed += text_splitter.split_documents([doc])

        # Remove duplicates
        unique_texts = {}
        docs_processed_unique = []
        for doc in docs_processed:
            if doc.page_content not in unique_texts:
                unique_texts[doc.page_content] = True
                docs_processed_unique.append(doc)

        return docs_processed_unique
    
    def create_chroma_vectorstore_from_docs(self, docs: List[Document], chunk_size: int, persist_directory="./database", verbose=False) -> Chroma:
        """ 
            Cria um vectorstore baseado em Chroma a partir de um conjunto de Documents. Internamente chama o método `split_documents`.

            Args:
            `docs`: documentos fracionados do tipo LangChain Documents.
            `embedding_model`: o modelo de embeddings que será utilizado para gerar os vetores.

            Returns:
            Retorna o objeto vector_store carregado.

        """

        database_folder_path = f"./{persist_directory}/database_chroma_{chunk_size}/"
        # Carrega o vectorstore se já existir a cópia local
        if os.path.isdir(database_folder_path):
            if verbose: print('Carregando vectorstore existente...')
            vectorstore = Chroma(collection_name="docs",embedding_function=self.embedding_model, persist_directory=database_folder_path)
        else:
            if verbose: print('Criando novo vectorstore...')
            docs_processed = self.split_documents(chunk_size=chunk_size, knowledge_base=docs)
            vectorstore = Chroma(collection_name="docs",embedding_function=self.embedding_model, persist_directory=database_folder_path)
            vectorstore.add_documents(docs_processed)

        return vectorstore