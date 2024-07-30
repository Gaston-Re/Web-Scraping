import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
Este script realiza web scraping en una lista de juegos personalizada según la categoría elegida por el usuario.
Extrae información sobre el nombre del juego, las categorías, la fecha de lanzamiento, las reseñas,
el total de reseñas, el precio y el enlace de cada uno de estos juegos.
'''

path = 'C:\\ruta_archivo\\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,)

'''
Segun que lista de juegos quieras extraer agrega la siguiente extencion luego de '/?flavor='
todos los articulos = contenthub_all
novedades destacadas = contenthub_newandtrending
lo mas vendido = contenthub_topsellers
los mejor valorados = contenthub_toprated
en oferta = popularpurchaseddiscounted
proximos lanzamientos = popularcomingsoon
'''

web = 'https://store.steampowered.com/category/action/?flavor=contenthub_all'
driver.get(web)

# Espera hasta que los elementos estén presentes
wait = WebDriverWait(driver, 10)

# Ciclo for para cargar mas juegos en la lista (predefinido en 5, esto extrae 72 juegos)
for _ in range(5):
    ver_mas = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@class="_36qA-3ePJIusV1oKLQep-w"]/button')))
    ver_mas.click()
    time.sleep(1)

# Guarda los elementos
juegos = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="gASJ2lL_xmVNuZkWGvrWg"]')))

# Crea listas para guardar la informacion de los elementos
nombre = []
categorias = []
lanzamiento = []
reseñas = []
total_reseñas = []
precio = []
link = []

# Ciclo 'for' que itera en los elementso guardados
for i in juegos:

    # Extrae el nombre del juego sino lo encuentra carga un none
    try:
        nombre_text = i.find_element(By.XPATH, './/div[@class="_3rrH9dPdtHVRMzAEw82AId"]/a/div').text
        nombre.append(nombre_text if nombre_text else None)
    except:
        nombre.append(None)

    # Extrae las categorias del juego sino las encuentra carga un none
    try:
        categorias_text = i.find_element(By.XPATH, './/div[@class="_3wryhCRrTuMULeq_YjNk-s"]/div[1]').text
        categorias.append(categorias_text if categorias_text else None)
    except:
        categorias.append(None)

    # Extrae la fecha de lanzamiento del juego sino la encuentra carga un none
    try:
        lanzamiento_text = i.find_element(By.XPATH, './/div[@class="_3wryhCRrTuMULeq_YjNk-s"]/div[2]/div').text
        lanzamiento.append(lanzamiento_text if lanzamiento_text else None)
    except:
        lanzamiento.append(None)

    # Extrae el tipo de reseña general del juego sino lo encuentra carga un none
    try:
        reseñas_text = i.find_element(By.XPATH, './/div[@class="_3wryhCRrTuMULeq_YjNk-s"]/a/div/div[1]').text
        reseñas.append(reseñas_text if reseñas_text else None)
    except:
        reseñas.append(None)

    # Extrae el total de las reseñas del juego sino lo encuentra carga un none
    try:
        total_reseñas_text = i.find_element(By.XPATH, './/div[@class="_3wryhCRrTuMULeq_YjNk-s"]/a/div/div[2]').text
        total_reseñas.append(total_reseñas_text if total_reseñas_text else None)
    except:
        total_reseñas.append(None)

    # Extrae el precio del juego sino lo encuentra carga un none
    try:
        precio_text = i.find_element(By.XPATH, './/div[@class="kW6m4Sjqacp5hykrj5LEo"]/div/div[2]').text
        precio.append(precio_text if precio_text else None)
    except:
        precio.append(None)
    
    # Extrae el link del juego sino lo encuentra carga un none
    try:
        link_href = i.find_element(By.XPATH, './/div[@class="_3rrH9dPdtHVRMzAEw82AId"]/a').get_attribute('href')
        link.append(link_href if link_href else None)
    except:
        link.append(None)

# Crea un diccionario con las listas
juegos_categoria = {
            'nombre': nombre,
            'categorias':categorias,
            'lanzamiento':lanzamiento,
            'reseñas':reseñas,
            'total_reseñas':total_reseñas,
            'precio':precio,
            'link':link}

# Crea un DataFrame con el diccionario
juegos_cat = pd.DataFrame(juegos_categoria)
time.sleep(2)

# Cierra el navegador
driver.quit()

# Guarda el DF en un archivo CSV
juegos_cat.to_csv('cat juegos steam.csv', index=False)