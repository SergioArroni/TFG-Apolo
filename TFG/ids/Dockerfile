FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN cd /app && pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]