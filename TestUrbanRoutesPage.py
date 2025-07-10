from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
import data
import time
import helpers
import WaitHelpers 
import UrbanRoutesPage
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

class TestUrbanRoutesPage:
    driver = None     
    @classmethod    
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        
   # Prueba1 Confirmación del establecimiento de la ruta     
    def test_set_route(self):        
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        routes_page.wait_for_load_field_from()
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from,address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to
        
    # Prueba2 Seleccion de tarifa Confort 
    def test_set_tarifa(self):
        tarifa_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        #WaitHelpers
        time.sleep(3)
        tarifa_page.wait_for_load_button_pedir_taxi()
        tarifa_page.pide_taxi ()        
        #WaitHelpers        
        tarifa_page.wait_for_load_button_tarifa()                     
        tarifa_page.set_tarifa()
        assert tarifa_page.get_tarifa() == True

    # Prueba3 phone

    def test_set_phone(self):
        phone_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        phone_page.wait_for_load_phone_btn()
        phone_page.set_numero_tel()        
        number_phone = data.phone_number
        phone_page.wait_for_load_field_num_tel()
        phone_page.set_phone(number_phone)
        phone_page.wait_for_load_button_siguiente()
        phone_page.set_siguiente_btn()
        phone_page.wait_for_load_phone_code()
        retrieve_phone_code(self.driver)
        phone_page.wait_for_load_button_confirmar()
        phone_page.set_confirmar_btn()
        phone_page.wait_for_load_cerrar_tel_code() 
        phone_page.set_cerrar_code_tel()
        assert phone_page.get_phone() == number_phone

    # Prueba4 Metodo de pago

    def test_set_metodo_de_pago(self):
        pago_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        pago_page.wait_for_load_metodo_de_pago()       
        pago_page.set_metodo_de_pago()
        pago_page.set_efectivo()
        assert pago_page.get_efectivo() == True
        
   # Prueba5 verifica que se pueda enviar mensaje para el conductor
   
    def test_set_driver_message(self):       
        req_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        #WaitHelpers        
        #req_page.wait_for_load_mensaje_conductor(self.driver)        
        #Mensaje al conductor
        req_page.wait_for_load_mensaje_conductor()
        mensaje_cond = data.message_for_driver
        req_page.set_mensaje_conductor(mensaje_cond)
        assert req_page.get_mensaje_conductor() == mensaje_cond

    # Prueba6 pide manta y pañuelos

    def test_set_manta_pañuelos(self):       
        req_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        #req_page.wait_for_load_sw_manta_pañuelos()
        req_page.set_manta_pañuelos(self)
        assert req_page.get_manta_pañuelos() == True

    # Prueba7 pide helados

    def test_set_helados(self):       
        req_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        req_page.wait_for_load_helados_counter()
        req_page.set_helados(self)
        req_page.set_helados(self)
        assert req_page.get_helados() == "2"

    # Prueba8 Reserva auto

    def test_set_reserva(self):       
        reserva_page = UrbanRoutesPage.UrbanRoutesPage(self.driver)
        #WaitHelpers        
        #req_page.wait_for_load_mensaje_conductor(self.driver)        
        #Mensaje al conductor
        reserva_page.wait_for_load_button_reservar()
        reserva_page.set_reserva(self)        
        assert reserva_page.get_reserva() == True
        time.sleep (10)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
        
        

    


