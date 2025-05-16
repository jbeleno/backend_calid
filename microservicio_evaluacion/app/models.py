from sqlalchemy import Column, Integer, String, Text, Float, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Parametro(Base):
    __tablename__ = "parametros"
    id_parametro = Column(Integer, primary_key=True, index=True)
    id_formulario = Column(Integer, nullable=False)
    id_parametro_predeterminado = Column(Integer)
    nombre = Column(String(255))
    descripcion = Column(Text)
    porcentaje_obtenido = Column(Float)
    porcentaje_maximo = Column(Float)

class ParametroPredeterminado(Base):
    __tablename__ = "parametros_predeterminados"
    id_parametro_predeterminado = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text)

class Pregunta(Base):
    __tablename__ = "preguntas"
    id_pregunta = Column(Integer, primary_key=True, index=True)
    id_parametro = Column(Integer, nullable=False)
    id_pregunta_predeterminada = Column(Integer)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
    valor_obtenido = Column(Float)
    valor_maximo = Column(Float)
    __table_args__ = (
        CheckConstraint('valor_obtenido >= 0 AND valor_obtenido <= 3', name='preguntas_valor_obtenido_check'),
    )

class PreguntaPredeterminada(Base):
    __tablename__ = "preguntas_predeterminadas"
    id_pregunta_predeterminada = Column(Integer, primary_key=True, index=True)
    id_parametro_predeterminado = Column(Integer, nullable=False)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=False)
