"""DTOs para la capa de infrastructura del dominio de contratos

En este archivo usted encontrará los DTOs (modelos anémicos) de
la infraestructura del dominio de contratos

"""

from aeroalpes.config.db import db
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

Base = db.declarative_base()

class Contrato(db.Model):
    __tablename__ = "contratos"
    id = db.Column(db.String, primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=False)
    fecha_actualizacion = db.Column(db.DateTime, nullable=False)
    direccion = db.Column(db.String, nullable=False)
    telefono = db.Column(db.Int, nullable=False)
    fecha_inicio = db.Column(db.DateTime, nullable=False)
    fecha_fin = db.Column(db.DateTime, nullable=False)
    arrendatario = db.Column(db.String, nullable=False)
    inquilino = db.Column(db.String, nullable=False)
    monto = db.Column(db.Integer, nullable=False)