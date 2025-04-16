# Se necesita una clave secreta, pero esta herramienta puede fallar si la clave secreta no tiene una buena estructura, ya que por defecto jwt
# hace validaciones
import jwt



public_key = "Key private here"

payload = {
    "username":"user",
    "password":"password5"
}


access_token = jwt.encode(payload, public_key, algorithm="HS256")

print(access_token)
