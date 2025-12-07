# EngLab Calcs API

API de cálculos utilizados em automação/engenharia, projetada como um **microserviço independente**, simples e de alta coesão.  
Este serviço fornece cálculos de grandezas elétricas e de fluxo, servindo como backend especializado e consumido pela **EngLab Orchestrator API**.

---

## 🎯 Funcionalidades

### 🔌 Corrente trifásica

**Fórmula aproximada:**

```text
I = P / (√3 × V × FP)
```

Onde:

- `I` = corrente em ampères (A)  
- `P` = potência ativa em kW  
- `V` = tensão de linha em volts (V)  
- `FP` = fator de potência (adimensional)

> Aplicação: dimensionamento de cabos, disjuntores e análise de carga em sistemas trifásicos.

---

### 🌊 Velocidade do fluxo

```text
v = Q / A
```

Onde:

- `v` = velocidade do fluido (m/s)  
- `Q` = vazão volumétrica (m³/s)  
- `A` = área interna da tubulação (m²)

> Aplicação: verificar faixas de velocidade adequadas em tubulações (evitar erosão, ruído, cavitação) e validar medições de instrumentos de vazão.

---

### 🔍 Número de Reynolds

```text
Re = (ρ × v × D) / μ
```

Onde:

- `Re` = número de Reynolds (adimensional)  
- `ρ` = densidade do fluido (kg/m³)  
- `v` = velocidade (m/s)  
- `D` = diâmetro interno da tubulação (m)  
- `μ` = viscosidade dinâmica (Pa·s ou kg/(m·s))

> Aplicação: classificar se o escoamento é **laminar**, **de transição** ou **turbulento**, conceito chave em mecânica dos fluidos e projetos de instrumentação/automação.

---

## 📌 Arquitetura

A **EngLab Calcs API** segue:

- **FastAPI** como framework web (alta performance e documentação automática via Swagger).  
- **Arquitetura modular por domínio** (`electrical`, `flow`, `health`).  
- **Pydantic** para validação e tipagem dos dados de entrada.  
- Serviço totalmente **stateless** e independente, ideal para compor arquiteturas de microsserviços.

Este serviço é consumido pela **EngLab Orchestrator API**, que registra as conversões em banco de dados e integra com a API de clima.

---

## 📁 Estrutura de diretórios

```text
MVP-englab-calcs-api/
├── app/
│   ├── main.py              # Criação da aplicação FastAPI
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── electrical.py    # Rotas de cálculos elétricos
│   │   ├── flow.py          # Rotas de cálculos de vazão / Reynolds
│   │   └── health.py        # Health check da API
│   └── __init__.py
├── .dockerignore
├── .gitattributes
├── .gitignore
├── Dockerfile               # Definição da imagem Docker da Calcs API
├── README.md
└── requirements.txt         # Dependências Python
```

---

## 🚀 Como rodar localmente (sem Docker)

> Recomendado para inspecionar o código e testar a API diretamente no ambiente Python.  
> Testado com **Python 3.11**.

### 1️⃣ Criar e ativar ambiente virtual

No Windows (PowerShell):

```bash
python -m venv venv
.venv\Scriptsactivate
```

> Em sistemas Unix-like (opcional para referência):  
> `python3 -m venv venv && source venv/bin/activate`

### 2️⃣ Instalar dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Subir o servidor FastAPI (Uvicorn)

```bash
uvicorn app.main:app --reload --port 8000
```

Depois de iniciado, os endpoints podem ser testados via Swagger UI:

👉 **http://127.0.0.1:8000/docs**

---

## 🐳 Rodando com Docker (standalone)

> Esta opção é útil para rodar **apenas** a Calcs API isoladamente.  
> Em contexto de projeto completo, a execução recomendada é via `docker compose` no repositório raiz.

### 1️⃣ Build da imagem

No diretório `MVP-englab-calcs-api`:

```bash
docker build -t englab-calcs-api .
```

### 2️⃣ Subir o container

```bash
docker run --rm -p 8000:8000 englab-calcs-api
```

Acesse:

👉 **http://127.0.0.1:8000/docs**

---

## 🧩 Uso em conjunto com Orchestrator (via docker-compose)

Quando o projeto é iniciado a partir do repositório raiz com:

```bash
docker compose up --build
```

- A **EngLab Calcs API** sobe automaticamente como serviço `englab-calcs-api` na porta `8000`.  
- A **EngLab Orchestrator API** consome esta API internamente, usando o nome do serviço Docker e a variável de ambiente:

```text
CALCS_API_URL=http://englab-calcs-api:8000
```

---

## 🧮 Endpoints principais

### 🔌 Corrente trifásica  
`POST /electrical/three_phase_current`

Exemplo:

```json
{
  "power_kw": 50,
  "voltage_v": 440,
  "power_factor": 0.85
}
```

### 🌊 Velocidade de fluxo  
`POST /flow/velocity`

```json
{
  "flow_m3_h": 300,
  "diameter_mm": 150
}
```

### 🔍 Número de Reynolds  
`POST /flow/reynolds`

```json
{
  "density_kg_m3": 1000,
  "velocity_m_s": 3.0,
  "diameter_m": 0.15,
  "dynamic_viscosity_pa_s": 0.001
}
```

---

## 🎯 Objetivo

Este microserviço ilustra:

- **Separação de responsabilidades** em uma arquitetura de microsserviços.
- Encapsulamento de **regras de negócio de engenharia** em um serviço simples, reusável e independente.
- Como um serviço especializado pode ser **consumido por um orquestrador**, que agrega dados de domínio (clima, banco de dados, histórico de conversões).

Ele pode ser reutilizado em outros projetos que demandem cálculos de corrente trifásica, escoamento em tubulações ou regime de fluxo em sistemas industriais.
