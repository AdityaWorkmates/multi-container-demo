FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY substraction_service.py substraction_service.py

EXPOSE 5002

CMD ["python", "substraction_service.py"]
