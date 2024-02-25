"""Entidades del dominio de vuelos

En este archivo usted encontrará las entidades del dominio de contratos

"""

from __future__ import annotations
from dataclasses import dataclass, field

import aeroalpes.modulos.contratos.dominio.objetos_valor as ov
from aeroalpes.modulos.contratos.dominio.eventos import ContratoCreado, ContratoFirmado, ContratoProcesado
from aeroalpes.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

""" @dataclass
class Aeropuerto(Locacion):
    codigo: ov.Codigo = field(default_factory=ov.Codigo)
    nombre: ov.NombreAero = field(default_factory=ov.NombreAero)

    def __str__(self) -> str:
        return self.codigo.codigo.upper()

@dataclass
class Proveedor(Entidad):
    codigo: ov.Codigo = field(default_factory=ov.Codigo)
    nombre: ov.NombreAero = field(default_factory=ov.NombreAero)
    itinerarios: list[ov.Itinerario] = field(default_factory=list[ov.Itinerario])

    def obtener_itinerarios(self, odos: list[Odo], parametros: ParametroBusca):
        return self.itinerarios

@dataclass
class Pasajero(Entidad):
    clase: ov.Clase = field(default_factory=ov.Clase)
    tipo: ov.TipoPasajero = field(default_factory=ov.TipoPasajero) """

@dataclass
class Contrato(AgregacionRaiz):
    #id: uuid.UUID = field(hash=True, default=None)
    #estado: ov.EstadoContrato = field(default=ov.EstadoContrato.PENDIENTE)
    direccion: ov.Direccion = field(hash=True, default=None)
    telefono: ov.Telefono = field(hash=True, default=None)
    fecha_inicio: ov.Fecha_inicio = field(hash=True, default=None)
    fecha_fin: ov.Fecha_fin = field(hash=True, default=None)
    arrendatario: ov.Arrendatario = field(hash=True, default=None)
    inquilino: ov.Inquilino = field(hash=True, default=None)
    monto: ov.Monto = field(hash=True, default=None)

    """ def crear_contrato(self, contrato: Contrato):
        self.id = contrato.id
        self.estado = contrato.estado
        self.telefono = contrato.telefono
        self.fecha_inicio = contrato.fecha_inicio
        self.fecha_fin = contrato.fecha_fin
        self.arrendatario = contrato.arrendatario
        self.inquilino = contrato.inquilino
        self.monto = contrato.monto

        self.agregar_evento(ContratoCreado(id_contrato=self.id, estado=self.estado.name, fecha_creacion=self.fecha_creacion))

    def firmar_contrato(self):
        self.estado = ov.EstadoContrato.FIRMADO

        self.agregar_evento(ContratoFirmado(self.id, self.fecha_actualizacion))

    def procesar_contrato(self):
        self.estado = ov.EstadoContrato.PROCESADO

        self.agregar_evento(ContratoProcesado(self.id, self.fecha_actualizacion)) """
