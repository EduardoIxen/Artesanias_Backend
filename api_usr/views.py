from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import hashlib
import os
import json

from .utils.jwt_utils import generate_jwt, verify_jwt
from django.conf import settings

cred_path = os.path.join(settings.BASE_DIR, 'artesanias-9f078-firebase-adminsdk-r6arm-8b0b10a99b.json')
cred = credentials.Certificate(cred_path)

# Comprueba si ya existe una aplicación de Firebase inicializada
if not firebase_admin._apps:
    # Si no hay una aplicación, inicializa una nueva
    firebase_admin.initialize_app(cred,  {
    'databaseURL': "https://artesanias-9f078-default-rtdb.firebaseio.com"
})

database = db.reference('')

@csrf_exempt
@require_http_methods(['GET'])
def index(request):
    productos = database.child('productos').get()
    return JsonResponse({'message': 'Hola mundo', "productos": productos})


@csrf_exempt
@require_http_methods(['POST'])
def registro(request):
    data = json.loads(request.body)

    existe_usr = database.child('usuarios').order_by_child('email').equal_to(data['email']).get()
    
    if existe_usr:
        return JsonResponse({'message': 'El correo ingresado ya se encuentra registrado'}, status=401)


    password = hashlib.sha256(data['contrasena'].encode('utf-8')).hexdigest()

    data['contrasena'] = password
    id = database.child('usuarios').push(data)
    return JsonResponse({'message': 'Registro exitoso', 'id': id.key}, status=200)

