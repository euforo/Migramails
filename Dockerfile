# Use a imagem base do Python
FROM python:3.8-slim-buster

# Configuração do ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Cria e define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos do projeto para o contêiner
COPY . /app/

# Instala as dependências do aplicativo
RUN pip install --no-cache-dir -r requirements.txt

# Comando para iniciar o aplicativo Flask
CMD ["python", "app.py"]
