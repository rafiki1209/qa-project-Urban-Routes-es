# LEOPOLDO RAFAEL HERNANDEZ GUTIERREZ GPO 29 QAEngineer Sprint 8
# Proyecto de automatización de pruebas de app web Urban Routes

- Ruta del proyecto local

- C:/usuarios/Dell Laptop/Projects/qa-Urban-Routes-app-es

# DESCRIPCIÓN DEL PROYECTO 

Las pruebas están escritas para comprobar la funcionalidad de Urban Routes.

Se definieron los localizadores y métodos necesarios en las clases helpers, WaitHelpers, UrbanRoutesPage y las pruebas en la clase TestUrbanRoutes.

Se desarrollaron las pruebas automatizadas que cubren el proceso completo de pedir un taxi.
Las pruebas cubren estas acciones:

- Configurar la dirección
- Seleccionar la tarifa Comfort
- Rellenar el número de teléfono
- Agregar una tarjeta de crédito
- Se usó la función retrieve_phone_code() que intercepta el código de confirmación requerido para agregar una tarjeta
- Escribir un mensaje para el conductor
- Pedir una manta y pañuelos
- Pedir 2 helados

# CONFIGURACION DEL AMBIENTE

- Python
- Instalar Pytest
- Instalar el paquete requests
- Instalar Selenium WebDriver
- Consola Git Bash

# TEMAS EJERCITADOS Y APLICADOS EN ESTE PROYECTO

- Clases y objetos en Python
- Selenium:Web Driver , localizadores y métodos
- HTML , entendimiento del DOM (Document Object Model) utilizando DevTools del navegador
- Aplicación del POM (Page Object Model) para pruebas 

# EJECUCIÓN DE PRUEBAS 

- 1. Se utiliza el comando pytest projects/qa-project-Urban-Routes-es/TestUrbanRoutesPage.py en la terminal
- 2. Actualizar el URL en el archivo data.py


# CONTROL DE VERSIONES 

- El control de versiones se lleva a cabo a través de Git,
- Autenticarse con SSH para vincular repositorio local con 
- repositorio remoto:

-	ssh -T git@github.com

- Una vez realizadas modificaciones en el repositorio local,
- hay que "empujarlas" al repositorio remoto mediante los 
- siguientes comandos de consola Git Bash:

-	git add .
-	git commit -am "qa-project-Urban-Routes-es
-	git push



