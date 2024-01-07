FROM python:3.10-slim

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader omw-1.4

WORKDIR /

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api.server_api:app", "--host", "0.0.0.0", "--port", "8000"]