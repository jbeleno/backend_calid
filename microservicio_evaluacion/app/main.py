from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import engine, SessionLocal
from .models import Base
from . import crud, schemas, models  # <--- AGREGA ESTO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:5173"],  # O ["*"] solo para pruebas
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)

# Dependencia para obtener la sesión de base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["root"])
def read_root():
    return {"msg": "Microservicio de Evaluación funcionando"}

# CRUD Parámetros
@app.post("/parametros/", response_model=schemas.Parametro, tags=["parametros"])
def create_parametro(parametro: schemas.ParametroCreate, db: Session = Depends(get_db)):
    return crud.create_parametro(db, parametro)

@app.get("/parametros/", response_model=list[schemas.Parametro], tags=["parametros"])
def read_parametros(skip: int = 0, limit: int = 100, id_formulario: int = None, db: Session = Depends(get_db)):
    query = db.query(models.Parametro)
    if id_formulario is not None:
        query = query.filter(models.Parametro.id_formulario == id_formulario)
    return query.offset(skip).limit(limit).all()

@app.get("/parametros/{parametro_id}", response_model=schemas.Parametro, tags=["parametros"])
def read_parametro(parametro_id: int, db: Session = Depends(get_db)):
    db_parametro = crud.get_parametro(db, parametro_id=parametro_id)
    if db_parametro is None:
        raise HTTPException(status_code=404, detail="Parámetro no encontrado")
    return db_parametro

@app.put("/parametros/{parametro_id}", response_model=schemas.Parametro, tags=["parametros"])
def update_parametro(parametro_id: int, parametro: schemas.ParametroCreate, db: Session = Depends(get_db)):
    db_parametro = crud.update_parametro(db, parametro_id, parametro)
    if db_parametro is None:
        raise HTTPException(status_code=404, detail="Parámetro no encontrado")
    return db_parametro

@app.delete("/parametros/{parametro_id}", response_model=schemas.Parametro, tags=["parametros"])
def delete_parametro(parametro_id: int, db: Session = Depends(get_db)):
    db_parametro = crud.delete_parametro(db, parametro_id)
    if db_parametro is None:
        raise HTTPException(status_code=404, detail="Parámetro no encontrado")
    return db_parametro

# CRUD Parámetros Predeterminados
@app.post("/parametros_predeterminados/", response_model=schemas.ParametroPredeterminado, tags=["parametros_predeterminados"])
def create_parametro_predeterminado(parametro_predeterminado: schemas.ParametroPredeterminadoCreate, db: Session = Depends(get_db)):
    return crud.create_parametro_predeterminado(db, parametro_predeterminado)

@app.get("/parametros_predeterminados/", response_model=list[schemas.ParametroPredeterminado], tags=["parametros_predeterminados"])
def read_parametros_predeterminados(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_parametros_predeterminados(db, skip=skip, limit=limit)

@app.get("/parametros_predeterminados/{parametro_predeterminado_id}", response_model=schemas.ParametroPredeterminado, tags=["parametros_predeterminados"])
def read_parametro_predeterminado(parametro_predeterminado_id: int, db: Session = Depends(get_db)):
    db_parametro_predeterminado = crud.get_parametro_predeterminado(db, parametro_predeterminado_id=parametro_predeterminado_id)
    if db_parametro_predeterminado is None:
        raise HTTPException(status_code=404, detail="Parámetro predeterminado no encontrado")
    return db_parametro_predeterminado

@app.put("/parametros_predeterminados/{parametro_predeterminado_id}", response_model=schemas.ParametroPredeterminado, tags=["parametros_predeterminados"])
def update_parametro_predeterminado(parametro_predeterminado_id: int, parametro_predeterminado: schemas.ParametroPredeterminadoCreate, db: Session = Depends(get_db)):
    db_parametro_predeterminado = crud.update_parametro_predeterminado(db, parametro_predeterminado_id, parametro_predeterminado)
    if db_parametro_predeterminado is None:
        raise HTTPException(status_code=404, detail="Parámetro predeterminado no encontrado")
    return db_parametro_predeterminado

@app.delete("/parametros_predeterminados/{parametro_predeterminado_id}", response_model=schemas.ParametroPredeterminado, tags=["parametros_predeterminados"])
def delete_parametro_predeterminado(parametro_predeterminado_id: int, db: Session = Depends(get_db)):
    db_parametro_predeterminado = crud.delete_parametro_predeterminado(db, parametro_predeterminado_id)
    if db_parametro_predeterminado is None:
        raise HTTPException(status_code=404, detail="Parámetro predeterminado no encontrado")
    return db_parametro_predeterminado

# CRUD Preguntas
@app.post("/preguntas/", response_model=schemas.Pregunta, tags=["preguntas"])
def create_pregunta(pregunta: schemas.PreguntaCreate, db: Session = Depends(get_db)):
    return crud.create_pregunta(db, pregunta)

@app.get("/preguntas/", response_model=list[schemas.Pregunta], tags=["preguntas"])
def read_preguntas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_preguntas(db, skip=skip, limit=limit)

@app.get("/preguntas/parametro/{id_parametro}", response_model=list[schemas.Pregunta], tags=["preguntas"])
def read_preguntas_por_parametro(id_parametro: int, db: Session = Depends(get_db)):
    preguntas = db.query(models.Pregunta).filter(models.Pregunta.id_parametro == id_parametro).all()
    return preguntas

@app.get("/preguntas/{pregunta_id}", response_model=schemas.Pregunta, tags=["preguntas"])
def read_pregunta(pregunta_id: int, db: Session = Depends(get_db)):
    db_pregunta = crud.get_pregunta(db, pregunta_id=pregunta_id)
    if db_pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return db_pregunta

@app.put("/preguntas/{pregunta_id}", response_model=schemas.Pregunta, tags=["preguntas"])
def update_pregunta(pregunta_id: int, pregunta: schemas.PreguntaCreate, db: Session = Depends(get_db)):
    db_pregunta = crud.update_pregunta(db, pregunta_id, pregunta)
    if db_pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return db_pregunta

@app.delete("/preguntas/{pregunta_id}", response_model=schemas.Pregunta, tags=["preguntas"])
def delete_pregunta(pregunta_id: int, db: Session = Depends(get_db)):
    db_pregunta = crud.delete_pregunta(db, pregunta_id)
    if db_pregunta is None:
        raise HTTPException(status_code=404, detail="Pregunta no encontrada")
    return db_pregunta

# CRUD Preguntas Predeterminadas
@app.post("/preguntas_predeterminadas/", response_model=schemas.PreguntaPredeterminada, tags=["preguntas_predeterminadas"])
def create_pregunta_predeterminada(pregunta_predeterminada: schemas.PreguntaPredeterminadaCreate, db: Session = Depends(get_db)):
    return crud.create_pregunta_predeterminada(db, pregunta_predeterminada)

@app.get("/preguntas_predeterminadas/", response_model=list[schemas.PreguntaPredeterminada], tags=["preguntas_predeterminadas"])
def read_preguntas_predeterminadas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_preguntas_predeterminadas(db, skip=skip, limit=limit)

@app.get("/preguntas_predeterminadas/{pregunta_predeterminada_id}", response_model=schemas.PreguntaPredeterminada, tags=["preguntas_predeterminadas"])
def read_pregunta_predeterminada(pregunta_predeterminada_id: int, db: Session = Depends(get_db)):
    db_pregunta_predeterminada = crud.get_pregunta_predeterminada(db, pregunta_predeterminada_id=pregunta_predeterminada_id)
    if db_pregunta_predeterminada is None:
        raise HTTPException(status_code=404, detail="Pregunta predeterminada no encontrada")
    return db_pregunta_predeterminada

@app.put("/preguntas_predeterminadas/{pregunta_predeterminada_id}", response_model=schemas.PreguntaPredeterminada, tags=["preguntas_predeterminadas"])
def update_pregunta_predeterminada(pregunta_predeterminada_id: int, pregunta_predeterminada: schemas.PreguntaPredeterminadaCreate, db: Session = Depends(get_db)):
    db_pregunta_predeterminada = crud.update_pregunta_predeterminada(db, pregunta_predeterminada_id, pregunta_predeterminada)
    if db_pregunta_predeterminada is None:
        raise HTTPException(status_code=404, detail="Pregunta predeterminada no encontrada")
    return db_pregunta_predeterminada

@app.delete("/preguntas_predeterminadas/{pregunta_predeterminada_id}", response_model=schemas.PreguntaPredeterminada, tags=["preguntas_predeterminadas"])
def delete_pregunta_predeterminada(pregunta_predeterminada_id: int, db: Session = Depends(get_db)):
    db_pregunta_predeterminada = crud.delete_pregunta_predeterminada(db, pregunta_predeterminada_id)
    if db_pregunta_predeterminada is None:
        raise HTTPException(status_code=404, detail="Pregunta predeterminada no encontrada")
    return db_pregunta_predeterminada
