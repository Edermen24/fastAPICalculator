from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pydantic import BaseModel
import pymongo 
from motor.motor_asyncio import AsyncIOMotorClient





client =  "mongodb+srv://Admin:SpsProject2024@talentinhouse.g4djaq3.mongodb.net/?retryWrites=true&w=majority"
        #"mongodb+srv://Admin:SpsProject2024@talentinhouse.g4djaq3.mongodb.net/?retryWrites=true&w=majority")

    #db = client["Accesosdb"]
    #collection = db["clientes"]



# Crea una instancia de cliente MongoDB
mongo_client = AsyncIOMotorClient(client)

# Selecciona la base de datos y la colección
db = mongo_client["Accesosdb"]
collection = db["clientes"]











# Seleccionar la base de datos y la colección
#db = client.Accesosdb
#mi_coleccion = db.Accesosdb.clientes





# Realizar una consulta (obtener todos los documentos en la colección)
#resultados = mi_coleccion.find()

# Imprimir los resultados
#for documento in resultados:
 #   print("conexion satisfactoria")
  #  print(documento)
    

# Cerrar la conexión
#client.close() 












