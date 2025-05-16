from sqlalchemy.orm import Session
from . import models, schemas

def get_parametros(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Parametro).offset(skip).limit(limit).all()

def get_parametro(db: Session, parametro_id: int):
    return db.query(models.Parametro).filter(models.Parametro.id_parametro == parametro_id).first()

def create_parametro(db: Session, parametro: schemas.ParametroCreate):
    db_parametro = models.Parametro(**parametro.dict())
    db.add(db_parametro)
    db.commit()
    db.refresh(db_parametro)
    return db_parametro

def update_parametro(db: Session, parametro_id: int, parametro_update: schemas.ParametroCreate):
    parametro = db.query(models.Parametro).filter(models.Parametro.id_parametro == parametro_id).first()
    if parametro:
        for key, value in parametro_update.dict().items():
            setattr(parametro, key, value)
        db.commit()
        db.refresh(parametro)
    return parametro

def delete_parametro(db: Session, parametro_id: int):
    parametro = db.query(models.Parametro).filter(models.Parametro.id_parametro == parametro_id).first()
    if parametro:
        db.delete(parametro)
        db.commit()
    return parametro

# Parametros Predeterminados
def get_parametros_predeterminados(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ParametroPredeterminado).offset(skip).limit(limit).all()

def get_parametro_predeterminado(db: Session, parametro_predeterminado_id: int):
    return db.query(models.ParametroPredeterminado).filter(models.ParametroPredeterminado.id_parametro_predeterminado == parametro_predeterminado_id).first()

def create_parametro_predeterminado(db: Session, parametro_predeterminado: schemas.ParametroPredeterminadoCreate):
    db_parametro_predeterminado = models.ParametroPredeterminado(**parametro_predeterminado.dict())
    db.add(db_parametro_predeterminado)
    db.commit()
    db.refresh(db_parametro_predeterminado)
    return db_parametro_predeterminado

def update_parametro_predeterminado(db: Session, parametro_predeterminado_id: int, parametro_predeterminado_update: schemas.ParametroPredeterminadoCreate):
    parametro_predeterminado = db.query(models.ParametroPredeterminado).filter(models.ParametroPredeterminado.id_parametro_predeterminado == parametro_predeterminado_id).first()
    if parametro_predeterminado:
        for key, value in parametro_predeterminado_update.dict().items():
            setattr(parametro_predeterminado, key, value)
        db.commit()
        db.refresh(parametro_predeterminado)
    return parametro_predeterminado

def delete_parametro_predeterminado(db: Session, parametro_predeterminado_id: int):
    parametro_predeterminado = db.query(models.ParametroPredeterminado).filter(models.ParametroPredeterminado.id_parametro_predeterminado == parametro_predeterminado_id).first()
    if parametro_predeterminado:
        db.delete(parametro_predeterminado)
        db.commit()
    return parametro_predeterminado

# Preguntas
def get_preguntas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pregunta).offset(skip).limit(limit).all()

def get_pregunta(db: Session, pregunta_id: int):
    return db.query(models.Pregunta).filter(models.Pregunta.id_pregunta == pregunta_id).first()

def create_pregunta(db: Session, pregunta: schemas.PreguntaCreate):
    db_pregunta = models.Pregunta(**pregunta.dict())
    db.add(db_pregunta)
    db.commit()
    db.refresh(db_pregunta)
    return db_pregunta

def update_pregunta(db: Session, pregunta_id: int, pregunta_update: schemas.PreguntaCreate):
    pregunta = db.query(models.Pregunta).filter(models.Pregunta.id_pregunta == pregunta_id).first()
    if pregunta:
        for key, value in pregunta_update.dict().items():
            setattr(pregunta, key, value)
        db.commit()
        db.refresh(pregunta)
    return pregunta

def delete_pregunta(db: Session, pregunta_id: int):
    pregunta = db.query(models.Pregunta).filter(models.Pregunta.id_pregunta == pregunta_id).first()
    if pregunta:
        db.delete(pregunta)
        db.commit()
    return pregunta

# Preguntas Predeterminadas
def get_preguntas_predeterminadas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PreguntaPredeterminada).offset(skip).limit(limit).all()

def get_pregunta_predeterminada(db: Session, pregunta_predeterminada_id: int):
    return db.query(models.PreguntaPredeterminada).filter(models.PreguntaPredeterminada.id_pregunta_predeterminada == pregunta_predeterminada_id).first()

def create_pregunta_predeterminada(db: Session, pregunta_predeterminada: schemas.PreguntaPredeterminadaCreate):
    db_pregunta_predeterminada = models.PreguntaPredeterminada(**pregunta_predeterminada.dict())
    db.add(db_pregunta_predeterminada)
    db.commit()
    db.refresh(db_pregunta_predeterminada)
    return db_pregunta_predeterminada

def update_pregunta_predeterminada(db: Session, pregunta_predeterminada_id: int, pregunta_predeterminada_update: schemas.PreguntaPredeterminadaCreate):
    pregunta_predeterminada = db.query(models.PreguntaPredeterminada).filter(models.PreguntaPredeterminada.id_pregunta_predeterminada == pregunta_predeterminada_id).first()
    if pregunta_predeterminada:
        for key, value in pregunta_predeterminada_update.dict().items():
            setattr(pregunta_predeterminada, key, value)
        db.commit()
        db.refresh(pregunta_predeterminada)
    return pregunta_predeterminada

def delete_pregunta_predeterminada(db: Session, pregunta_predeterminada_id: int):
    pregunta_predeterminada = db.query(models.PreguntaPredeterminada).filter(models.PreguntaPredeterminada.id_pregunta_predeterminada == pregunta_predeterminada_id).first()
    if pregunta_predeterminada:
        db.delete(pregunta_predeterminada)
        db.commit()
    return pregunta_predeterminada
