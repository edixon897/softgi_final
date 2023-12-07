import secrets
import string

#token de registro
def token_registro(length=32):  
    characters = string.ascii_letters + string.digits  
    token01 = ''.join(secrets.choice(characters) for _ in range(length))
    return token01 

#token de recuperacion de contraseña
def token_recuperar_contrasena(length=32):
    characters = string.ascii_letters + string.digits  
    token02 = ''.join(secrets.choice(characters) for _ in range(length))
    return token02

def generador_id(length=20):
    characters = string.ascii_letters + string.digits  
    generador = ''.join(secrets.choice(characters) for _ in range(length))
    return generador