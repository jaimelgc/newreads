<div align="center">

# NEWREADS: PROYECTO FINAL 

</div>

<div align="center">
<img src="../img/logo-1-crop.png" />
</div>

+ Autor: Jaime León García
+ Curso: 2024/2025 2º DAW
+ Tutor: David Jorge Bilbao

## Índice

1. [**INTRODUCCIÓN.**](#id1)
2. [**TECNOLOGÍAS UTILIZADAS.**](#id2)
3. [**DERECHOS DE AUTOR.**](#id2)
4. [**GRADO DE CUMPLIMIENTO.**](#id4)
5. [**PLAN DE MARKETING.**](#id5)
6. [**PLAN DE MANTENIMIENTO.**](#id6)

### 1. INTRODUCCIÓN. <a name="id1"></a>

Este documento presenta el reporte de la primera fase de desarrollo de NewReads, aquí se verán datos como las tecnologías utilizadas durante el desarrollo, el rango de cumplimiento con los objetivos acordados y las medidas a tomar, los planes de expansión a futuro, el plan de marketing y el de mantenimiento.


### 2. TECNOLOGÍAS UTILIZADAS. <a name="id2"></a>

**Django==5.2:** Framework web depara Python usado principalmente para crear APIs y aplicaciones robustas rápidamente.

**mysql-connector-python==8.3.0:** Sistema de gestión de bases de datos relacionales, se utiliza para almacenar y consultar datos.

**djangorestframework==3.16.0:** Extensión de Django para construir APIs RESTful de forma sencilla y estructurada.

**djangorestframework_simplejwt==5.5.0:** Librería para autenticación basada en tokens JWT, que permite login seguro y sin sesiones.

**django-cors-headers==4.7.0:** Middleware para permitir solicitudes entre diferentes dominios (CORS), útil al conectar frontend y backend.

**gunicorn==23.0.0:** Servidor WSGI para ejecutar aplicaciones Django en producción de forma eficiente.

Frontend

**Vue + router:** Framework progresivo de JavaScript usado para construir interfaces de usuario interactivas.

**Axios:** Cliente HTTP que permite hacer solicitudes a APIs desde el frontend.

**Pinia:** Sistema de gestión de estado para Vue 3, útil para compartir datos entre componentes.

### 3. DERECHOS DE AUTOR. <a name="id3"></a>

Hay que recordar que la aplicación hace uso de Open Library API, la cual es de código abierto, la cual usa libros ambos de dominio público y privado, por lo cual hay que tomar ciertas consideraciones como atribuir abiertamente a Open Library por el uso de sus servicios y no distribuir contenido completo de libros que no estén claramente en dominio público.

### 4. GRADO DE CUMPLIMIENTO. <a name="id4"></a>

Se ha implementado todo lo acordado entre el equipo y el supuesto cliente a excepción de que en el frontend no se ha usado la tecnología acordada debido a la falta de tiempo pero ello no ha impedido que el producto final se vea apropiadamente.

Se han conseguido implementar las funciones que componen el producto mínimo viable con excepciones.

El producto final ha resultado limitado desde el punto de vista de estilo y funcionalidades puntuales como el guardado de listas y fotos de perfil.

Entre las funcionalidades acordadas que han sido implementadas destacan:

- Pagina Inicial con ejemplos de las funcionalidades
- Login
- Zona de usuario con sus listas y posts
- Zona de busqueda de librería, posts, listas y usuarios
- Sistema de Foro
- Sistema de creación y administración de listas
- Sistema de moderación básico
- Zona de Admin
- API

Funcionalidades más urgentes a añadir

- Sistema de moderación complejo con feed y bloqueo de cuenta
- Sistema de guardado de listas ajenas
- Implementación de mejoras en la edición de usuario
- Estilos y efectos para elever el frontend

### 5. PLAN DE MARKETING. <a name="id4"></a>

Creemos que la evolución natural de una página como esta es por la vía social, esto implica convertirla en una red social para lectores, añadiendo funcionalidades como seguimiento, feed personalizada, grupos, clubs de lectura con libros designados por el administrador, etc.

Las principales formas de monetización viables para la app son

- **Publicidad:** Un sistema de publicidad poco invasivo localizado principalmente en los laterales de la página, bajo la barra de navegación o en los resultados de búsqueda.

- **Afiliación con librerías virtuales:** Contratar afiliaciones con librerías como Amazon, Book Depository, etc. Añadiendo un sistema de links a las páginas de estos a cambio de una comisión por compra a través de estos.