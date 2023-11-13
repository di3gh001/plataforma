# Importaciones de módulos y paquetes necesarios
from flask import flash, Flask, render_template, request, session, redirect, url_for, Response
from flask_mysqldb import MySQL

from flask import jsonify
import json
import traceback

# Creación de la aplicación Flask
app = Flask(__name__, template_folder='template')
app.secret_key = "diego"

# Configuración de la base de datos MySQL
app.config['MYSQL_HOST'] = 'Di3gh003.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'Di3gh003'
app.config['MYSQL_PASSWORD'] = '6482865Cbbab'
app.config['MYSQL_DB'] = 'Di3gh003$plataforma'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

#app.config['MYSQL_HOST'] = 'localhost'
#app.config['MYSQL_USER'] = 'root'
#app.config['MYSQL_PASSWORD'] = ''
#app.config['MYSQL_DB'] = 'plataforma'
#app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#mysql = MySQL(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/acceso-login', methods=["POST", "GET"])
def login():

    if request.method == 'POST' and 'txtusuario' in request.form and 'txtcontraseña' in request.form:
        nombre = request.form['txtusuario']
        contraseña = request.form['txtcontraseña']

        # Conexión a la base de datos y ejecución de la consulta
        cur = mysql.connection.cursor()
        cur.execute(
            'SELECT * FROM usuarios WHERE usuario = %s AND contraseña = %s', (nombre, contraseña))
        account = cur.fetchone()

        if account is not None:
            # Establecer variables de sesión para el usuario autenticado
            session['logueado'] = True
            session['id'] = account['id']
            session['nombre'] = account['nombre']
            session['apellido'] = account['apellido']
            session['cedula'] = account['cedula']
            session['profesion'] = account['profesion']
            session['fechanac'] = account['fechanac']
            session['correo'] = account['usuario']
            session['telefono'] = account['telefono']

            session['id_rol'] = account['id_rol']

            # Redirigir según el rol del usuario
            if session['id_rol'] == 1:

                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM usuarios")
                cur.close()
                return redirect(url_for('admin'))
            elif session['id_rol'] == 2:
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM usuarios")
                cur.close()

                return redirect(url_for('usuario'))
            elif session['id_rol'] == 3:
                cur = mysql.connection.cursor()
                cur.execute("SELECT * FROM usuarios")
                cur.close()
                return redirect(url_for('tecnico'))
        else:
            # Mostrar mensaje de error si las credenciales son incorrectas
            flash('Correo y/o contraseña incorrectos', 'danger')
            return render_template('index.html', mensaje="usuario y/o contraseña incorrectos")

    # Renderizar la página de inicio si no se envió un formulario de inicio de sesión

    return render_template('index.html')


@app.route('/crear-registro', methods=["POST"])
def crear_registro():
    # Obtener datos del formulario
    correo = request.form['txtCorreo']
    password = request.form['txtPassword']
    nombre = request.form['txtnombre']
    apellido = request.form['txtapellido']
    fechanac = request.form['txtfechanac']
    cedula = request.form['txtcedula']
    profesion = request.form['txtprofesion']
    telefono = request.form['txttelefono']

    # Conexión a la base de datos y ejecución de la verificación
    cur = mysql.connection.cursor()

    # Verificar si el correo ya está registrado
    cur.execute("SELECT * FROM usuarios WHERE usuario = %s", (correo,))
    usuario_existente = cur.fetchone()

    if usuario_existente:
        # Si el correo ya está registrado, mostrar mensaje de error
        flash('Correo electrónico ya registrado. Por favor, utiliza otro correo.')
        return render_template("index.html", mensaje2="Correo electrónico ya registrado. Por favor, utiliza otro correo")

    # Si el correo no está registrado, realizar la inserción
    cur.execute(
        "INSERT INTO usuarios (usuario, contraseña, nombre, apellido, fechanac, cedula, profesion,telefono, id_rol) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, '2')",
        (correo, password, nombre, apellido, fechanac, cedula, profesion, telefono))
    mysql.connection.commit()

    # Mostrar mensaje de éxito
    flash('Usuario registrado exitosamente')
    return render_template("index.html", mensaje2="Usuario registrado exitosamente")


@app.route('/crear-registrotec', methods=["POST"])
def crear_registrotec():
    # Obtener datos del formulario
    correo = request.form['txtCorreo']
    password = request.form['txtPassword']
    nombre = request.form['txtnombre']
    apellido = request.form['txtapellido']
    fechanac = request.form['txtfechanac']
    cedula = request.form['txtcedula']
    profesion = request.form['txtprofesion']
    telefono = request.form['txttelefono']

    # Conexión a la base de datos y ejecución de la verificación
    cur = mysql.connection.cursor()

    # Verificar si el correo ya está registrado
    cur.execute("SELECT * FROM usuarios WHERE usuario = %s", (correo,))
    usuario_existente = cur.fetchone()

    if usuario_existente:
        # Si el correo ya está registrado, mostrar mensaje de error
        flash('Correo electrónico ya registrado. Por favor, utiliza otro correo.')
        return redirect(url_for('tecnico'))

    # Si el correo no está registrado, realizar la inserción
    cur.execute(
        "INSERT INTO usuarios (usuario, contraseña, nombre, apellido, fechanac, cedula, profesion,telefono, id_rol) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, '2')",
        (correo, password, nombre, apellido, fechanac, cedula, profesion, telefono))
    mysql.connection.commit()

    # Mostrar mensaje de éxito
    flash('Usuario registrado exitosamente')
    return redirect(url_for('tecnico'))


@app.route('/crear-registroadm', methods=["POST"])
def crear_registroadm():
    # Obtener datos del formulario
    correo = request.form['txtCorreo']
    password = request.form['txtPassword']
    nombre = request.form['txtnombre']
    apellido = request.form['txtapellido']
    fechanac = request.form['txtfechanac']
    cedula = request.form['txtcedula']
    telefono = request.form['txttelefono']
    profesion = request.form['txtprofesion']

    # Conexión a la base de datos y ejecución de la verificación
    cur = mysql.connection.cursor()

    # Verificar si el correo ya está registrado
    cur.execute("SELECT * FROM usuarios WHERE usuario = %s", (correo,))
    usuario_existente = cur.fetchone()

    if usuario_existente:
        # Si el correo ya está registrado, mostrar mensaje de error
        flash('Correo electrónico ya registrado. Por favor, utiliza otro correo.')
        return redirect(url_for('admin'))

    # Si el correo no está registrado, realizar la inserción
    cur.execute(
        "INSERT INTO usuarios (usuario, contraseña, nombre, apellido, fechanac, cedula,profesion, telefono, id_rol) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, '2')",
        (correo, password, nombre, apellido, fechanac, cedula, profesion, telefono))
    mysql.connection.commit()

    # Mostrar mensaje de éxito
    flash('Usuario registrado exitosamente')
    return redirect(url_for('admin'))
# ------------------------------------------ADMIN---------------------------------------------------------


@app.route('/admin', methods=["GET"])
def admin():
    if 'logueado' in session and session['id_rol'] == 1:

        operadores = listarop()
        return render_template('admin.html', operadores=operadores)
    flash('DEBES INICIAR SESION PARA PODER ACCEDER')
    return render_template('index.html', mensaje="DEBES INICIAR SESION PARA PODER ACCEDER")


@app.route('/agregarpacad', methods=["POST"])
def agregarpacad():
    # Obtener datos del formulario

    nombrepac = request.form['txtnombrepactec']
    apellidopac = request.form['txtapellidopactec']
    cedulapac = request.form['txtcedulapactec']
    fechanacpac = request.form['txtfechanacpactec']

    operador_id = request.form['operador']

    if nombrepac and apellidopac and fechanacpac and cedulapac and id:
        # Conexión a la base de datos y ejecución de la inserción
        cur = mysql.connection.cursor()
        sql = "INSERT INTO paciente (nombres, apellidos, cedulapac, fechanacpc, id) VALUES (%s,%s, %s, %s, %s )"
        data = (nombrepac, apellidopac, cedulapac,
                fechanacpac, operador_id)
        cur.execute(sql, data)
        mysql.connection.commit()

    # Mostrar mensaje de éxito
    flash('Paciente Agregado Exitosamente')
    return redirect(url_for('admin'))


@app.route('/updatepac/<id_paciente>', methods=['POST'])
def update_pac(id_paciente):
    if request.method == 'POST':
        nombres = request.form['txtnombrepac']

        apellidos = request.form['txtapellidopac']

        cedulapac = request.form['txtcedulapac']

        fechanacpac = request.form['txtfechanacpac']

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE paciente
        SET     nombres = %s,
                apellidos = %s,
                
      
                cedulapac = %s,
                
                fechanacpc = %s
                
        WHERE id_paciente = %s
    """, (nombres, apellidos, cedulapac, fechanacpac, id_paciente))
    mysql.connection.commit()
    flash('Actualización Exitosa!')

    return redirect(url_for('listarpaciente'))


@app.route('/updatepactec/<id_paciente>', methods=['POST'])
def update_pactec(id_paciente):
    if request.method == 'POST':
        nombres = request.form['txtnombrepac']

        apellidos = request.form['txtapellidopac']

        cedulapac = request.form['txtcedulapac']

        fechanacpac = request.form['txtfechanacpac']

        operador = request.form['operador']

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE paciente
        SET     nombres = %s,
                apellidos = %s,
                
      
                cedulapac = %s,
                
                fechanacpc = %s,
                id=%s
                
        WHERE id_paciente = %s
    """, (nombres, apellidos, cedulapac, fechanacpac, operador, id_paciente))
    mysql.connection.commit()
    flash('Actualización Exitosa!')

    return redirect(url_for('tecnico'))

# lista de operadores


@app.route('/listar', methods=["GET", "POST"])
def listar():
    if 'logueado' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE id_rol = 2")
        lista = cur.fetchall()

        cur.close()

    # Renderizar la página 'listar.html' con la lista de usuarios
        return render_template('listar.html', lista=lista)
    return render_template('index.html')
    # Consulta a la base de datos para obtener una lista de usuarios con id_rol igual a 1


@app.route('/buscarusuario', methods=["POST", "GET"])
def buscarusuario():

    if 'logueado' in session:
        termino_busqueda = request.form['nombre']

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE nombre LIKE %s OR cedula = %s OR apellido LIKE %s OR usuario LIKE %s OR profesion LIKE %s",
                    ('%' + termino_busqueda + '%', termino_busqueda, '%' + termino_busqueda + '%', termino_busqueda + '%', termino_busqueda + '%'))

        lista = cur.fetchall()
        return render_template('listar.html', lista=lista)
    return render_template('index.html')


@app.route('/editaroperador/<id>')
def editaroperador(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM usuarios WHERE id = %s', (id))

    return render_template('listar.html')


@app.route('/update/<id>', methods=['POST'])
def update_operador(id):
    if request.method == 'POST':
        nombres = request.form['txtnombreop']
        apellidos = request.form['txtapellidoop']
        correo = request.form['txcorreoop']
        contraseña = request.form['txtcontraseñaop']
        cedula = request.form['txtcedulaop']
        profesion = request.form['txtprofesionop']
        fechanac = request.form['txtfechanacop']
        telefono = request.form['txttelefono']

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE usuarios
        SET     nombre = %s,
                apellido = %s,
                usuario = %s,
                contraseña = %s,
                cedula = %s,
                profesion = %s,
                telefono =%s,
                fechanac = %s
        WHERE id = %s
    """, (nombres, apellidos, correo, contraseña, cedula, profesion, telefono, fechanac, id))
    mysql.connection.commit()
    flash('Usuario actualizado')
    return redirect(url_for('listar'))


@app.route('/borraroperador/<string:id>')
def borraroperador(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id ={0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('listar'))


@app.route('/borraroperadortec/<string:id>')
def borraroperadortec(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM usuarios WHERE id ={0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('tecnico'))


@app.route('/borrarpaciente/<string:id_paciente>')
def borrarpaciente(id_paciente):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM paciente WHERE id_paciente ={0}'.format(id_paciente))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('listarpaciente'))


@app.route('/borrarpacientetec/<string:id_paciente>')
def borrarpacientetec(id_paciente):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM paciente WHERE id_paciente ={0}'.format(id_paciente))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('tecnico'))


@app.route('/borrardato/<string:id_tratamiento>', methods=["GET", "POST"])
def borrardato(id_tratamiento):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tratamiento WHERE id_tratamiento = %s',
                (id_tratamiento,))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('tecnico'))


@app.route('/borrar_dato2/<string:id_tratamiento2>', methods=["GET", "POST"])
def borrar_dato2(id_tratamiento2):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM tratamiento2 WHERE id_tratamiento2 = %s', (id_tratamiento2,))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('tecnico'))


@app.route('/borrardato3/<string:id_tratamiento3>', methods=["GET", "POST"])
def borrardato3(id_tratamiento3):
    cur = mysql.connection.cursor()
    cur.execute(
        'DELETE FROM tratamiento3 WHERE id_tratamiento3 = %s', (id_tratamiento3,))
    mysql.connection.commit()
    flash('Contacto Eliminado')
    return redirect(url_for('tecnico'))


# --------------------------------------------------OPERADOR--------------------------------------------------


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/usuario')
def usuario():
    if 'logueado' in session and session['id_rol'] == 2 and session.get('id'):
        pacientes = LISTAPAC()
        return render_template('usuario.html', pacientes=pacientes)
    else:
        flash('Debes iniciar sesión como usuario con el rol correcto', 'danger')
        return redirect(url_for('acceso-login'))


@app.errorhandler(Exception)
def handle_error(e):
    ruta = request.path
    mensaje = traceback.format_exc()

    # Insertar el error en la base de datos
    try:
        with app.app_context():
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO errores (ruta, mensaje) VALUES (%s, %s)", (ruta, mensaje))
            mysql.connection.commit()
    except Exception as db_error:
        print(f"Error al insertar en la base de datos: {db_error}")

    return render_template('error.html', error=e), 500


@app.route('/agregarpac', methods=["POST"])
def agregarpac():
    nombrepac = request.form['txtnombrepac']
    apellidopac = request.form['txtapellidopac']
    cedulapac = request.form['txtcedulapac']
    fechanacpac = request.form['txtfechanacpac']
    operador = session['id']

    # Conexión a la base de datos y ejecución de la consulta para verificar si el paciente existe
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM paciente WHERE cedulapac = %s", (cedulapac,))
    paciente_existente = cur.fetchone()

    if paciente_existente:
        flash('El paciente ya existe')
    else:
        # El paciente no existe, entonces se agrega a la base de datos
        sql = "INSERT INTO paciente (nombres, apellidos, cedulapac, fechanacpc, id) VALUES (%s, %s, %s, %s, %s )"
        data = (nombrepac, apellidopac, cedulapac, fechanacpac, operador)
        cur.execute(sql, data)
        mysql.connection.commit()
        flash('Paciente Agregado Exitosamente')

    return redirect(url_for('usuario'))


@app.route('/accesopac', methods=["GET"])
def accesopac():
    if 'logueado' in session and session['logueado']:
        # Recupera la cédula del paciente del parámetro de consulta
        cedulapac = request.args.get('cedulapac')

        if cedulapac:
            # Si la cédula está definida, autentica al paciente
            paciente = autenticar_paciente_cedula(cedulapac)

            if paciente:
                # Si el paciente existe en la base de datos
                session['id_paciente'] = paciente['id_paciente']
                session['nombrepac'] = paciente['nombres']
                session['apellidopac'] = paciente['apellidos']
                session['cedulapac'] = paciente['cedulapac']
                session['fechanacpc'] = paciente['fechanacpc']
                session['id'] = paciente['id']

                return redirect(url_for('paciente'))
            else:
                flash('El paciente no existe', 'danger')
                return redirect(url_for('usuario'))
        else:
            flash('Cédula del paciente no proporcionada', 'danger')
            return redirect(url_for('algun_otro_ruteo'))
    else:
        flash('Debes estar logueado para acceder a un paciente', 'danger')
        return redirect(url_for('acceso-login'))


def autenticar_paciente_cedula(cedulapac):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM paciente WHERE cedulapac = %s", (cedulapac,))
    paciente = cur.fetchone()
    cur.close()

    return paciente
 # ------------------------------------------------------------------------PACIENTE--------------------------


@app.route('/paciente')
def paciente():
    if 'logueado' in session:
        cedulapac = session.get('cedulapac')
        if cedulapac:
            # Aquí puedes usar cedula_paciente para referenciar al paciente
            return render_template('paciente.html')
        else:
            flash('No se ha seleccionado un paciente', 'danger')
            return redirect(url_for('usuario'))
    return render_template('index.html')


@app.route('/listarpaciente', methods=["GET"])
def listarpaciente():
    if 'logueado' in session:
        operadores = listarop()
        # Consulta a la base de datos para obtener una lista de usuarios con id_rol igual a 1
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT paciente.*, usuarios.nombre AS nombre_usuario FROM paciente LEFT JOIN usuarios ON paciente.id = usuarios.id")
        listapac = cur.fetchall()

        cur.close()

        # Renderizar la página 'listar.html' con la lista de usuarios
        return render_template('listarpaciente.html', listapac=listapac, operadores=operadores)
    return render_template('index.html')


@app.route('/LISTAPAC', methods=["GET"])
def LISTAPAC():

    # Consulta a la base de datos para obtener una lista de usuarios con id_rol igual a 1
    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT paciente.*, usuarios.nombre AS nombre_usuario FROM paciente LEFT JOIN usuarios ON paciente.id = usuarios.id")
    listapacient = cur.fetchall()

    cur.close()

    return listapacient


@app.route('/listatrat', methods=["GET"])
def listatrat():

    # Consulta a la base de datos para obtener una lista de usuarios con id_rol igual a 1
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tratamiento WHERE id_tratamiento")
    listatratamiento = cur.fetchall()

    cur.close()

    return listatratamiento


@app.route('/listatrat2', methods=["GET"])
def listatrat2():

    # Consulta a la base de datos para obtener una lista de usuarios con id_rol igual a 1
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tratamiento2 WHERE id_tratamiento2")
    listatratamiento2 = cur.fetchall()

    cur.close()

    return listatratamiento2


@app.route('/listatrat3', methods=["GET"])
def listatrat3():

    # Consulta a la base de datos para obtener una lista de usuarios con id_rol igual a 1
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tratamiento3 WHERE id_tratamiento3")
    listatratamiento3 = cur.fetchall()

    cur.close()

    return listatratamiento3


@app.route('/listarerror', methods=["GET"])
def listarerror():

    # Consulta a la base de datos para obtener una lista de usuarios con id_rol igual a 1
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM errores WHERE id_error")
    listarerror = cur.fetchall()

    cur.close()

    return listarerror


@app.route('/listarop', methods=["GET", "POST"])
def listarop():
    if 'logueado' in session:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM usuarios WHERE id_rol = 2")
        lista = cur.fetchall()

        cur.close()

    # Renderizar la página 'listar.html' con la lista de usuarios
        return lista
    return render_template('index.html')
    # Consulta a la base de datos para obtener una lista de usuarios con id_rol igual a 1

# ---------------------------------------------------tecnico----------------------------------


@app.route('/tecnico', methods=["GET"])
def tecnico():

    if 'logueado' in session and session['id_rol'] == 3:

        pacientes = LISTAPAC()
        operadores = listarop()
        tratamiento = listatrat()
        tratamiento2 = listatrat2()
        tratamiento3 = listatrat3()
        error = listarerror()

    # Renderizar la página 'listar.html' con la lista de usuarios
        return render_template('tecnico.html', pacientes=pacientes, operadores=operadores, tratamiento=tratamiento, tratamiento2=tratamiento2, tratamiento3=tratamiento3, error=error)
    return render_template('index.html')


@app.route('/registrotec', methods=["POST"])
def registrotec():
    # Obtener datos del formulario
    correo = request.form['txtCorreo']
    password = request.form['txtPassword']
    nombre = request.form['txtnombre']
    apellido = request.form['txtapellido']
    fechanac = request.form['txtfechanac']
    cedula = request.form['txtcedula']
    profesion = request.form['txtprofesion']

    # Conexión a la base de datos y ejecución de la inserción
    cur = mysql.connection.cursor()
    cur.execute(
        "INSERT INTO usuarios (usuario, contraseña, nombre, apellido, fechanac, cedula, profesion, id_rol) VALUES (%s, %s, %s, %s, %s, %s, %s, '2')",
        (correo, password, nombre, apellido, fechanac, cedula, profesion))
    mysql.connection.commit()

    # Mostrar mensaje de éxito
    flash('Contacto Agregado Exitosamente')
    return redirect(url_for('tecnico', mensaje2="Operador Registrado Exitosamente"))


@app.route('/agregarpactec', methods=["POST"])
def agregarpactec():
    # Obtener datos del formulario
    nombrepac = request.form['txtnombrepactec']
    apellidopac = request.form['txtapellidopactec']
    cedulapac = request.form['txtcedulapactec']
    fechanacpac = request.form['txtfechanacpactec']
    operador_id = request.form['operador']

    # Conexión a la base de datos y ejecución de la consulta para verificar si el paciente existe
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM paciente WHERE cedulapac = %s", (cedulapac,))
    paciente_existente = cur.fetchone()

    if paciente_existente:
        flash('El paciente ya existe')
    else:
        # El paciente no existe, entonces se agrega a la base de datos
        sql = "INSERT INTO paciente (nombres, apellidos, cedulapac, fechanacpc, id) VALUES (%s, %s, %s, %s, %s )"
        data = (nombrepac, apellidopac, cedulapac, fechanacpac, operador_id)
        cur.execute(sql, data)
        mysql.connection.commit()
        flash('Paciente Agregado Exitosamente')

    return redirect(url_for('tecnico'))


@app.route('/updatetec/<id>', methods=['POST'])
def updatetec(id):
    if request.method == 'POST':
        nombres = request.form['txtnombreop']
        apellidos = request.form['txtapellidoop']
        correo = request.form['txcorreoop']
        contraseña = request.form['txtcontraseñaop']
        cedula = request.form['txtcedulaop']
        profesion = request.form['txtprofesionop']
        fechanac = request.form['txtfechanacop']

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE usuarios
        SET     nombre = %s,
                apellido = %s,
                usuario = %s,
                contraseña = %s,
                cedula = %s,
                profesion = %s,
                fechanac = %s
        WHERE id = %s
    """, (nombres, apellidos, correo, contraseña, cedula, profesion, fechanac, id))
    mysql.connection.commit()
    flash('contacto actualizado')
    return redirect(url_for('tecnico'))


@app.route('/updatepactec/<id_paciente>', methods=['POST'])
def updatepactec(id_paciente):
    if request.method == 'POST':
        nombres = request.form['txtnombrepac']

        apellidos = request.form['txtapellidopac']

        cedulapac = request.form['txtcedulapac']

        fechanacpac = request.form['txtfechanacpac']

    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE paciente
        SET     nombres = %s,
                apellidos = %s,
      
                cedulapac = %s,
                
                fechanacpc = %s
        WHERE id_paciente = %s
    """, (nombres, apellidos, cedulapac, fechanacpac, id_paciente))
    mysql.connection.commit()

    return redirect(url_for('tecnico'))


@app.route('/buscarpaciente', methods=["POST", "GET"])
def buscarpaciente():
    termino_busquedapac = request.form['nombrepac']

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM paciente WHERE nombres LIKE %s OR cedulapac = %s OR apellidos LIKE %s",
                ('%' + termino_busquedapac + '%', termino_busquedapac, '%' + termino_busquedapac + '%'))

    listapac = cur.fetchall()
    return render_template('listarpaciente.html', listapac=listapac)


@app.route('/editarpaciente')
def editarpaciente():
    return render_template('inicio.html')


@app.route('/plantillajuegos', methods=["POST", "GET"])
def plantillajuegos():
    return render_template('plantillajuegos.html')


@app.route('/juego1', methods=["POST", "GET"])
def juego1():
    if 'logueado' in session:

        return render_template('juego1.html')
    return render_template('index.html')


@app.route('/izquierda1', methods=["POST", "GET"])
def izquierda1():
    if 'logueado' in session:

        return render_template('izquierda1.html')
    return render_template('index.html')


@app.route('/derecha1', methods=["POST", "GET"])
def derecha1():
    if 'logueado' in session:

        return render_template('derecha1.html')
    return render_template('index.html')


@app.route('/izquierda2', methods=["POST", "GET"])
def izquierda2():
    if 'logueado' in session:

        return render_template('izquierda2.html')
    return render_template('index.html')


@app.route('/izquierda3', methods=["POST", "GET"])
def izquierda3():
    if 'logueado' in session:

        return render_template('izquierda3.html')
    return render_template('index.html')


@app.route('/derecha2', methods=["POST", "GET"])
def derecha2():
    if 'logueado' in session:

        return render_template('derecha2.html')
    return render_template('index.html')


@app.route('/derecha3', methods=["POST", "GET"])
def derecha3():
    if 'logueado' in session:

        return render_template('derecha3.html')
    return render_template('index.html')


@app.route('/juego2', methods=["POST", "GET"])
def juego2():
    return render_template('juego2.html')


@app.route('/juego3', methods=["POST", "GET"])
def juego3():
    return render_template('juego3.html')


@app.route('/logout', methods=["GET"])
def logout():
    session.pop('logueado', None)
    session.pop('id', None)
    session.pop('id_rol', None)
    return redirect('/')


@app.route('/puntos', methods=['POST', 'GET'])
def puntos():

    tiempo_str = request.args.get('tiempo')
    tiempo_json = json.loads(tiempo_str)
    minutos = tiempo_json['minutos']
    segundos = tiempo_json['segundos']
    texto_adicional = request.args.get('texto')
    print(request.args.get('texto'))
    return render_template('puntos.html', minutos=minutos, segundos=segundos, texto_adicional=texto_adicional)


@app.route('/puntos2', methods=['POST', 'GET'])
def puntos2():
    tiempo_str = request.args.get('tiempo')
    tiempo_json = json.loads(tiempo_str)
    minutos = tiempo_json['minutos']
    segundos = tiempo_json['segundos']
    texto_adicional = request.args.get('texto')

    return render_template('puntos2.html', minutos=minutos, segundos=segundos, texto_adicional=texto_adicional)


@app.route('/puntos3', methods=['POST', 'GET'])
def puntos3():
    tiempo_str = request.args.get('tiempo')
    tiempo_json = json.loads(tiempo_str)
    minutos = tiempo_json['minutos']
    segundos = tiempo_json['segundos']
    texto_adicional = request.args.get('texto')
    return render_template('puntos3.html', minutos=minutos, segundos=segundos, texto_adicional=texto_adicional)


@app.route('/enviarpuntos', methods=['POST', 'GET'])
def enviarpuntos():

    puntos = request.form['txtpuntos']
    pacienteid = session['id_paciente']
    nivel = request.form['txtnivel']
    mano = request.form['txtmano']

    # Conexión a la base de datos y ejecución de la consulta para verificar si el paciente existe
    cur = mysql.connection.cursor()

    # El paciente no existe, entonces se agrega a la base de datos
    sql = "INSERT INTO tratamiento (nivel, hora,mano, id_paciente) VALUES ( %s,%s, %s, %s )"
    data = (nivel, puntos, mano, pacienteid)
    cur.execute(sql, data)
    mysql.connection.commit()
    flash('tiempo agregado')

    return redirect(url_for('plantillajuegos', mensaje3="puntos agregados"))


@app.route('/enviarpuntos2', methods=['POST', 'GET'])
def enviarpuntos2():

    puntos = request.form['txtpuntos']
    pacienteid = session['id_paciente']
    nivel = request.form['txtnivel']
    mano = request.form['txtmano']
    # Conexión a la base de datos y ejecución de la consulta para verificar si el paciente existe
    cur = mysql.connection.cursor()

    # El paciente no existe, entonces se agrega a la base de datos
    sql = "INSERT INTO tratamiento2 (nivel, hora,mano, id_paciente) VALUES ( %s,%s, %s , %s)"
    data = (nivel, puntos, mano, pacienteid)
    cur.execute(sql, data)
    mysql.connection.commit()
    flash('tiempo agregado')

    return redirect(url_for('plantillajuegos', mensaje3="puntos agregados"))


@app.route('/enviarpuntos3', methods=['POST', 'GET'])
def enviarpuntos3():

    puntos = request.form['txtpuntos']
    pacienteid = session['id_paciente']
    nivel = request.form['txtnivel']
    mano = request.form['txtmano']
    # Conexión a la base de datos y ejecución de la consulta para verificar si el paciente existe
    cur = mysql.connection.cursor()

    # El paciente no existe, entonces se agrega a la base de datos
    sql = "INSERT INTO tratamiento3 (nivel, hora, mano,id_paciente) VALUES ( %s,%s, %s,%s )"
    data = (nivel, puntos, mano, pacienteid)
    cur.execute(sql, data)
    mysql.connection.commit()
    flash('tiempo agregado')

    return redirect(url_for('plantillajuegos', mensaje3="puntos agregados"))


# Inicio de la aplicación
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)
