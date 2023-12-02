FROM python:3.10-slim

# Install pip requirements
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader omw-1.4

WORKDIR /
COPY . .

EXPOSE 8000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "src.api.server_api:app", "--host", "0.0.0.0", "--port", "8000"]
