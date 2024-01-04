# Aplicación de juego llamado The Hunger Game

## Para poder instalar la aplicación deberás realizar los siguientes pasos

Una vez que hayas clonado la aplicación y estés ubicado en el directorio correspondiente, ejecuta los siguientes comandos:

1. **Crear el entorno virtual:**

    `python -m venv venv`

3. **Ejecutar el entorno virtual:**

    _En windows:_

    `.\venv\scripts\activate`

2. **Con el entorno virtual activo proceder a instalar las dependencias del archivo requirements.txt:**

    `pip install -r requirements.txt`

3. **Instalar las dependencias del cliente:**

    _Ubicarse en la carpeta client y ejecutar el siguiente comando:_

    `npm install`

4. **Crear la base de datos:**

    _En una terminal, ubicado en el directorio de la aplicación y con el venv activo ejecuta:_

    `python app.py`

    _Esto leventará el servidor 5000.

    _En una segunda terminal, ubicado en el directorio de la aplicación y con el venv activo ejecuta:_

    `python`

    _Esto abrirá la consola de python, en la misma ejecuta el siguiente script:_

    import app
    from app import db, create_app
    app = create_app()
    with app.app_context():
    db.create_all()

    _Luego de escribir el script presiona dos veces enter._

    _Esto creará una carpeta instance/db_user.db, con la base de datos.


## Para poder levantar la aplicación y jugar deberás realizar los siguientes pasos

1. **Levantar la aplicación:**

    _Ubicado en el directorio de la aplicación y con el venv activo ejecuta:_

    `python app.py`

    _En una segunda terminal y ubicado en la carpeta client ejecuta:_

    `npm start`

    _Esto abrirá una página web con el juego en un puerto localhost:3000 


# Disfruta del juego!