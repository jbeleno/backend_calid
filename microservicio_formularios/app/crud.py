from sqlalchemy.orm import Session
from . import models, schemas

def get_formularios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Formulario).offset(skip).limit(limit).all()

def get_formulario(db: Session, formulario_id: int):
    return db.query(models.Formulario).filter(models.Formulario.id_formulario == formulario_id).first()

def create_formulario(db: Session, formulario: schemas.FormularioCreate):
    db_formulario = models.Formulario(**formulario.dict())
    db.add(db_formulario)
    db.commit()
    db.refresh(db_formulario)
    return db_formulario

def update_formulario(db: Session, formulario_id: int, formulario_update: schemas.FormularioCreate):
    formulario = db.query(models.Formulario).filter(models.Formulario.id_formulario == formulario_id).first()
    if formulario:
        for key, value in formulario_update.dict().items():
            setattr(formulario, key, value)
        db.commit()
        db.refresh(formulario)
    return formulario

def delete_formulario(db: Session, formulario_id: int):
    formulario = db.query(models.Formulario).filter(models.Formulario.id_formulario == formulario_id).first()
    if formulario:
        db.delete(formulario)
        db.commit()
    return formulario

# Objetivos

def get_objetivos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ObjetivoFormulario).offset(skip).limit(limit).all()

def get_objetivo(db: Session, objetivo_id: int):
    return db.query(models.ObjetivoFormulario).filter(models.ObjetivoFormulario.id_objetivo == objetivo_id).first()

def create_objetivo(db: Session, objetivo: schemas.ObjetivoFormularioCreate):
    db_objetivo = models.ObjetivoFormulario(**objetivo.dict())
    db.add(db_objetivo)
    db.commit()
    db.refresh(db_objetivo)
    return db_objetivo

def update_objetivo(db: Session, objetivo_id: int, objetivo_update: schemas.ObjetivoFormularioCreate):
    objetivo = db.query(models.ObjetivoFormulario).filter(models.ObjetivoFormulario.id_objetivo == objetivo_id).first()
    if objetivo:
        for key, value in objetivo_update.dict().items():
            setattr(objetivo, key, value)
        db.commit()
        db.refresh(objetivo)
    return objetivo

def delete_objetivo(db: Session, objetivo_id: int):
    objetivo = db.query(models.ObjetivoFormulario).filter(models.ObjetivoFormulario.id_objetivo == objetivo_id).first()
    if objetivo:
        db.delete(objetivo)
        db.commit()
    return objetivo

# Participantes

def get_participantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ParticipanteFormulario).offset(skip).limit(limit).all()

def get_participante(db: Session, participante_id: int):
    return db.query(models.ParticipanteFormulario).filter(models.ParticipanteFormulario.id_participante == participante_id).first()

def create_participante(db: Session, participante: schemas.ParticipanteFormularioCreate):
    db_participante = models.ParticipanteFormulario(**participante.dict())
    db.add(db_participante)
    db.commit()
    db.refresh(db_participante)
    return db_participante

def update_participante(db: Session, participante_id: int, participante_update: schemas.ParticipanteFormularioCreate):
    participante = db.query(models.ParticipanteFormulario).filter(models.ParticipanteFormulario.id_participante == participante_id).first()
    if participante:
        for key, value in participante_update.dict().items():
            setattr(participante, key, value)
        db.commit()
        db.refresh(participante)
    return participante

def delete_participante(db: Session, participante_id: int):
    participante = db.query(models.ParticipanteFormulario).filter(models.ParticipanteFormulario.id_participante == participante_id).first()
    if participante:
        db.delete(participante)
        db.commit()
    return participante
