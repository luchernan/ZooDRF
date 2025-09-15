# **README del Proyecto Fandit Zoo API**

## **Descripción General**

- **Propósito:** Sistema de gestión de zoológicos y especies animales.
- **Tecnología Principal:** Django REST Framework.
- **Funcionalidad Clave:** Operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para zoológicos, especies y familias.

## **Documentación de la API**

- **Colección de Postman:** Incluida en el repositorio del proyecto.
- **Ubicación del archivo:** Carpeta docs/.
- **Nombre del archivo:** fandit_zoo_api.json.
- **Base de Datos:** Usuario y contraseña del panel /admin de Django en correo electrónico enviado.
- **Detalles:** Migraciones y Fixtures ya aplicadas.
  

## **Puesta en Marcha (Paso a Paso)**

1.  **Requisitos:**

    - Python 3
    - Git

2.  **Clonar Repositorio:**

    - En tu terminal, ejecuta:

    ```bash
     git clone https://github.com/luchernan/ZooDRF
    ```

3.  **Acceder al Directorio:**

    - Ejecuta:

    ```bash
    cd ZooDRF
    ```

4.  **Configurar Entorno Virtual:**

    - **Para Linux/macOS:**

      ```bash
        python3 -m venv venv
      ```

      ```bash
         source venv/bin/activate
      ```

    - **Para Windows (CMD):**

      ```bash
         python -m venv venv
      ```

      ```bash
          venv\\Scripts\\activate
      ```

5.  **Instalar Dependencias:**

    - Con el entorno virtual activado, ejecuta:

    ```bash
       pip install -r requirements.txt
    ```

6.  **Ejecutar el Servidor:**

    - Inicia el servidor de desarrollo con:

    ```bash
       python manage.py runserver
    ```

    - La API estará disponible en: http://127.0.0.1:8000
  
### **Autor**

* **Lucas Hernández** - `luchernan`
