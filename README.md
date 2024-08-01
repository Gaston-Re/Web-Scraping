<h1 align="center">WEB-SCRAPING </h1>

<p align="center">
  <img src="src/imagenwebscraping" alt="webscraping" width="300">
</p>


<hr>
<h1 align="center"> Selenium </h1>
<hr>

<p align="center">
  <img src="src/seleniumimagen" alt="selenium" width="300">
</p>

<h1 align="center">Introducción</h1>

<p align="justify"> 
Bienvenido a este repositorio de proyectos de web scraping, donde encontrarás herramientas diseñadas para extraer datos valiosos de dos populares plataformas: LinkedIn y Steam. Este repositorio contiene scripts y utilidades para realizar scraping de datos de puestos de trabajo publicados en LinkedIn y de información de juegos disponibles en Steam.
</p>


<h1 align="center">Estructura del Repositorio</h1>
<p align="justify"> 
  
  - Scripts/: Contiene scripts y utilidades para realizar scraping de ofertas de empleo en LinkedIn.
    
      -linkedin.py :Script puestos laborales en linkedin.
    
      -steam_juegos_cat.py :Script de lista de juegos por categoria.
    
      -steam_top_jegos.py :Script de steam con top juegos por jugadores actuales con pico diario.
    
  - csv/: Datos extraídos en formatos estructurados CSV.
    
      -cat juegos steam.csv :datasets juegos por cateogria
    
      -job_details.csv :datasets detalles de puestos en linekedin
    
      -links_usa.csv :datasets links de puestos en linkedin
    
      -top juegos.csv :datasets top juegos por jugadores activos
    
  - scv/:  Imagenes asociadas al readme.

<h1 align="center">linkedin</h1>
<p align="justify"> 
  El proceso de este script se divide en dos partes:
    
  - Primera Parte:\n
      Inicia logueando en la página de LinkedIn. Luego de este paso, se dirige a la URL de trabajos. En la misma, busca los elementos para insertar el puesto y la ubicación predefinida en el archivo.             Realiza la búsqueda y comienza un ciclo while con la condición true, el cual ejecuta principalmente la función que extraerá los enlaces de las postulaciones. Antes de esto, comienza a scrollear hacia       abajo para cargar todos los puestos sin inconvenientes. Luego, extrae los links y ejecuta la funcion para el cambio de página que retorna true. Si no se encuentra el botón para pasar a la siguiente         página, retorna false. Estos enlaces extraídos se guardan en una lista, la cual se usará luego para crear un DataFrame y exportar el archivo.
      <p align="center">
        <img src="src/busqueda_linkedin.jpg" alt="busqueda" width="300">
      </p>

  - Segunda Parte:\n
      Carga el archivo guardado en la primera parte. Crea una lista en la cual se guardarán diccionarios e inicia un ciclo for que devolverá los enlaces del DataFrame. Si este enlace no es nulo, se ejecuta       una función de extracción de información, la cual está compuesta por varias sentencias try. La primera realiza clic en el elemento de "ver más" para extraer correctamente la información de la               descripción. Luego, cada sentencia try siguiente está definida para extraer un elemento, como el nombre del puesto, la ubicación, el tipo de empleo, etc. Estas sentencias try individuales evitan que        la falta de un elemento impida extraer la información de los demás. Al concluir la función, se retorna un diccionario que se guarda en la lista mencionada anteriormente. Esta lista se convierte en un       DataFrame y se exporta en formato CSV.
    <p align="center">
      <img src="src/detalles_linkedin.jpg" alt="busqueda" width="300">
    </p>
    <p align="center">
      <img src="src/acerca_linkedin.jpg" alt="busqueda" width="300">
    </p>
    <p align="center">
      <img src="src/aptitudes_linkedin.jpg" alt="busqueda" width="300">
    </p>
    
  - Optimizacion:\n
      Una optimización recomendada es configurar el script para evitar la primera parte. Para esto, se debe configurar para que haga clic en cada postulación y extraiga la información en la ventana               emergente al lado de las postulaciones.
    <p align="center">
      <img src="src/extraccion_linkedin.jpg" alt="busqueda" width="300">
    </p>
    
  *`encontraremos este proceso en el archivo Scripts/linkedin.py`*


<h1 align="center">Steam</h1>
<p align="justify"> 
Esta seccion esta compuesta por dos Scripts

-Primer Script:
  Este realiza una extraccion de juegos por categoria:

*`encontraremos este proceso en los archivos Scripts/steam_juegos_cat.py|Scripts/steam_top_juegos.py`*


<h1 align="center">¿Cómo lo hicimos? 🤔</h1>

1. Extracción y transformación de datos con Python usando las librerías Pandas y Numpy principalmente.

2. Almacenamiento de datos limpios y estructurados con el servicio en la nube Google Cloud Storage

3. Análisis de datos en la nube con BigQuery

4. Modelo de Machine Learning

5. Visualización y reportes con Power Bi


# Metodología de trabajo

<h1 align="center">Stack Tecnológico 🔧</h1>
<p align="justify"> 

🐍 **Python**: Lenguaje utilizado para realizar cálculos estadísticos, crear visualizaciones de datos, construir algoritmos de aprendizaje automático, manipular y analizar datos y completar tareas relacionadas con los datos.

🐼 **Pandas**: Librería de Python Utilizada para la manipulación y análisis de datos estructurados.
master

📈 **Matplotlib**: Librería de Python utilizada para la visualización de datos y generación de gráficos.  

📘 **Visual Studio Code**: Editor de código fuente que permite el desarrollo de las instrucciones para la ejecución de todo el proyecto.

💻 **Power BI**: Power BI es un servicio de análisis de datos de Microsoft orientado a proporcionar visualizaciones interactivas y capacidades de inteligencia empresarial con una interfaz simple.

  ⚡**Hevo**: plataforma de canalización de datos sin mantenimiento que te ayuda a configurar canalizaciones de datos en minutos. Sincroniza automáticamente los datos de todas tus fuentes con el almacén, sin necesidad de mantenimiento.

🔰**Bert**: Red neuronal de código abierto que ha sido entrenada para procesar el lenguaje natural.
  </p>
