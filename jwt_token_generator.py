# This tools allows you to generater tokens with any key
import base64
import hmac
import hashlib
import json

# Clave secreta, incluyendo el 'ssh-rsa' al principio
#example
#secret = b'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDHSoarRoLvgAk4O41RE0w6lj2e7TDTbFk62WvIdJFo/aSLX/x9oc3PDqJ0Qu1x06/8PubQbCSLfWUyM7Dk0+irzb/VpWAurSh+hUvqQCkHmH9mrWpMqs5/L+rluglPEPhFwdL5yWk5kS7rZMZz7YaoYXwI7Ug4Es4iYbf6+UV0sudGwc3HrQ5uGUfOpmixUO0ZgTUWnrfMUpy2dFbZp7puQS6T8b5EJPpLY+iojMb/rbPB34NrvJKU1F84tfvY8xtg3HndTNPyNWp7EOsujKZIxKF5/RdW+Qf9jjBMvsbjfCo0LiNVjpotiLPVuslsEWun+LogxR+fxLiUehSBb8ip'

secret = 'Your-Key-Secret-Here'


# Datos del token
header = {
    "alg": "HS256",
    "typ": "JWT"
}

payload = {
    "username": "admin",
    "admin": 1
}

def b64url_encode(data):
    return base64.urlsafe_b64encode(data).rstrip(b'=')

# Codificamos el header y el payload
header_b64 = b64url_encode(json.dumps(header, separators=(',', ':')).encode())
payload_b64 = b64url_encode(json.dumps(payload, separators=(',', ':')).encode())

# Concatenamos
msg = header_b64 + b'.' + payload_b64

# Firmamos usando HMAC-SHA256 con tu clave secreta
signature = hmac.new(secret, msg, hashlib.sha256).digest()
signature_b64 = b64url_encode(signature)

# Armamos el token final
jwt_token = msg + b'.' + signature_b64

print(jwt_token.decode())
