FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["export" , "FLASK_APP=Search"]
CMD ["flask", "db", "init"]
CMD ["flask", "db", "migrate"]
CMD ["flask", "db", "upgrade"]

CMD ["python3", "services.py"]

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

