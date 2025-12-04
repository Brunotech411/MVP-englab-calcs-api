from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/electrical", tags=["electrical"])


class ThreePhaseCurrentRequest(BaseModel):
    power_kw: float = Field(..., gt=0, description="Potência em kW")
    voltage_v: float = Field(..., gt=0, description="Tensão linha-linha em V")
    power_factor: float = Field(
        0.8, ge=0, le=1, description="Fator de potência (0 a 1)"
    )


class ThreePhaseCurrentResponse(BaseModel):
    current_a: float
    power_kw: float
    voltage_v: float
    power_factor: float


@router.post("/three_phase_current", response_model=ThreePhaseCurrentResponse)
def calculate_three_phase_current(body: ThreePhaseCurrentRequest):
    """
    Calcula corrente trifásica aproximada:
    I = P / (√3 * V * FP)
    """
    from math import sqrt

    current_a = body.power_kw * 1000 / (sqrt(3) * body.voltage_v * body.power_factor)

    return ThreePhaseCurrentResponse(
        current_a=current_a,
        power_kw=body.power_kw,
        voltage_v=body.voltage_v,
        power_factor=body.power_factor,
    )
