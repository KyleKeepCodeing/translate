FROM python:3.8-slim

WORKDIR /app

COPY main.py .
COPY requirements.txt .

RUN pip install torch transformers flask
RUN pip install sentencepiece
RUN pip install sacremoses

EXPOSE 8010

CMD ["python", "main.py"] 