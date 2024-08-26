FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY multiplication_service.py multiplication_service.py

EXPOSE 5003

CMD ["python", "multiplication_service.py"]
