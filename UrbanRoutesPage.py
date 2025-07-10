from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
import data
import time 
class UrbanRoutesPage:

    # se agregó clase y archivo UrbanRoutesPage de acuerdo a revision entrega 1
    
    def __init__(self, driver):
        self.driver = driver
    # Prueba1 Route
    from_field = (By.ID,'from')
    to_field = (By.ID,'to')
    # Prueba2 Tarifa
    pedir_taxi_btn = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.type-picker.shown\
    > div.results-container > div.results-text > button')
    tarifa = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    numero_tel = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    # Prueba3 Phone
    phone_btn = (By.CSS_SELECTOR,'#root > div > div.workflow > div.workflow-subcontainer > div.tariff-picker.shown > div.form > div.np-button > div')
    phone_field = (By.XPATH, '//*[@id="phone"]')
    phone_code = (By.ID,'code')
    siguiente_btn = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    confirmar_btn = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    cerrar_code_tel = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/button')
    # Prueba4 Agregar Card
    cerrar_metodo_de_pago_btn = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    metodo_de_pago = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
    efectivo_btn = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    agregar_card_plus_btn = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')
    agregar_btn = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    card_numero = (By.ID,'number')
    code_card_field = (By.ID,'code')
    # Prueba5 Comentario al conductor
    comment_driver = (By.ID,'comment')
    # Prueba6 Requisitos Manta Pañuelos
    sw_manta_pañuelos =(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    # Prueba7 Requisitos Helados
    helados_mas = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    helados_counter = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    # Prueba8 Reservar
    reservar_btn = (By.CSS_SELECTOR,'.smart-button-secondary')
        
   # Metodos de Wait de acuerdo a la revisión de 1ra entrega
  
    # Prueba1 Route
    def wait_for_load_field_from(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.from_field))
    # Prueba2 Tarifa
    def wait_for_load_button_pedir_taxi(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.pedir_taxi_btn))
    def wait_for_load_button_tarifa(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.tarifa))
    # Prueba3 Phone
    def wait_for_load_phone_btn(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.numero_tel))
    def wait_for_load_field_num_tel(self):
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located(self.phone_field))
    def wait_for_load_button_siguiente(self):
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.siguiente_btn))
    def wait_for_load_phone_code(self):        
        WebDriverWait(self.driver,3).until(EC.presence_of_element_located(self.phone_code))
    def wait_for_load_button_confirmar(self):        
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.confirmar_btn))
    def wait_for_load_cerrar_tel_code(self):         
        WebDriverWait(self.driver,3).until(EC.element_to_be_clickable(self.cerrar_code_tel))
    # Prueba4 Agregar Card
    def wait_for_load_metodo_de_pago(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.metodo_de_pago))
    def wait_agregar_card_plus_btn(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.agregar_card_plus_btn))
    def wait_agregar_btn(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.agregar_btn))
    def wait_card_number(self,number_card):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.card_numero))    
    def wait_card_code_number(self,code_card_number):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.code_card_field))  
    def wait_for_load_cerrar_metodo_de_pago(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.cerrar_metodo_de_pago_btn))
    # Prueba5 Mensaje al conductor
    def wait_for_load_mensaje_conductor(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.comment_driver))
    # Prueba6 Requisitos  sw manta pañuelos
    def wait_for_load_sw_manta_pañuelos(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.sw-manta-pañuelos))
    # Prueba7 contador Helados
    def wait_for_load_helados_counter(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.helados_counter))
    # Prueba8 Reservar
    def wait_for_load_button_reservar(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.reservar_btn))

    # Metodos Prueba1 route

    def set_route(self,address_from,address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def set_from(self,address_from):
        self.driver.find_element(*self.from_field).send_keys(address_from)

    def set_to(self, address_to):
        self.driver.find_element(*self.to_field).send_keys(address_to)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Metodos Prueba2 tarifa

    def pide_taxi(self):
        self.driver.find_element(*self.pedir_taxi_btn).click()
    
    def set_tarifa(self):
        self.driver.find_element(*self.tarifa).click()

    def get_tarifa(self):
        return self.driver.find_element(*self.tarifa).is_enabled()

    # Metodos Prueba3 Phone

    def set_numero_tel(self):
        self.driver.find_element(*self.numero_tel).click()

    def set_phone(self, number_phone):
        self.driver.find_element(*self.phone_field).send_keys(number_phone)

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')
    
    def set_siguiente_btn(self):
        self.driver.find_element(*self.siguiente_btn).click()

    def set_confirmar_btn(self):
        self.driver.find_element(*self.confirmar_btn).click()

    def set_cerrar_code_tel(self):
        self.driver.find_element(*self.cerrar_code_tel).click()

    # Metodos Prueba4 de metodo de pago

    def set_metodo_de_pago(self):
        self.driver.find_element(*self.metodo_de_pago).click()
        
    def set_efectivo(self):
        self.driver.find_element(*self.efectivo_btn).click()

    def get_efectivo(self):
        return self.driver.find_element(*self.efectivo_btn).is_enabled()
        
    def set_agregar_card_plus_btn(self):
        self.driver.find_element(*self.agregar_card_plus_btn).click()

    def set_agregar_btn(self):
        self.driver.find_element(*self.agregar_btn).click() 

    def set_card_number(self,number_card):
        self.driver.find_element(*self.card_numero).send_keys(number_card)
        
    def set_card_code_number(self,code_card_number):
        self.driver.find_element(*self.code_card_field).send_keys(code_card_number)

    def get_card(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    def cerrar_metodo_de_pago(self):
        self.driver.find_element(*self.cerrar_metodo_de_pago_btn).click()

    # Metodos Prueba5 de mensaje a conductor
    
    def set_mensaje_conductor(self,mensaje_cond):
        self.driver.find_element(*self.comment_driver).send_keys(mensaje_cond)
        
    def get_mensaje_conductor(self):
        return self.driver.find_element(*self.comment_driver).get_property('value')
    
    # Metodos Prueba6 SW de manta y pañuelos
    
    def set_manta_pañuelos(self,mensaje_cond):
        self.driver.find_element(*self.sw_manta_pañuelos).click()
        
    def get_manta_pañuelos(self):
        return self.driver.find_element(*self.sw_manta_pañuelos).is_enabled()

    # Metodos Prueba7 Helados
    
    def set_helados(self,mensaje_cond):
        self.driver.find_element(*self.helados_mas).click()
        
    def get_helados(self):
        return self.driver.find_element(*self.helados_counter).text

    # Metodos Prueba8 Reservar auto
    
    def set_reserva(self,mensaje_cond):
        self.driver.find_element(*self.reservar_btn).click()
        
    def get_reserva(self):
        return self.driver.find_element(*self.reservar_btn).is_enabled()
