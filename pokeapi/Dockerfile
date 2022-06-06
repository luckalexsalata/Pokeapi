FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /pokeapi
WORKDIR /pokeapi

COPY requirements.txt .
COPY . /pokeapi/

RUN pip install -r requirements.txt

ADD . /pokeapi/
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
