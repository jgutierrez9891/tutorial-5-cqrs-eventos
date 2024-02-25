from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.dto import DTO

#@dataclass(frozen=True)
class ContratoDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    direccion: str = field(default_factory=str)
    telefono: int = field(default_factory=str)
    fecha_inicio: str = field(default_factory=str)
    fecha_fin: str = field(default_factory=str)
    arrendatario: str = field(default_factory=str)
    inquilino: str = field(default_factory=str)
    monto: float = field(default_factory=str)