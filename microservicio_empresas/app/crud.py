from sqlalchemy.orm import Session
from . import models, schemas

def get_empresas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Empresa).offset(skip).limit(limit).all()

def get_empresa(db: Session, empresa_id: int):
    return db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()

def create_empresa(db: Session, empresa: schemas.EmpresaCreate):
    db_empresa = models.Empresa(nombre=empresa.nombre, telefono=empresa.telefono)
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def delete_empresa(db: Session, empresa_id: int):
    empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()
    if empresa:
        db.delete(empresa)
        db.commit()
    return empresa

def update_empresa(db: Session, empresa_id: int, empresa_update: schemas.EmpresaCreate):
    empresa = db.query(models.Empresa).filter(models.Empresa.id_empresa == empresa_id).first()
    if empresa:
        empresa.nombre = empresa_update.nombre
        empresa.telefono = empresa_update.telefono
        db.commit()
        db.refresh(empresa)
    return empresa
