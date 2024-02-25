from aeroalpes.seedwork.aplicacion.comandos import Comando
from aeroalpes.modulos.contratos.aplicacion.dto import ContratoDTO
from .base import CrearContratoBaseHandler
from dataclasses import dataclass, field
from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando as comando

from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from aeroalpes.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from aeroalpes.modulos.contratos.aplicacion.mapeadores import MapeadorContrato
from aeroalpes.modulos.contratos.infraestructura.repositorios import RepositorioContratos

@dataclass
class CrearContrato(Comando):
    fecha_creacion: str
    fecha_actualizacion: str
    id: str

class CrearContratoHandler(CrearContratoBaseHandler):
    
    def handle(self, comando: CrearContrato):
        contrato_dto = ContratoDTO(
                fecha_actualizacion=comando.fecha_actualizacion
            ,   fecha_creacion=comando.fecha_creacion
            ,   id=comando.id)

        contrato: Contrato = self.fabrica_contratos.crear_objeto(contrato_dto, MapeadorContrato())
        contrato.crear_contrato(contrato)

        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioContratos.__class__)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, contrato)
        UnidadTrabajoPuerto.savepoint()
        UnidadTrabajoPuerto.commit()


@comando.register(CrearContrato)
def ejecutar_comando_crear_contrato(comando: CrearContrato):
    handler = CrearContratoHandler()
    handler.handle(comando)
    