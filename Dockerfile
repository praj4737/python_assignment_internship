FROM python:3-alpine3.12
WORKDIR /
COPY . /
RUN pip install flask
RUN pip install pymongo
EXPOSE 5000
CMD python ./main.py
