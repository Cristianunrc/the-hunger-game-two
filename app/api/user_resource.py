from flask_restful import Resource
from app import db 
from user.user import User
from flask import jsonify, make_response, request
from sqlalchemy import inspect
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, get_jwt_identity, unset_jwt_cookies, jwt_required
from datetime import timedelta

is_user_authenticated = False

class Structure(Resource):
    def get(self):
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        table_info = {}
        for table in tables:
            columns = inspector.get_columns(table)
            column_names = [column['name'] for column in columns]
            table_info[table] = column_names
        return jsonify(table_info)
        
class Register(Resource):
    def post(self):
        global is_user_authenticated
        data = request.get_json()
        name = data.get('name')
        password = data.get('password')
        confirm_password = data.get('confirmPassword')
        if name is None or password is None or name == '' or password == '':
            return { 'message': 'Nombre de usuario o contraseña obligatorios.' }, 400
        if password != confirm_password:
            return { 'error' : 'Las contraseñas no coinciden.' }, 401
        if is_user_authenticated:
            return { 'error': 'No puedes registrar una cuenta si estás logueado.' }, 400
        user = User()
        try:
            user.add_user(name, password)
            return { 'message': 'Usuario registrado con éxito.' }, 200
        except IntegrityError as integrity_error:
            db.session.rollback()
            return { 'error': 'Nombre de usuario en uso, prueba con otro.' }, 400

class Login(Resource):
    def post(self):
        global is_user_authenticated
        data = request.get_json()
        user = User.query.filter_by(username=data['name'], password=data['password']).first()
        if user:
            if is_user_authenticated:
                return { 'error': 'No puedes iniciar sesión mientras estés logueado.' }, 400         
            is_user_authenticated = True
            access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=5)) #se crea un token unico de acceso
            return { 'message': 'Inicio de sesión exitoso.',
                     'access_token': access_token }, 200
        return { 'error': 'Nombre de usuario o constraseña incorrectos.' }, 401

    @jwt_required()
    def get(self):
        try:
            user_id = get_jwt_identity()
            user = User.query.get(user_id)
            if user:
                return { 'message': 'Token de acceso valido', 
                         'user_id': user_id, 
                         'username': user.username }, 200
        except Exception as event:
            return { 'error': 'Token de acceso no valido' }, 401
        
class UserGet(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['name']).first()
        if user:
            return user.json(), 200
        else:
            return { 'error': 'Usuario no encontrado.' }, 404

class SelectPj(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['name']).first()
        user.select_character(num_pj=data['pj'])
        
class UserIdGet(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['name']).first()        
        if user:
            return { 'user_id': user.get_id() }, 200
        return { 'error': 'Usuario no encontrado.' }, 404

class Logout(Resource):
    @jwt_required()
    def post(self):
        global is_user_authenticated
        user_id = get_jwt_identity()
        user = User.query.get(user_id)
        if user:
            response = make_response()
            unset_jwt_cookies(response)
            is_user_authenticated = False
            return { 'message': 'Cierre de sesión exitoso.' }, 200
        return { 'error': 'No hay un usuario logueado.' }, 404