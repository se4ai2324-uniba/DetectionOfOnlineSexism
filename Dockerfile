FROM python:3.10-slim

# Install pip requirements
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

WORKDIR /workdir
COPY setup.py /workdir/setup.py
COPY . /workdir/model

RUN pip install  .
EXPOSE 8000

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["uvicorn", "model.api:app", "--host", "0.0.0.0", "--port", "8000"]
