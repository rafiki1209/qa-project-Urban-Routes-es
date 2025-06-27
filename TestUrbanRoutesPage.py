from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
import time
import helpers
import WaitHelpers
import UrbanRoutesPage

class TestUrbanRoutesPage:
    driver = None    
    
    @classmethod
    
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        
    def test_set_route(self):        
        self.driver.get(data.urban_routes_ur.l)
        
        #WaitHelpers        
        
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field_from(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from,address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_set_phone(self):
        phone_page = UrbanRoutesPage(self.driver)        
        #WaitHelpers        
        phone_page.wait_for_load_button_pedir_taxi(self.driver)
        phone_page.pide_taxi ()        
        #WaitHelpers        
        phone_page.wait_for_load_button_tarifa(self.driver)       
        phone_page.set_tarifa()        
        #WaitHelpers        
        phone_page.wait_for_load_field_num_tel(self.driver)
        phone_page.set_numero_tel()        
        number_phone = data.phone_number
        phone_page.set_phone(number_phone)        
        #WaitHelpers        
        phone_page.wait_for_load_button_siguiente(self.driver)
        phone_page.set_siguiente_btn()
        #WaitHelpers
        phone_page.wait_for_load_phone_code(self)
        retrieve_phone_code(self.driver)
        #WaitHelpers
        phone_page.wait_for_load_button_confirmar(self)
        phone_page.set_confirmar_btn()
        #WaitHelpers 
        phone_page.wait_for_load_cerrar_tel_code(self) 
        phone_page.set_cerrar_code_tel()        
        assert phone_page.get_phone() == number_phone
        
    def test_set_metodo_de_pago(self):
        pago_page = UrbanRoutesPage(self.driver)
        #WaitHelpers
        pago_page.wait_for_load_metodo_de_pago(self)       
        pago_page.set_metodo_de_pago()
        wait_for_        
        #WaitHelpers
        pago_page.wait_agregar_card_plus_btn(self)
        pago_page.set_agregar_card_plus_btn()
        #WaitHelpers
        pago_page.wait_card_number(self.driver).
        number_card = data.card_number
       #WaitHelpers 
        pago_page.wait_card_code_number(self.driver)
        code_card_number = data.card_code        
        pago_page.set_card_number(number_card)
       #WaitHelpers 
        pago_page.set_card_code_number(code_card_number)
        pago_page.wait_agregar_btn(self) 
        pago_page.set_agregar_btn()
        #WaitHelpers
        pago_page.wait_for_load_cerrar_metodo_de_pago(self).
        pago_page.cerrar_metodo_de_pago()        
        assert card_page.get_card() == number_card
        
    def test_set_requisitos(self):       
        req_page = UrbanRoutesPage(self.driver)
        #WaitHelpers        
        req_page.wait_for_load_mensaje_conductor(self.driver)        
        mensaje_cond = data.message_for_driver
        #Mensaje al conductor
        mensaje_cond = data.message_for_driver
        pago_page.mensaje_conductor(mensaje_cond)        
        #SW Manta y pañuelos
        #WaitHelpers 
        req_page.wait_for_load_sw_manta_pañuelos(self.driver)
        req_page.set_manta_pañuelos()        
        # 2 helados
        #WaitHelpers 
        req_page.wait_for_load_helados_counter(self.driver)
        req_page.set_helados_counter()
        req_page.set_helados_counter()
        # Reservar
        #WaitHelpers
        req_page.wait_for_load_button_reservar(self)
        req_page.set_reservar_btn(self)
        assert pago_page.get_mensaje_conductor() == mensaje_cond
        time.sleep(10)
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
