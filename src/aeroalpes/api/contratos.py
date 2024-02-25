import aeroalpes.seedwork.presentacion.api as api
import json
from aeroalpes.modulos.contratos.aplicacion.servicios import ServicioContrato
from aeroalpes.modulos.vuelos.aplicacion.dto import ReservaDTO
from aeroalpes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from aeroalpes.modulos.contratos.aplicacion.mapeadores import MapeadorContratoDTOJson
#from aeroalpes.modulos.contratos.aplicacion.comandos.crear_contrato import CrearContrato
#from aeroalpes.modulos.contratos.aplicacion.queries.obtener_contrato import ObtenerContrato
#from aeroalpes.seedwork.aplicacion.comandos import ejecutar_commando
#from aeroalpes.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('contratos', '/contratos')

@bp.route('/contrato', methods=('POST',))
def crear_contrato():
    try:
        contrato_dict = request.json

        map_contrato = MapeadorContratoDTOJson()
        contrato_dto = map_contrato.externo_a_dto(contrato_dict)

        sr = ServicioContrato()
        dto_final = sr.crear_contrato(contrato_dto)

        return map_contrato.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/contrato', methods=('GET',))
@bp.route('/contrato/<id>', methods=('GET',))
def dar_contrato(id=None):
    if id:
        sr = ServicioContrato()
        map_contrato = MapeadorContratoDTOJson()
        
        return map_contrato.dto_a_externo(sr.obtener_contrato_por_id(id))
    else:
        return [{'message': 'GET!'}]

