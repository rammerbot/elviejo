##### Español:
### Portal El Viejo
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20210723.png?raw=true" align="center" style="width: 100%" />
</div>  
  

### <div align="center">Protal Web El Viejo</div>  
  #### Descripcion.
  
> Se trata de un portal, blog de la empresa de apuestas 'El Viejo' el mismo cuenta con seccion de noticias, blog, articulos de interes, seccion de envetos, ubicacion de sucursales, registro de usuarios. 

#### Características
- Registro de cuentas de usuarios.
- Agregar articulos a favoritos.
- Barra de busqueda de articulos.
- Informacion sobre cuotas y eventos.
- Informacion sobre las sucursales de la empresa.
- Panel administrativo.
- Cuenta de administrador.

#### Instalación

##### Crear entorno virtual:
```
python -m venv elviejo
```

##### Entrar en el entorno
```
cd elviejo
```
##### Activar el entorno dependiendo del sistema operativo
>  windows:
```
cd elviejo/Script
```
```
activate
```
> en Lunix:
```
source elviejo/bin/activate
```

##### Clonar el repositorio:

```
git clone https://github.com/rammerbot/elviejo.git
```

> Navegar al directorio del proyecto:

```
cd elviejo
```

##### Instalar las dependencias requeridas:

```
pip install -r requirements.txt
```

#### Uso
##### Crear base de dato y configurar la conexion
> luego ejecutar las migraciones
```
python manage.py makemigrations
```
```
python manage.py migrate
```

> Ejecutar la aplicación:

```
python manage.py runserver
```

##### Acceder al sistema a través de la URL proporcionada.

> Crear una cuenta de Administrador

```
python manage.py createsuperuser
```

##### Iniciar sesión con tu cuenta administrativa.
##### Usar la interfaz para cargar, evaluar y generar reportes y balances.

#### Contribuciones
##### Haz un fork del repositorio.

>Crea tu rama de funcionalidad:
  > Copiar código
```
git checkout -b feature/tu-funcionalidad
```
> Realiza tus cambios:

> Copiar código
```
git commit -m 'Agrega alguna funcionalidad'
```

> Sube tus cambios:

> Copiar código
```
git push origin feature/tu-funcionalidad
```
> Abre un pull request.
### Licencia
<p>Este proyecto está licenciado bajo la Licencia MIT. RammerBot</p>


### English:

## El Viejo Portal
<div align="center">
<img src="https://github.com/rammerbot/files/blob/main/Captura%20de%20pantalla%202024-05-26%20210723.png?raw=true" align="center" style="width: 100%" />
</div>  
<div align="center">El Viejo Portal Web</div>

 ### Description
 
 > It's a portal and Blog for the company 'El Viejo'. It includes sections for news, a blog, articles of interest, events, branch locations, and user registration.
#### Features

- User account registration.
- Adding articles to favorites.
- Article search bar.
- Information about odds and events.
- Information about company branches.
- Administrative panel.
- Administrator account.
  
#### Installation
#### Create a virtual environment:

```
python -m venv elviejo
```

#### Enter the environment
```
cd elviejo
```
#### Activate the environment depending on the operating system:

> Windows:

```
cd elviejo/Scripts
```
```
activate
```
> Linux:
```
source elviejo/bin/activate
```

Clone the repository:
```
git clone https://github.com/rammerbot/elviejo.git
```

> Navigate to the project directory:

```
cd elviejo
```

#### Install the required dependencies:
```
pip install -r requirements.txt
```

#### Usage
#### Create a database and configure the connection

> Then run the migrations
```
python manage.py makemigrations
```
```
python manage.py migrate
```

#### Run the application:

```
python manage.py runserver
```

#### Access the system through the provided URL.
 > Create an admin account:

```
python manage.py createsuperuser
```

#### Log in with your administrative account.
#### Use the interface to upload, evaluate, and generate reports and balances.
#### Contributions
> Fork the repository.
> Create your feature branch:

```
git checkout -b feature/your-feature
```

#### Commit your changes:

```
git commit -m 'Add some feature'
```

#### Push to the branch:
```
git push origin feature/your-feature
```

#### Open a pull request.

#### License
<p>This project is licensed under the MIT License. RammerBot</p>
