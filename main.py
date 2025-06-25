from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
import time

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID,'from')
    to_field = (By.ID,'to')
    pedir_taxi_btn = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[1]/div[3]/div[1]/button')
    tarifa = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]')
    numero_tel = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[1]/div')
    phone_field = (By.XPATH, '//*[@id="phone"]')
    siguiente_btn = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[1]/form/div[2]/button')
    confirmar_btn = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/form/div[2]/button[1]')
    cerrar_code_tel = (By.XPATH,'//*[@id="root"]/div/div[1]/div[2]/div[2]/button')
    cerrar_metodo_de_pago = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    metodo_de_pago = (By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[2]/div[1]')
    Efectivo_btn = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[1]/div[2])')
    agregar_card_plus_btn = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[3]/div/img')
    agregar_btn = (By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    card_numero = (By.XPATH,'//*[@id="number"]')
    code_card_field = (By.XPATH,'//*[@id="code"]')
    comment_driver = (By.XPATH,'//*[@id="comment"]')

    def __init__(self,driver):
        self.driver = driver

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

    def pide_taxi(self):
        self.driver.find_element(*self.pedir_taxi_btn).click()

    def set_tarifa(self):
        self.driver.find_element(*self.tarifa).click()

    def set_numero_tel(self):
        self.driver.find_element(*self.numero_tel).click()

    def set_phone(self, number_phone):
        self.driver.find_element(*self.phone_field).send_keys(number_phone)

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')
    
    def set_metodo_de_pago(self):
        self.driver.find_element(*self.metodo_de_pago).click()
        
    def set_efectivo(self):
        self.driver.find_element(*self.efectivo_btn).click()    
        
    def set_agregar_card_plus_btn(self):
        self.driver.find_element(*self.agregar_card_plus_btn).click()

    def set_agregar_btn(self):
        self.driver.find_element(*self.agregar_btn).click() 

    def set_card_number(self,number_card):
        self.driver.find_element(*self.card_numero).send_keys(number_card)
        
    def set_card_code_number(self,code_card_number):
        self.driver.find_element(*self.code_card_field).send_keys(code_card_number)     

    def get_phone(self):
        return self.driver.find_element(*self.phone_field).get_property('value')
    
    def get_card(self):
        return self.driver.find_element(*self.card_number).get_property('value')
    
    def get_code(self):
        return self.driver.find_element(*self.code_card_number).get_property('value') 

    def set_siguiente_btn(self):
        self.driver.find_element(*self.siguiente_btn).click()

    def set_confirmar_btn(self):
        self.driver.find_element(*self.confirmar_btn).click()

    def set_cerrar_code_tel(self):
        self.driver.find_element(*self.cerrar_code_tel).click()
        
    def cerrar_metodo_de_pago(self):
        self.driver.find_element(*self.cerrar_metodo_de_pago).click()
        
    def mensaje_conductor(self,mensaje_cond):
        self.driver.find_element(*self.comment_driver).send_keys(mensaje_cond)

class TestUrbanRoutes:
    driver = None    
    
    @classmethod
    
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        
    def test_set_route(self):        
        self.driver.get(data.urban_routes_url)
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.ID,"from")))
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from,address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_phone(self):
        phone_page = UrbanRoutesPage(self.driver)
        time.sleep(3)
        # Buscar el botón y hacer clic en él
        phone_page.pide_taxi ()        
        
        time.sleep(3)
        # self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[1]/div[5]/div[2]').click()
        phone_page.set_tarifa()
        time.sleep(3)
        phone_page.set_numero_tel()
        time.sleep(5)
        number_phone = data.phone_number
        phone_page.set_phone(number_phone)
        time.sleep(3)
        phone_page.set_siguiente_btn()
        time.sleep(3)
        retrieve_phone_code(self.driver)
        time.sleep(3)
        phone_page.set_confirmar_btn()
        time.sleep(3) 
        phone_page.set_cerrar_code_tel()
        time.sleep(3)
        assert phone_page.get_phone() == number_phone
    def test_set_metodo_de_pago(self):
        pago_page = UrbanRoutesPage(self.driver)
        time.sleep(3)       
        pago_page.set_metodo_de_pago()
        time.sleep(3)
        # Efectivo
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[2]/div[2]/div[1]/button').click()        
        #card_page.set_agregar_card_plus_btn()
        #time.sleep(3)
        #number_card = data.card_number
        #code_card_number = data.card_code        
        #card_page.set_card_number(number_card)
        #WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.ID,"code")))
        #card_page.set_card_code_number(code_card_number)
        #time.sleep(3) 
        #card_page.set_agregar_btn()                
        #card_page.cerrar_metodo_de_pago()
        #assert card_page.get_card() == number_card        
        # def test_set_requisitos(self):
        time.sleep(3)
        #Mensaje al conductor
        mensaje_cond = data.message_for_driver
        pago_page.mensaje_conductor(mensaje_cond)
        #SW Manta y pañuelos
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span').click()
        time.sleep(3)
        # 2 helados
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]').click
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]').click
        time.sleep(5)
        # Reservar
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div[4]/button/span[2]').click()
        time.sleep(10)
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
