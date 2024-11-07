# Resumidor de PDF com LangChain e Streamlit

Este projeto é uma aplicação em Python que utiliza **Streamlit** para criar uma interface de usuário e **LangChain** para gerar resumos de documentos PDF. O sistema permite que o usuário faça o upload de um arquivo PDF, que é processado para extrair e resumir o conteúdo das páginas.

## Funcionalidades

- **Carregar PDFs**: Carregue arquivos PDF para análise e resumo.
- **Dividir Texto**: O conteúdo do PDF é dividido em pedaços menores, facilitando o processamento e a geração de resumos.
- **Geração de Resumo**: O resumo é gerado usando o modelo de linguagem do **LangChain**.
- **Interface Interativa**: Utiliza o Streamlit para exibir o resumo gerado diretamente na interface.

## Estrutura do Código

1. **Carregamento de Configurações**:
   - As configurações da API são carregadas a partir de um arquivo `config.yaml`.
   - A chave da API para o Google Generative AI é configurada no ambiente.

2. **Configuração do Modelo de Linguagem**:
   - O modelo de linguagem `gemini-1.5-pro` do LangChain é usado com uma temperatura de `0.7` para fornecer resumos informativos.

3. **Função de Resumo**:
   - A função `resumir_documento` carrega e processa o PDF, divide o conteúdo em pedaços menores e gera resumos usando uma cadeia `LLMChain`.
   - Os resumos são combinados em um resumo final, exibido na interface.

4. **Interface do Usuário**:
   - A interface Streamlit permite que o usuário faça upload do PDF e visualize o resumo gerado.
   - Após o upload, o arquivo PDF é processado, e o conteúdo resumido é exibido diretamente na aplicação.

## Dependências

Para rodar o projeto, as seguintes bibliotecas são necessárias:

- `os`
- `yaml`
- `streamlit`
- `langchain_google_genai`
- `langchain.prompts`
- `langchain.chains`
- `langchain.document_loaders`
- `langchain.text_splitter`

### Instalando as Dependências

Certifique-se de que as dependências estão instaladas executando o comando:

```bash
pip install -r requirements.txt
