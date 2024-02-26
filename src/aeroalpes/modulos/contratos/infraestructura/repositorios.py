""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de vuelos

"""

from aeroalpes.config.db import db
from aeroalpes.modulos.contratos.dominio.repositorios import RepositorioContratos, RepositorioProveedores
from aeroalpes.modulos.vuelos.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from aeroalpes.modulos.contratos.dominio.fabricas import FabricaContratos
from .dto import Contrato as ContratoDTO
from .mapeadores import MapeadorContrato
from uuid import UUID

class RepositorioProveedoresSQLite(RepositorioProveedores):

    def obtener_por_id(self, id: UUID) -> Contrato:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Contrato):
        # TODO
        raise NotImplementedError

    def actualizar(self, entity: Contrato):
        # TODO
        raise NotImplementedError

    def eliminar(self, entity_id: UUID):
        # TODO
        raise NotImplementedError
    
class RepositorioContratosSQLite(RepositorioContratos):

    def __init__(self):
        self._fabrica_contratos: FabricaContratos = FabricaContratos()

    @property
    def fabrica_contratos(self):
        return self._fabrica_contratos

    def obtener_por_id(self, id: UUID) -> Contrato:
        contrato_dto = db.session.query(ContratoDTO).filter_by(id=str(id)).one()
        return self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())

    def obtener_todos(self) -> list[Contrato]:
        # TODO
        raise NotImplementedError

    def agregar(self, contrato: Contrato):
        contrato_dto = self.fabrica_contratos.crear_objeto(contrato, MapeadorContrato())
        print("contrato-sqlite")
        print(contrato_dto)
        db.session.add(contrato_dto)

    def actualizar(self, contrato: Contrato):
        # TODO
        raise NotImplementedError

    def eliminar(self, contrato_id: UUID):
        # TODO
        raise NotImplementedError