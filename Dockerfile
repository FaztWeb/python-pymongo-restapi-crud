FROM python:3.8-alpine

WORKDIR /code

ENV FLASK_APP=src/app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 3000

COPY . .

CMD ["flask", "run", "--port=3000"]