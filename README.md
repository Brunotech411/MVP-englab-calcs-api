# EngLab Calcs API

API de cálculos utilizados em automação/engenharia, projetada como um **microserviço independente**, simples e de alta coesão.  
Este serviço fornece cálculos de grandezas elétricas e de fluxo, servindo como backend especializado e consumido pela **Orchestrator API**.

---

## 📌 Arquitetura

A Calcs API segue:

- **FastAPI** para alta performance  
- **Arquitetura modular** por domínio  
- **Pydantic** para validação segura de entrada  
- Serviço totalmente _stateless_ e independente  

---

## 📁 Estrutura de diretórios

```
MVP-englab-calcs-api/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── electrical.py
│   │   ├── flow.py
│   │   └── health.py
│   └── __init__.py
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🚀 Como rodar localmente

### 1. Criar ambiente virtual

```bash
python -m venv venv
./venv/Scripts/activate
```

### 2. Instalar dependências

```bash
pip install -r requirements.txt
```

### 3. Rodar servidor

```bash
uvicorn app.main:app --reload --port 8000
```

Acesse Swagger:  
👉 **http://127.0.0.1:8000/docs**

---

## 🧮 Endpoints principais

### 🔌 Corrente trifásica  
`POST /electrical/three_phase_current`

### 🌊 Velocidade de fluxo  
`POST /flow/velocity`

### 🔍 Número de Reynolds  
`POST /flow/reynolds`

---

## 🐳 Docker

### Build

```bash
docker build -t englab-calcs-api .
```

### Run

```bash
docker run -p 8000:8000 englab-calcs-api
```

---

## 🎯 Objetivo

Este microserviço fornece cálculos de engenharia isolados, servindo como componente reutilizável em arquiteturas maiores.


