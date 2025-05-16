from pydantic import BaseModel

class EmpresaBase(BaseModel):
    nombre: str
    telefono: str | None = None

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id_empresa: int

    class Config:
        orm_mode = True
