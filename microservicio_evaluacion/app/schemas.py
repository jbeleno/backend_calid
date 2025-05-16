from pydantic import BaseModel, conint

class ParametroBase(BaseModel):
    id_formulario: int
    id_parametro_predeterminado: int | None = None
    nombre: str | None = None
    descripcion: str | None = None
    porcentaje_obtenido: float | None = None
    porcentaje_maximo: float | None = None

class ParametroCreate(ParametroBase):
    pass

class Parametro(ParametroBase):
    id_parametro: int
    class Config:
        orm_mode = True

class ParametroPredeterminadoBase(BaseModel):
    nombre: str
    descripcion: str | None = None

class ParametroPredeterminadoCreate(ParametroPredeterminadoBase):
    pass

class ParametroPredeterminado(ParametroPredeterminadoBase):
    id_parametro_predeterminado: int
    class Config:
        orm_mode = True

class PreguntaBase(BaseModel):
    id_parametro: int
    id_pregunta_predeterminada: int | None = None
    nombre: str
    descripcion: str
    valor_obtenido: conint(ge=0, le=3) | None = None
    valor_maximo: float | None = None

class PreguntaCreate(PreguntaBase):
    pass

class Pregunta(PreguntaBase):
    id_pregunta: int
    class Config:
        orm_mode = True

class PreguntaPredeterminadaBase(BaseModel):
    id_parametro_predeterminado: int
    nombre: str
    descripcion: str

class PreguntaPredeterminadaCreate(PreguntaPredeterminadaBase):
    pass

class PreguntaPredeterminada(PreguntaPredeterminadaBase):
    id_pregunta_predeterminada: int
    class Config:
        orm_mode = True
