FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY division_service.py division_service.py

EXPOSE 5004

CMD ["python", "division_service.py"]
