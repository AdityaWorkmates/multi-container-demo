FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY addition_service.py addition_service.py

EXPOSE 5001

CMD ["python", "addition_service.py"]
