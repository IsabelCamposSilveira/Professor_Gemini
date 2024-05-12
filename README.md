# Estude com o Gemini

Este é um projeto que utiliza a API do Gemini para ajudar os usuários a estudarem melhor. Ele permite que os usuários façam perguntas sobre um texto fornecido em formato PDF e recebam respostas geradas pela IA do Gemini.

## Funcionalidades

- Os usuários podem fazer upload de um arquivo PDF.
- Eles podem escolher entre diferentes opções de como desejam interagir com o texto.
- As respostas são geradas automaticamente pelo Gemini.
- O projeto possui uma interface web amigável para facilitar a interação.

## Tecnologias Utilizadas

- Flask: Framework web em Python para o backend.
- HTML/CSS: Para a estruturação e estilização da interface do usuário.
- Bootstrap: Para estilos e componentes adicionais.
- JavaScript: Para interatividade do lado do cliente.
- Google Generative AI: Para geração de texto baseada em inteligência artificial.

## Estrutura do Projeto

- `app.py`: Arquivo principal que contém a lógica do servidor web.
- `index.html`, `result.html`: Arquivos HTML para as diferentes páginas da aplicação.
- Pasta `uploads`: Para armazenar os arquivos PDF enviados pelos usuários.

## Como Executar

1. Clone este repositório para o seu ambiente local.
2. Instale as dependências do Python listadas:
    - python -m pip install flask
    - pip install PyPDF2
    - pip install google.generativeai

3. Adicione a sua key do Gemini no arquivo 'app.py'
    - genai.configure(api_key="sua_chave_aqui")
3. Execute o arquivo `app.py` para iniciar o servidor Flask.
4. Acesse a aplicação em seu navegador, geralmente em `http://localhost:5000`
5. Começe a utilizar.

## Telas
![image](https://github.com/IsabelCamposSilveira/Professor_Gemini/assets/107281625/9ca85cf9-2aa4-41a5-ba0b-016100cb17b1)


## Contribuição

Contribuições são bem-vindas! Se você quiser melhorar este projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.
