
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

'''
Este script realiza la tarea de hacer web scraping a las publicaciones de empleo en LinkedIn,
enfocándose en realizar una búsqueda personalizada del puesto y lugar deseado. Actualmente,
el script extrae primero los enlaces de las publicaciones de empleo para luego proceder a extraer la información de cada puesto.

En esta primera parte, se puede optimizar el script ajustando el flujo de trabajo para que salte la extracción de enlaces y,
en su lugar, itere directamente sobre cada publicación (ruta XPath: //ul[@class="scaffold-layout__list-container"]/li)
para extraer la información necesaria de cada puesto directamente desde los elementos de la lista.
Esto puede mejorar la eficiencia del script al reducir el número de pasos necesarios para obtener la información deseada.
'''

# Ruta al ChromeDriver
path = 'c:\\ruta_al_archivo\\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

# URL de LinkedIn trabajo
web = 'https://www.linkedin.com/login'
driver.get(web)

# Espera hasta que el botón de inicio de sesión sea clicable y haz clic en él
wait = WebDriverWait(driver, 20)

# Espera hasta que los campos de correo y contraseña estén presentes
email_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[1]/input')))
contraseña_input = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')))
boton_inicio_sesion = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[3]/button')))

# Introduce tu correo y contraseña de linkedin
email_input.send_keys('mail')
contraseña_input.send_keys('contraseña')

boton_inicio_sesion.click()
time.sleep(1)

web = 'https://www.linkedin.com/jobs/'
driver.get(web)

buscar = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/header/div/div[@id="global-nav-search"]')))
buscar.click()

puesto_input = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="relative"]/input[@class="jobs-search-box__text-input jobs-search-box__keyboard-text-input jobs-search-global-typeahead__input"]')))
locacion_input = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="relative"]/input[@class="jobs-search-box__text-input"]')))

# Introduce el puesto de trabajo
puesto_input.clear()  # Asegúrate de que el campo esté vacío
puesto_input.send_keys('Data Engineer')
# Borra el contenido del input de localización
driver.execute_script("arguments[0].value = '';", locacion_input)
# Introduce la nueva localización
locacion_input.send_keys('Estados Unidos')
time.sleep(5) # Tiempo de espera para poder seleccionar la zona si es necesario
locacion_input.send_keys(Keys.ENTER)


# Scroll para poder cargar correctamente los li
def scroll(element, scroll_tiempo_pausa=2, scroll_paso=400, scroll_cantidad=10): #variables para agustar el tiempo entre scroll, desplazamiento y cantidad
    """Desplaza el elemento hacia abajo en un número fijo de veces."""
    for _ in range(scroll_cantidad):
        # Desplaza el elemento hacia abajo en pequeños pasos
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[1];", element, scroll_paso)
        
        # Espera a que los nuevos elementos se carguen
        time.sleep(scroll_tiempo_pausa)


def extract_links():
    time.sleep(2)
    trabajo_links = []
    try:
        # Ejecuta la funcion para realizar el scroll
        elemento = wait.until(EC.presence_of_element_located((By.XPATH, '//main/div/div/div[@class="scaffold-layout__list "]/div')))
        scroll(elemento)

        # Espera un momento para asegurarte de que el scroll se complete, regular atentamente el tiempo de espera para poder cargar correctamente los li
        time.sleep(25)
        trabajo = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//ul[@class="scaffold-layout__list-container"]/li')))
        for trabajo in trabajo:
            link = trabajo.find_element(By.XPATH, './/a[@class="disabled ember-view job-card-container__link job-card-list__title job-card-list__title--link"]').get_attribute('href')
            trabajo_links.append(link)
    except Exception as e:
        print("Exception: No se pudieron encontrar los elementos de trabajo.")
        print(e)
    return trabajo_links


# Funcion para realizar el cambio de paginas
def siguiente_pagina():
    time.sleep(1)
    try:
        boton_siguiente = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Ver siguiente página"]')))
        boton_siguiente.click()
        time.sleep(2)  # Espera para cargar la nueva página
        return True
    except Exception as e:
        print("No se pudo encontrar el botón para la siguiente página o no hay más páginas.")
        print(e)
        return False
    
# Ciclo while para extraer los links y realizar el cambio de pagina
todos_trabajo_links = []
while True:
    todos_trabajo_links.extend(extract_links())
    if not siguiente_pagina():
        break

# Guardar archivos de links
df = pd.DataFrame(todos_trabajo_links, columns=['trabajo_links'])
df.to_csv('links.csv', index=False)

print('aca')
# Cargar archivo guardado
df = pd.read_csv('links.csv')

# Funcion para extraer los detalles de los puestos
def extraer_detalles_trabajo(link):
    driver.get(link)
    time.sleep(3)  # Espera a que la página cargue completamente

    # Clicke "ver mas" para extraer correctamente la descripcion
    try:
        ver_mas = wait.until(EC.element_to_be_clickable((By.XPATH, '//footer/button/span[@class="artdeco-button__text"]')))
        ver_mas.click()
    except Exception as e:
        print(f"No se pudo encontrar o hacer clic en el botón 'Ver más' en el link: {link}")

    # Inicializar variables
    trabajo_titulo = trabajo_locacion = trabajo_tipo = tiempo = trabajo_descripcion = aptitudes = tipo_solicitud = None

    # Titulo
    try:
        trabajo_titulo = wait.until(EC.presence_of_element_located((By.XPATH, '//h1'))).text
    except Exception as e:
        print(f"No se pudo extraer el título del trabajo en el link: {link}")
    
    # Locacion
    try:
        trabajo_locacion = wait.until(EC.presence_of_element_located((By.XPATH, '//div/span[@class="tvm__text tvm__text--low-emphasis"][1]'))).text
    except Exception as e:
        print(f"No se pudo extraer la ubicación del trabajo en el link: {link}")
    
    # Tipo de trabajo
    try:
        trabajo_tipo = wait.until(EC.presence_of_element_located((By.XPATH, '//ul/li[contains(@class, "jobs-unified-top-card__job-insight")][1]/span'))).text
    except Exception as e:
        print(f"No se pudo extraer el tipo de trabajo en el link: {link}")
    
    # Tiempo pasado desde la publicacion del puesto
    try:
        tiempo = wait.until(EC.presence_of_element_located((By.XPATH, '//div/span[@class="tvm__text tvm__text--positive"] | //div/span[@class="tvm__text tvm__text--low-emphasis"][3]'))).text
    except Exception as e:
        print(f"No se pudo extraer el tiempo de trabajo en el link: {link}")
    
    # Aptitudes solicitadas al puesto
    try:
        aptitudes_elements = driver.find_elements(By.XPATH, '//div[@class="pt5"]/div/div/a')
        aptitudes = ', '.join([element.text for element in aptitudes_elements])
    except Exception as e:
        print(f"No se pudieron extraer las aptitudes en el link: {link}")
        aptitudes = None

    # Descripcion del puesto
    try:
        trabajo_descripcion = wait.until(EC.presence_of_element_located((By.XPATH, '//article/div/div[1]'))).text
    except Exception as e:
        print(f"No se pudo extraer la descripción del trabajo en el link: {link}")
    
    # Tipo de solicitud
    try:
        tipo_solicitud = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="mt5"]/div/div/div/button/span[@class="artdeco-button__text"] | //div[@class="mt5"]/div/span'))).text
    except Exception as e:
        print(f"No se pudo extraer el tipo de solicitud en el link: {link}")

    # Devuelve un diccionario el cual agrega a la lista creada de "trabajos_detalles_lista"
    return {
        'trabajo_link': link,
        'trabajo_titulo': trabajo_titulo,
        'trabajo_tipo': trabajo_tipo,
        'tiempo': tiempo,
        'trabajo_locacion': trabajo_locacion,
        'trabajo_descripcion': trabajo_descripcion,
        'aptitudes': aptitudes,
        'tipo_solicitud': tipo_solicitud
    }

# Extraer información adicional para cada enlace en la columna de nuestro df
trabajo_detalle_lista = []
for link in df['trabajo_links']:
    if link:
        trabajo_detalle = extraer_detalles_trabajo(link)
        trabajo_detalle_lista.append(trabajo_detalle)
    else:
        pass

# Guardar los detalles de los trabajos en un archivo CSV
trabajo_detalle_df = pd.DataFrame(trabajo_detalle_lista)
trabajo_detalle_df.to_csv('trabajo_detalle.csv', index=False)

print(f"Total trabajos extraidos: {len(trabajo_detalle_df)}")

# Cerrar el navegador
driver.quit()