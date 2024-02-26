"""Objetos valor del dominio de vuelos

En este archivo usted encontrará los objetos valor del dominio de vuelos

"""

from __future__ import annotations

from dataclasses import dataclass
from aeroalpes.seedwork.dominio.objetos_valor import Codigo
from datetime import datetime
from enum import Enum

@dataclass(frozen=True)
class Fecha_inicio():
    fecha_inicio: datetime

@dataclass(frozen=True)
class Fecha_fin():
    fecha_fin: datetime


@dataclass(frozen=True)
class Monto():
    monto: float

class EstadoContrato(str, Enum):
    PENDIENTE = "Pendiente"
    #FIRMADO = "Firmado"
    #PROCESADO = "Procesado"