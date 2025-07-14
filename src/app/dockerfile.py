FROM python
ENV FLASK_APP=flaskr
ENV FLASK_ENV=development
RUN pip install flask
WORKDIR /src/app
COPY . .
CMD ["pip", "install", "--editable", "."]
CMD ["flask", "init-db"]
CMD ["flask", "run", "--host=0.0.0.0"]

