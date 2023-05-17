import jwt
from datetime import datetime, timedelta
from django.conf import settings

def generate_jwt(payload):
    expiration = datetime.utcnow() + timedelta(days=12)
    payload['exp'] = expiration

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


def verify_jwt(payload):
    try:
        payload = jwt.decode(payload, settings.SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None