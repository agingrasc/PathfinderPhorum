FROM python
COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app
WORKDIR /app
RUN nosetests /app/tests
CMD python phorum/main.py
