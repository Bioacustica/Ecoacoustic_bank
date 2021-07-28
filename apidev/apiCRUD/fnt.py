def choose_role(username: str, password: str, roles: str) -> str:
    """Función encargada de crear roles con el usuario y contraseña

    :param username: nombre del usuario
    :type username: str
    :param password: contraseña del usuario
    :type password: str
    :param roles:  rol que se le asiganará al usuario
    :type roles: str
    :return:  devuelve el query que será ejecutado por un cursor en postgres
    :rtype: str
    """
    rol = roles

    roles = {
        'admin':"SELECT bioacustica.create_user_admin('{}','{}')".format(
            username, password
        ),
        'registro':"SELECT bioacustica.create_user_registros('{}','{}')".format(
            username, password
        ),
        'etiquetado':"SELECT bioacustica.create_user_etiquetado('{}','{}')".format(
            username, password
        ),
        'usuario':"SELECT bioacustica.create_user_usuario('{}','{}')".format(
            username, password
        )


    }

    return(roles[rol])
    
def change_password(username:str, password:str) -> str:

    query = "SELECT bioacustica.change_password('{}', '{}')".format(username, password)

    return query

def delete_user(username:str) -> str:

    query = "SELECT drop_user('username')".format(username)

    return query