from cargarUsuarios import cargarUsuarios

def logearUsuario(nombreUsuario, contraseñaUsuario, archivoUsuarios):
    usuarios_dict = cargarUsuarios(archivoUsuarios)
    if (nombreUsuario in usuarios_dict):
        if (usuarios_dict[nombreUsuario] == contraseñaUsuario):
            mensaje = "La contraseña es correcta."
        else:
            mensaje = "La contraseña es incorrecta."
    else:
        mensaje = "Este usuario no esta registrado."
    return mensaje

