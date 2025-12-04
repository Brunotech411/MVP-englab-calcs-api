from fastapi import FastAPI
from app.routers import health, electrical, flow

app = FastAPI(
    title="EngLab Calcs API",
    description="API de cálculos para automação/engenharia",
    version="0.1.0",
)


@app.get("/")
def root():
    return {"message": "EngLab Calcs API - OK"}


# Incluindo as rotas dos módulos
app.include_router(health.router)
app.include_router(electrical.router)
app.include_router(flow.router)
