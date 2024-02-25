from aeroalpes.seedwork.aplicacion.dto import Mapeador as AppMap
from aeroalpes.seedwork.dominio.repositorios import Mapeador as RepMap
from aeroalpes.modulos.contratos.dominio.entidades import Contrato
from aeroalpes.modulos.contratos.dominio.objetos_valor import Direccion, Telefono, Fecha_inicio, Fecha_fin, Arrendatario, Inquilino, Monto
from .dto import ContratoDTO

from datetime import datetime

class MapeadorContratoDTOJson(AppMap):
    """ def _procesar_itinerario(self, itinerario: dict) -> ItinerarioDTO:
        odos_dto: list[OdoDTO] = list()
        for odo in itinerario.get('odos', list()):

            segmentos_dto: list[SegmentoDTO] = list()
            for segmento in odo.get('segmentos', list()):
                legs_dto: list[LegDTO] = list()
                for leg in segmento.get('legs', list()):
                    leg_dto: LegDTO = LegDTO(leg.get('fecha_salida'), leg.get('fecha_llegada'), leg.get('origen'), leg.get('destino')) 
                    legs_dto.append(leg_dto)  
                
                segmentos_dto.append(SegmentoDTO(legs_dto))
            
            odos_dto.append(Odo(segmentos_dto))

        return ItinerarioDTO(odos_dto) """
    
    def externo_a_dto(self, externo: dict) -> ContratoDTO:
        contrato_dto = ContratoDTO()

        """ itinerarios: list[ItinerarioDTO] = list()
        for itin in externo.get('itinerarios', list()):
            reserva_dto.itinerarios.append(self._procesar_itinerario(itin)) """

        return contrato_dto

    def dto_a_externo(self, dto: ContratoDTO) -> dict:
        return dto.__dict__

class MapeadorContrato(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    """ def _procesar_itinerario(self, itinerario_dto: ItinerarioDTO) -> Itinerario:
        odos = list()

        for odo_dto in itinerario_dto.odos:
            segmentos = list()
            for seg_dto in odo_dto.segmentos:
                
                legs = list()

                for leg_dto in seg_dto.legs:
                    destino = Aeropuerto(codigo=leg_dto.destino.get('codigo'), nombre=leg_dto.destino.get('nombre'))
                    origen = Aeropuerto(codigo=leg_dto.origen.get('codigo'), nombre=leg_dto.origen.get('nombre'))
                    fecha_salida = datetime.strptime(leg_dto.fecha_salida, self._FORMATO_FECHA)
                    fecha_llegada = datetime.strptime(leg_dto.fecha_llegada, self._FORMATO_FECHA)

                    leg: Leg = Leg(fecha_salida, fecha_llegada, origen, destino)

                    legs.append(leg)

                segmentos.append(Segmento(legs))
            
            odos.append(Odo(segmentos))

        return Itinerario(odos) """

    def obtener_tipo(self) -> type:
        return Contrato.__class__

    """ def locacion_a_dict(self, locacion):
        if not locacion:
            return dict(codigo=None, nombre=None, fecha_actualizacion=None, fecha_creacion=None)
        
        return dict(
                    codigo=locacion.codigo
                ,   nombre=locacion.nombre
                ,   fecha_actualizacion=locacion.fecha_actualizacion.strftime(self._FORMATO_FECHA)
                ,   fecha_creacion=locacion.fecha_creacion.strftime(self._FORMATO_FECHA)
        ) """
        

    def entidad_a_dto(self, entidad: Contrato) -> ContratoDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)
        direccion = str(entidad.direccion)
        telefono = int(entidad.telefono) 
        fecha_inicio = str(entidad.fecha_inicio) 
        fecha_fin = str(entidad.fecha_fin)
        arrendatario = str(entidad.arrendatario)
        inquilino = str(entidad.inquilino) 
        monto = float(entidad.monto)
        
        return ContratoDTO(fecha_creacion, fecha_actualizacion, _id, direccion, telefono, fecha_inicio, fecha_fin, arrendatario, inquilino, monto)

    def dto_a_entidad(self, dto: ContratoDTO) -> Contrato:
        contrato = Contrato()

        contrato.direccion = dto.direccion
        contrato.telefono = dto.telefono
        contrato.fecha_inicio = dto.fecha_inicio
        contrato.fecha_fin = dto.fecha_fin
        contrato.arrendatario = dto.arrendatario
        contrato.inquilino = dto.inquilino
        contrato.monto = dto.monto
        
        return contrato



