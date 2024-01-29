FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=baseapi.settings

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]