FROM python:3.9-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos do projeto para o container
COPY . .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expor a porta em que o Flask vai rodar
EXPOSE 5000

# Comando para rodar o Flask
CMD ["python", "app.py"]
