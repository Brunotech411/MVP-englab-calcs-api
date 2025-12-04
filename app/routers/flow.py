from fastapi import APIRouter
from pydantic import BaseModel, Field

router = APIRouter(prefix="/flow", tags=["flow"])


class VelocityRequest(BaseModel):
    flow_m3_h: float = Field(..., gt=0, description="Vazão em m³/h")
    diameter_mm: float = Field(..., gt=0, description="Diâmetro interno em mm")


class VelocityResponse(BaseModel):
    velocity_m_s: float
    flow_m3_h: float
    diameter_mm: float


@router.post("/velocity", response_model=VelocityResponse)
def calculate_velocity(body: VelocityRequest):
    """
    Calcula velocidade média no tubo:
    Q = v * A  => v = Q / A
    Q em m³/s, D em m.
    """
    import math

    flow_m3_s = body.flow_m3_h / 3600.0
    diameter_m = body.diameter_mm / 1000.0
    area = math.pi * (diameter_m**2) / 4
    velocity = flow_m3_s / area

    return VelocityResponse(
        velocity_m_s=velocity,
        flow_m3_h=body.flow_m3_h,
        diameter_mm=body.diameter_mm,
    )


class ReynoldsRequest(BaseModel):
    velocity_m_s: float = Field(..., gt=0)
    diameter_mm: float = Field(..., gt=0)
    kinematic_viscosity_m2_s: float = Field(
        ..., gt=0, description="Viscosidade cinemática em m²/s"
    )


class ReynoldsResponse(BaseModel):
    reynolds: float
    regime: str


@router.post("/reynolds", response_model=ReynoldsResponse)
def calculate_reynolds(body: ReynoldsRequest):
    """
    Re = v * D / ν
    """
    diameter_m = body.diameter_mm / 1000.0
    re = (body.velocity_m_s * diameter_m) / body.kinematic_viscosity_m2_s

    if re < 2300:
        regime = "laminar"
    elif re < 4000:
        regime = "transição"
    else:
        regime = "turbulento"

    return ReynoldsResponse(reynolds=re, regime=regime)
