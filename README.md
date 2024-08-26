# multi-container-demo
A demo backend api  of a calculator that can do addition, subtraction, multiplication, division. 
This backend app is being deployed as micro service for all the different operations

** Ignore initial-code folder **

# folder structure

# Calculator App Structure

```plaintext
Calculator-App/
├── main/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── services/
│   ├── addition/
│   │   ├── Dockerfile
│   │   ├── addition_service.py
│   │   └── requirements.txt
│   ├── division/
│   │   ├── Dockerfile
│   │   ├── division_service.py
│   │   └── requirements.txt
│   ├── multiplication/
│   │   ├── Dockerfile
│   │   ├── multiplication_service.py
│   │   └── requirements.txt
│   └── subtraction/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── substraction_service.py
└── docker-compose.yml
```

