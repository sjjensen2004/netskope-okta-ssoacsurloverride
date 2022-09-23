FROM python:3.10-slim

WORKDIR /netskope-acsurloveride

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

WORKDIR /netskope-acsurloveride/app

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]

