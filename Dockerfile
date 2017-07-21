FROM python
COPY ./requirements.txt /app/
RUN pip install -r /app/requirements.txt
COPY . /app
RUN nosetests /app/tests
CMD python /app/main.py
