FROM python:3
COPY ./app.py .
RUN pip install flask
EXPOSE 8080
ENTRYPOINT  [ "python3" , "./app.py" ]
