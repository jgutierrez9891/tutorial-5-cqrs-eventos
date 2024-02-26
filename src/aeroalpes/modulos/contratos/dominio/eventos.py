from __future__ import annotations
from dataclasses import dataclass, field
from aeroalpes.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class ContratoCreado(EventoDominio):
    id_contrato: int = None
    estado: str = None
    fecha_creacion: datetime = None
    
""" @dataclass
class ContratoFirmado(EventoDominio):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None

@dataclass
class ContratoProcesado(EventoDominio):
    id_reserva: uuid.UUID = None
    fecha_actualizacion: datetime = None """