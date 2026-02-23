from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By


# Ruta al WebDriver
driver=webdriver.Chrome()
URL_sitio= "http://playsite1.netlify.app/"
sleep(3)


# 1. Navegar a la página de inicio de sesión
print(f"Abriendo la página de login: {URL_sitio}")
driver.get(URL_sitio)
driver.maximize_window()
print("ok visita al sitio web")
sleep(5)

titulo = driver.find_element(By.XPATH, '//h1[@id="titulo"]')
print(titulo.text) # imprimir el texto encontrado en el sitio web.

projectos = driver.find_elements(By.XPATH, "//ul[@style='color:#22d271;']")
for projecto in projectos:
    print(projecto.text)
    with open('Projetos.txt', 'a') as arquivo:
        arquivo.write(projecto.text + "\n")