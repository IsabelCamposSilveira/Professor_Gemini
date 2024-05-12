from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import google.generativeai as genai

app = Flask(__name__)

# Configuração da API GenerativeAI
genai.configure(api_key="AIzaSyBI_2sR8gihdyGbOHeQUCpikrruTkbszdk")

# Configurações de geração
generation_config = {"temperature": 0.5}

# Configurações de segurança
safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"}
]

# Instrução do sistema
system_instruction = "Você é um professor e tudo que escrever deve ser formatado em HTML, utilizando as tags. Use a tag <p> e <h2>"

# Inicialização do modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings
)

# Iniciar a conversa 
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action')
def action():
    return render_template('action.html')

@app.route('/process', methods=['POST'])
def process():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = f"uploads/{uploaded_file.filename}"
        uploaded_file.save(file_path)

        # Inicializar uma string para armazenar o texto extraído
        texto_df = ''

        # Abrir o arquivo PDF
        with open(file_path, 'rb') as pdf_file:
            # Criar um objeto PdfReader
            pdf_reader = PdfReader(pdf_file)          

            # Iterar pelas páginas do PDF e extrair o texto
            for page_num in range(len(pdf_reader.pages)):
                texto_df += pdf_reader.pages[page_num].extract_text()
            
    texto_1 = request.form['opcao']

    if texto_1 in ['opcao1', 'opcao2', 'opcao3']:
        if texto_1 == 'opcao1':
            texto_2 = "Crie perguntas sobre o texto" + "\n" + texto_df
        elif texto_1 == 'opcao2':
            texto_2 = "Crie perguntas de múltipla escolha sobre o texto" + "\n" + texto_df
        elif texto_1 == 'opcao3':
            texto_2 = "Escreva em HTML um resumo sobre o texto, deixando em negrito os tópicos:" + "\n" + texto_df
        
        chat.send_message(texto_2)
        resposta = chat.last.text
        resposta_formatada = resposta.replace('**', '<br>').replace('*', '<br>').replace('#', '  ')         
        return render_template('result.html', resposta=resposta_formatada)       
    else:  
        texto_2 = request.form['texto'] + "\n" + texto_df
        chat.send_message(texto_2)
        resposta = chat.last.text
        resposta_formatada = resposta.replace('**', '<br>').replace('*', '<br>').replace('#', '  ')         
        return render_template('result.html', resposta=resposta_formatada)

@app.route('/conversa', methods=['POST'])
def conversa():
    texto_1 = request.form['texto']
    texto_2 = chat.last.text
    chat.send_message(texto_1 + texto_2)
    resposta = chat.last.text
    resposta_formatada = resposta.replace('**', '<br><br>').replace('*', '<br>').replace('#', '  ')         
    return render_template('result.html', resposta=resposta_formatada)  

if __name__ == '__main__':
    app.run(debug=True)
