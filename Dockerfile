FROM python:alpine 

COPY src /src/
WORKDIR src

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
