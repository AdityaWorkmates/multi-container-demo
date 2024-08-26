# multi-container-demo
A demo backend api  of a calculator that can do addition, subtraction, multiplication, division. 
This backend app is being deployed as micro service for all the different operations

** Ignore initial-code folder **

# folder structure

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

first
```bash
cd calculator-app
```
then
to compose the images and run all container
```bash
docker-compose up --build
```


then to test
API - http://127.0.0.1:5000/calculate

## for addition
request syntax
```json
{
  "operation":"add",
  "first_number":11,
  "second_number":10
}
```

response
```json
{
  "result":21
}
```

## for subtraction
request syntax
```json
{
  "operation":"sub",
  "first_number":11,
  "second_number":10
}
```

response
```json
{
  "result":1
}
```

## for multiplication
request syntax
```json
{
  "operation":"mul",
  "first_number":11,
  "second_number":10
}
```

response
```json
{
  "result":110
}
```

## for division
request syntax
```json
{
  "operation":"div",
  "first_number":11,
  "second_number":10
}
```

response
```json
{
  "result":1.1
}
```


