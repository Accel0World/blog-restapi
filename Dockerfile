FROM python:3.10.8

WORKDIR /app

COPY api/requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 4300

COPY ./api/app /app/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4300"]