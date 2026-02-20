import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce el "By" 

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/text-box")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos


# nombre = driver.find_element(By.ID, "userName")  # encontrar el campo "nombre" por ID = userName
nombre = driver.find_element(By.CSS_SELECTOR, "#userName")  # encontrar el campo "nombre" con CSS SELECTOR por ID = #userName. La anterior linea de codigo es igual a esta linea.
nombre.send_keys("Rodrigo")   # enviar la palabra Rodrigo al campo "nombre"

# driver.find_element(By.ID, "userEmail").send_keys("diana@micorreo.com") #encontrar campo email e ingresar email
driver.find_element(By.XPATH, "//input[contains(@id, 'userEmail')]").send_keys("diana@micorreo.com") #encontrar campo email e ingresar email
time.sleep(1)

driver.execute_script("window.scrollTo(0,300)") #desplazar 300 pixeles el contenido de la pagina para ver mas abajo

driver.find_element(By.XPATH, "//textarea[@id='currentAddress']").send_keys("Calle 12 No. 11 - 10") 
# encontrar campo direccion actual e ingresar ese dato
time.sleep(1)

driver.find_element(By.ID, 'permanentAddress').send_keys("Nota: No tengo otra dirección") #encontrar campo e ingresar direccion permanente
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, "#submit").click() #dar clic en el boton submit
time.sleep(2)

driver.close()