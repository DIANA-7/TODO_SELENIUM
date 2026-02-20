import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://pixabay.com/es/")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos




try:
    # busca el boton "Descuble mas"
    buscar = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".button--9NFL8.tonal--ErkFV.light--C3NP-.center--ZZf40")))
    buscar = driver.find_element(By.CSS_SELECTOR,".button--9NFL8.tonal--ErkFV.light--C3NP-.center--ZZf40")

    # mueve el scroll hasta donde se ubica el elemento encontrado
    ir = driver.execute_script("arguments[0].scrollIntoView();",buscar)
    time.sleep(10)

except TimeoutException as ex:
    print(ex.msg)
    print("El elemento no esta disponible")

