import time
from selenium import webdriver
from selenium.webdriver.common.by import By #reconoce la funcion "By" 
from selenium.webdriver.common.keys import Keys #reconoce la funcion "Keys" 

driver=webdriver.Chrome()                  # uso de drivers para el navegador chrome
driver.get("https://demoqa.com/text-box")  # ir y abrir la pagina web
driver.maximize_window()                   # maximizar la pagina
time.sleep(2)                              # esperar 2 segundos


# Modo 1 enviar el nombre y la direccion de correo electronico al los campos: nombre y "MAIL":
# nombre = driver.find_element(By.XPATH, "//input[@type='text' and @id='userName']").send_keys("Diana") # enviar la palabra Diana al campo "nombre"
# print("ok ingreso nombre")
# mail_1 = driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']").send_keys("diana@micorreo.com") # enviar la direccion de correo al campo "email"
# print("ok ingreso mail")


# Modo 2 enviar el nombre y la direccion de correo electronico al los campos: nombre y "MAIL":
# mail_1 = driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']") 
# mail_1.send_keys("diana@micorreo.com")  
# print("ok ingreso mail")


# Modo 3 enviar el nombre y la direccion de correo electronico al los campos: nombre y "MAIL":
#varios_campos = driver.find_element(By.XPATH, "//input[@type='text' and @id='userName']").send_keys("Diana")
#varios_campos(Keys.TAB + "diana@micorreo.com") 


# Modo 4 enviar el nombre, la direccion de correo electronico, direcciones y da clic al boton SUBMIT:
# Paso 1: Encuentra el elemento y lo asigna a la variable
varios_campos = driver.find_element(By.XPATH, "//input[@type='text' and @id='userName']")
# Paso 2: Ingresa texto a 3 campos y da clic en el boton SUBMIT
varios_campos.send_keys("Diana")
varios_campos.send_keys(Keys.TAB + "diana@micorreo.com" + Keys.TAB + "Calle 11 # 10-10" + Keys.TAB + "Calle 22 # 11-11" + Keys.TAB + Keys.ENTER)

                 

time.sleep(10)
driver.close()