from fastapi import FastAPI, Depends,HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from db.conexion import collection,db
from passlib.context import CryptContext
from db.hashear_pass import contraseña_hasheada, contraseña_plana


sec_app = APIRouter()
oauth2_scheme = OAuth2PasswordBearer("/token")


class user(BaseModel):
    username: str
    password: str


async def obtener_usuario(username: str):
    usuario = await collection.find_one({"username": username})
   
    return usuario




pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




def verificar_contraseña(contraseña_plana, contraseña_hasheada):
    return pwd_context.verify(contraseña_plana, contraseña_hasheada)
#


@sec_app.post("/token", tags=["Login"])
async def verificar(form_data: OAuth2PasswordRequestForm = Depends()):
    usuario = await obtener_usuario(form_data.username)
    if not usuario or not verificar_contraseña(form_data.password, usuario["password"]):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")

#def login(form_data: OAuth2PasswordRequestForm= Depends()):
 #      user =users_db.get(form_data.username)
  #     if not user:
   #           raise HTTPException(status_code=400, detail="Contraseña o usuario invalidos")
    #   if not form_data.password == user["hashed_password"]:
     #         raise HTTPException(status_code=400, detail="Contraseña o usuario invalidos")
      # return {
       #       "access_token": "TalentInHouse",
        #      "token_type": "bearer"

       #}



users_db = {
    "edermen": {
        "username": "Edermen24",
        "hashed_password": "fastAPI",
        "disabled": False,
    }
}







