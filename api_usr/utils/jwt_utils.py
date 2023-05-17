import jwt
from datetime import datetime, timedelta
from django.conf import settings

#Genera un token con la informacion del usuario, el cual expira en 1 dia
def generate_jwt(payload):
    expiration = datetime.utcnow() + timedelta(days=1)
    payload['exp'] = expiration

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


#Verifica si el token es valido y retorna los datos del usuario
def verify_jwt(payload):
    try:
        payload = jwt.decode(payload, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None