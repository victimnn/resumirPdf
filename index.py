import os
import yaml
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter

# Carregar as configurações da API
GOOGLE_API_KEY = st.secrets["general"]["GOOGLE_API_KEY"]

os.environ['GOOGLE_API_KEY'] = GOOGLE_API_KEY

# Configurar o modelo de linguagem
llm = ChatGoogleGenerativeAI(model='gemini-1.5-pro', temperature=0.7)

def resumir_documento(caminho_arquivo):
    # Carregar o documento
    loader = PyMuPDFLoader(caminho_arquivo)
    document = loader.load()

    # Extração de texto das páginas
    pages_text = [page.page_content for page in document]

    # Dividir o texto em pedaços menores
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(" ".join(pages_text))

    # Configurar o prompt
    prompt_template = PromptTemplate(
        input_variables=["text"],
        template="Resuma o seguinte texto em uma explicação concisa e informativa, destacando as ideias principais e pontos importantes, sem omitir informações essenciais, se possível formate em markdown para melhor visualização: Texto: {text}"
    )

    # Criar a cadeia LLMChain com o modelo e o prompt
    chain = LLMChain(llm=llm, prompt=prompt_template)

    # Gerar os resumos para cada pedaço de texto
    resumos = []
    for text in texts:
        resumo = chain.run({"text": text})
        resumos.append(resumo)

    # Combinar os resumos
    resumo_final = " ".join(resumos)
    return resumo_final

# Interface do Streamlit
st.title("Resumidor de PDF")

uploaded_file = st.file_uploader("Escolha um arquivo PDF", type="pdf")

if st.button('Gerar Resumo'):
    # Verificar se o arquivo é realmente um PDF
    if uploaded_file.type != "application/pdf":
        st.error("Por favor, envie um arquivo no formato PDF.")
    else:
        # Salvar o arquivo temporariamente
        with open("temp.pdf", "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            # Chamar a função de resumo
            resumo = resumir_documento("temp.pdf")
            
            # Exibir o resumo
            st.subheader("Resumo do Documento")
            st.write(resumo)
        except Exception as e:
            st.error(f"Ocorreu um erro ao resumir o documento: {e}")
        finally:
            # Remover o arquivo temporário após o uso
            os.remove("temp.pdf")
