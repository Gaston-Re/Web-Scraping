import selenium
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

'''
Este script realiza web scraping para extraer información de la lista de los juegos más jugados por jugadores actuales en Steam.
El script obtiene los siguientes datos: el nombre del juego, el precio,
la cantidad de jugadores actuales y el pico diario de jugadores.
'''

path = 'C:\\ruta_archivo\\chromedriver.exe'
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service,)
web = 'https://store.steampowered.com/charts/mostplayed'
driver.get(web)

# Espera hasta que los elementos estén presentes
wait = WebDriverWait(driver, 10)
juegos = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//tr[@class="_2-RN6nWOY56sNmcDHu069P"]')))

# Crea listas para cargar los datos extraidos
puesto = []
nombre = []
precio = []
j_actuales = []
pico = []

# Ciclo for que extrae la informacion de cada elemento en tipo texto
for i in juegos:
    puesto.append(i.find_element(by='xpath', value='./td[2]').text)
    nombre.append(i.find_element(by='xpath', value='./td[3]').text)
    precio.append(i.find_element(by='xpath', value='./td[4]').text)
    j_actuales.append(i.find_element(by='xpath', value='./td[5]').text)
    pico.append(i.find_element(by='xpath', value='./td[6]').text)

# Crea Diccionarios con toda la informacion para posteriormete crear un DataFrame y guardarlo en un archivo csv
rankin = {'puesto': puesto, 'nombre':nombre, 'precio':precio, 'jugadores_actuales':j_actuales, 'pico_diario':pico}
rankin = pd.DataFrame(rankin)
time.sleep(2)

driver.quit()

rankin.to_csv('top steam.csv', index=False)