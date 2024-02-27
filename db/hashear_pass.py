from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Contraseña en texto plano proporcionada por el usuario
contraseña_plana = ""


# Hashear la contraseña
contraseña_hasheada = pwd_context.hash(contraseña_plana)

# Imprimir la contraseña hasheada
print("Contraseña hasheada:", contraseña_hasheada)