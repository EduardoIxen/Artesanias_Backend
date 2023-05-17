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


# Verificar si el usuario existe en la base de datos y si las credenciales ingresadas son correctas,
# si es así, se genera un token y se devuelve al usuario
@csrf_exempt
@require_http_methods(['POST'])
def login(request):
    data = json.loads(request.body)
    admin = database.child('administradores').get()

    password = hashlib.sha256(data['contrasena'].encode('utf-8')).hexdigest()

    for item in admin:
        if item['email'] == data['email'] and item['contrasena'] == password:

            payload = {
                'email': item['email'],
                'id': item['id'],
                'nombre': item['nombre']
            }
            token = generate_jwt(payload)

            return JsonResponse({'message': 'Inicio de sesion exitoso', 'token': token, 'usr': payload}, status=200)
    
    return JsonResponse({'message': 'Usuario o contraseña incorrectos'}, status=401)


@csrf_exempt
@require_http_methods(['POST'])
def logout(request):
    data = json.loads(request.body)
    payload = {
        'email': data['email'],
        'id': data['id'],
        'nombre': data['nombre']
    }
    generate_jwt(payload) # Para que el token del login sea invalidado
    return JsonResponse({'message': 'Logout exitoso'}, status=200)


@csrf_exempt
@require_http_methods(['POST'])
def agregar_producto(request):
    try:
        data = json.loads(request.body)

        token = request.headers.get('Authorization')
        if not token:
            return JsonResponse({'message': 'Token no proporcionado'}, status=401)

        payload = verify_jwt(token)

        if not payload:
            return JsonResponse({'message': 'Token no valido o ha expirado'}, status=401)
            
        sku = data['sku']
        if sku:
            # Verificar si el SKU ya existe en la base de datos
            existing_product = database.child('productos').order_by_child('sku').equal_to(sku).get()
            if existing_product:
                return JsonResponse({'message': 'El SKU ya está en uso'}, status=409)


        database.child('productos').push(data) # Agregar producto a la base de datos
        return JsonResponse({'message': 'Producto agregado exitosamente'}, status=200)

    except Exception as e:
        return JsonResponse({'message': 'Error al agregar producto', 'error': e}, status=500)