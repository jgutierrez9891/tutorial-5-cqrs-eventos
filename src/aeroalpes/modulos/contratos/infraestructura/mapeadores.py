""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from aeroalpes.seedwork.dominio.repositorios import Mapeador
from aeroalpes.modulos.contratos.dominio.objetos_valor import Direccion, Telefono, Fecha_inicio, Fecha_fin, Arrendatario, Inquilino, Monto
from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from .dto import Contrato as ContratoDTO

class MapeadorContrato(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Contrato.__class__

    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
        
        contrato_dto = ContratoDTO()
        contrato_dto.fecha_creacion = entidad.fecha_creacion
        contrato_dto.fecha_actualizacion = entidad.fecha_actualizacion
        contrato_dto.id = str(entidad.id)
        contrato_dto.direccion = str(entidad.direccion)
        contrato_dto.telefono = int(entidad.telefono) 
        contrato_dto.fecha_inicio = str(entidad.fecha_inicio) 
        contrato_dto.fecha_fin = str(entidad.fecha_fin)
        contrato_dto.arrendatario = str(entidad.arrendatario)
        contrato_dto.inquilino = str(entidad.inquilino) 
        contrato_dto.monto = float(entidad.monto)

        return contrato_dto

    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        contrato = Contrato(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        contrato.direccion = dto.direccion
        contrato.telefono = dto.telefono
        contrato.fecha_inicio = dto.fecha_inicio
        contrato.fecha_fin = dto.fecha_fin
        contrato.arrendatario = dto.arrendatario
        contrato.inquilino = dto.inquilino
        contrato.monto = dto.monto
        
        return contrato